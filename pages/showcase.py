import streamlit as st
import polars as pl
from streamlit_echarts import st_echarts, JsCode

# Page Configuration
st.set_page_config(page_title="ECharts Gallery", layout="wide")


# --- DATA LOADING ---
@st.cache_resource
def get_dataset():
    df = pl.read_csv("data/global_superstore.csv", encoding="latin1")
    df = df.with_columns(
        pl.col("order_date").str.strptime(pl.Date, format="%d-%m-%Y"),
        pl.col("ship_date").str.strptime(pl.Date, format="%d-%m-%Y"),
    )
    return df


df = get_dataset()
max_date = df["order_date"].max()

st.title(":material/bar_chart: ECharts Gallery")
st.markdown(
    "This dashboard is a showcase of **streamlit-echarts**, demonstrating how to integrate "
    "highly interactive ECharts visualizations into Streamlit apps using real-world enterprise data.  \n"
    f"**Analysis period:** {df['order_date'].min()} to {max_date}"
)

# --- SIDEBAR: Filters + Info ---
with st.sidebar:
    st.title(":material/filter_alt: Filters")
    period = st.selectbox(
        "Reporting Period",
        ["1 Month", "3 Months", "6 Months", "12 Months", "24 Months", "All Time"],
        index=3,
    )
    markets = st.multiselect(
        "Market", options=sorted(df["market"].unique().to_list()), default=[]
    )
    categories = st.multiselect(
        "Category", options=sorted(df["category"].unique().to_list()), default=[]
    )
    # Sub-category options depend on selected categories
    if categories:
        sub_cat_options = sorted(
            df.filter(pl.col("category").is_in(categories))["sub_category"]
            .unique()
            .to_list()
        )
    else:
        sub_cat_options = sorted(df["sub_category"].unique().to_list())
    sub_categories = st.multiselect("Sub-Category", options=sub_cat_options, default=[])
    segments = st.selectbox(
        "Customer Segment", options=["All"] + sorted(df["segment"].unique().to_list())
    )

# --- FILTER LOGIC ---

# 1. Date Filtering
period_offsets = {
    "1 Month": "-1mo",
    "3 Months": "-3mo",
    "6 Months": "-6mo",
    "12 Months": "-1y",
    "24 Months": "-2y",
}
if period in period_offsets:
    offset = period_offsets[period]
    current_start = pl.select(pl.lit(max_date).dt.offset_by(offset)).item()
    prev_start = pl.select(pl.lit(current_start).dt.offset_by(offset)).item()
else:  # All Time
    current_start = df["order_date"].min()
    prev_start = None


# 2. Categorical Filtering
def apply_categorical_filters(base_df):
    filtered = base_df
    if markets:
        filtered = filtered.filter(pl.col("market").is_in(markets))
    if categories:
        filtered = filtered.filter(pl.col("category").is_in(categories))
    if sub_categories:
        filtered = filtered.filter(pl.col("sub_category").is_in(sub_categories))
    if segments != "All":
        filtered = filtered.filter(pl.col("segment") == segments)
    return filtered


current_df = apply_categorical_filters(df.filter(pl.col("order_date") >= current_start))

# Previous period
if prev_start:
    prev_df = apply_categorical_filters(
        df.filter(
            (pl.col("order_date") >= prev_start)
            & (pl.col("order_date") < current_start)
        )
    )
else:
    prev_df = None


# ==========================================
# ROW 1: KPIs (4 metrics)
# ==========================================
def get_kpis(data):
    if data is None or data.is_empty():
        return pl.DataFrame(
            {
                "total_revenue": [0.0],
                "profit_margin": [0.0],
                "total_orders": [0],
                "avg_order_value": [0.0],
            }
        )
    total_sales = data["sales"].sum()
    total_profit = data["profit"].sum()
    n_orders = data["order_id"].n_unique()
    return pl.DataFrame(
        {
            "total_revenue": [total_sales],
            "profit_margin": [
                (total_profit / total_sales * 100) if total_sales else 0.0
            ],
            "total_orders": [n_orders],
            "avg_order_value": [(total_sales / n_orders) if n_orders else 0.0],
        }
    )


current_kpis = get_kpis(current_df)
prev_kpis = get_kpis(prev_df)


def get_delta(curr, prev, is_pct=False):
    if prev is None or prev == 0:
        return None
    if is_pct:
        return f"{curr - prev:+.1f}%"
    return f"{(curr - prev) / prev * 100:+.1f}%"


# Sparkline data: monthly aggregates over the current period
sparkline_df = (
    current_df.with_columns(pl.col("order_date").dt.truncate("1mo").alias("month"))
    .group_by("month")
    .agg(
        pl.col("sales").sum().alias("revenue"),
        pl.col("profit").sum().alias("profit"),
        pl.col("order_id").n_unique().alias("orders"),
    )
    .sort("month")
)
if sparkline_df.is_empty():
    spark_revenue = spark_margin = spark_orders = spark_aov = None
else:
    spark_revenue = sparkline_df["revenue"].to_list()
    spark_profit = sparkline_df["profit"].to_list()
    spark_orders = sparkline_df["orders"].to_list()
    spark_margin = [
        round(p / r * 100, 1) if r else 0 for r, p in zip(spark_revenue, spark_profit)
    ]
    spark_aov = [
        round(r / o, 0) if o else 0 for r, o in zip(spark_revenue, spark_orders)
    ]

col1, col2, col3, col4 = st.columns(4)

with col1:
    val = current_kpis["total_revenue"][0] or 0
    delta = (
        get_delta(val, prev_kpis["total_revenue"][0]) if prev_kpis is not None else None
    )
    st.metric(
        "Total Revenue",
        f"${val:,.0f}",
        delta=delta,
        border=True,
        chart_data=spark_revenue,
        chart_type="area",
    )

with col2:
    val = current_kpis["profit_margin"][0] or 0
    delta = (
        get_delta(val, prev_kpis["profit_margin"][0], is_pct=True)
        if prev_kpis is not None
        else None
    )
    st.metric(
        "Profit Margin",
        f"{val:.1f}%",
        delta=delta,
        border=True,
        chart_data=spark_margin,
        chart_type="line",
    )

with col3:
    val = current_kpis["total_orders"][0] or 0
    delta = (
        get_delta(val, prev_kpis["total_orders"][0]) if prev_kpis is not None else None
    )
    st.metric(
        "Total Orders",
        f"{val:,}",
        delta=delta,
        border=True,
        chart_data=spark_orders,
        chart_type="bar",
    )

with col4:
    val = current_kpis["avg_order_value"][0] or 0
    delta = (
        get_delta(val, prev_kpis["avg_order_value"][0])
        if prev_kpis is not None
        else None
    )
    st.metric(
        "Avg. Order Value",
        f"${val:,.0f}",
        delta=delta,
        border=True,
        chart_data=spark_aov,
        chart_type="line",
    )

# ==========================================
# ROW 2: "How are we trending?"
# ==========================================
st.subheader(":material/trending_up: How are we trending?")
st.caption(
    "Track revenue and profit over time with smart aggregation, and spot month-over-month momentum shifts."
)
row2_1, row2_2 = st.columns([3, 2], gap="small")

with row2_1:
    # Smart aggregation based on period
    if period == "1 Month":
        trunc_rule = None  # daily — no truncation
        date_fmt = "%Y-%m-%d"
    elif period == "3 Months":
        trunc_rule = "1w"
        date_fmt = "%Y-%m-%d"
    else:
        trunc_rule = "1mo"
        date_fmt = "%Y-%m"

    if trunc_rule:
        trend_df = (
            current_df.with_columns(
                pl.col("order_date").dt.truncate(trunc_rule).alias("period_date")
            )
            .group_by("period_date")
            .agg(
                pl.col("sales").sum().alias("revenue"),
                pl.col("profit").sum().alias("profit"),
            )
            .sort("period_date")
        )
    else:
        trend_df = (
            current_df.group_by("order_date")
            .agg(
                pl.col("sales").sum().alias("revenue"),
                pl.col("profit").sum().alias("profit"),
            )
            .sort("order_date")
            .rename({"order_date": "period_date"})
        )

    if trend_df.is_empty():
        st.info("No data for the selected filters.")
    else:
        dates = trend_df["period_date"].dt.to_string(date_fmt).to_list()

        options = {
            "title": {"text": "Revenue & Profit Trend", "left": "center", "top": 5},
            "toolbox": {
                "feature": {
                    "saveAsImage": {},
                    "dataView": {"readOnly": True},
                    "restore": {},
                    "magicType": {"type": ["line", "bar"]},
                }
            },
            "tooltip": {
                "trigger": "axis",
                "valueFormatter": JsCode(
                    "function(v){return '$'+Math.round(v).toLocaleString()}"
                ),
            },
            "legend": {"bottom": "0"},
            "xAxis": {"type": "category", "data": dates},
            "yAxis": {"type": "value"},
            "dataZoom": [
                {"type": "inside", "start": 0, "end": 100},
                {"type": "slider", "start": 0, "end": 100, "height": 20, "bottom": 30},
            ],
            "grid": {"bottom": "18%"},
            "series": [
                {
                    "name": "Revenue",
                    "type": "line",
                    "smooth": True,
                    "areaStyle": {"opacity": 0.1},
                    "data": trend_df["revenue"].to_list(),
                },
                {
                    "name": "Profit",
                    "type": "line",
                    "smooth": True,
                    "data": trend_df["profit"].to_list(),
                },
            ],
        }
        st_echarts(options=options, height="400px", key="trend", theme="streamlit")

with row2_2:
    # MoM Revenue Growth
    mom_df = (
        current_df.with_columns(pl.col("order_date").dt.truncate("1mo").alias("month"))
        .group_by("month")
        .agg(pl.col("sales").sum().alias("revenue"))
        .sort("month")
    )

    if mom_df.height <= 2:
        st.info("Need at least 3 months of data to show growth.")
    else:
        mom_df = (
            mom_df.with_columns(
                (
                    (pl.col("revenue") - pl.col("revenue").shift(1))
                    / pl.col("revenue").shift(1)
                    * 100
                ).alias("growth_pct")
            )
            .drop_nulls("growth_pct")
            .slice(1)  # drop first bar — partial month causes extreme spike
        )

        months = mom_df["month"].dt.to_string("%Y-%m").to_list()
        growth_vals = mom_df["growth_pct"].round(1).to_list()

        # Conditional coloring: green for positive, red for negative
        bar_data = []
        for v in growth_vals:
            color = "#91cc75" if v >= 0 else "#ee6666"
            bar_data.append({"value": v, "itemStyle": {"color": color}})

        options = {
            "title": {"text": "MoM Revenue Growth", "left": "center", "top": 5},
            "toolbox": {
                "feature": {
                    "saveAsImage": {},
                    "dataView": {"readOnly": True},
                    "restore": {},
                }
            },
            "tooltip": {"trigger": "axis", "formatter": "{b}<br/>Growth: {c}%"},
            "xAxis": {"type": "category", "data": months, "axisLabel": {"rotate": 45}},
            "yAxis": {"type": "value", "axisLabel": {"formatter": "{value}%"}},
            "grid": {"bottom": "20%", "containLabel": True},
            "series": [{"type": "bar", "data": bar_data, "label": {"show": False}}],
        }
        st_echarts(options=options, height="400px", key="mom_growth", theme="streamlit")

# ==========================================
# ROW 3: "Where & What?"
# ==========================================
st.subheader(":material/explore: Where & What?")
st.caption(
    "Break down performance by category, market, and product to see where revenue and margins concentrate."
)
row3_1, row3_2, row3_3 = st.columns(3)

with row3_1:
    # Treemap: Category → Sub-Category (size=revenue, color=profit margin)
    tree_df = (
        current_df.group_by("category", "sub_category")
        .agg(
            pl.col("sales").sum().alias("revenue"),
            pl.col("profit").sum().alias("profit_sum"),
        )
        .with_columns(
            (
                pl.col("profit_sum")
                / pl.when(pl.col("revenue") != 0).then(pl.col("revenue")).otherwise(1)
                * 100
            ).alias("margin")
        )
        .drop("profit_sum")
    )

    if tree_df.is_empty():
        st.info("No data for treemap.")
    else:
        # Build hierarchical data
        tree_data = []
        for cat in sorted(tree_df["category"].unique().to_list()):
            children = []
            cat_rows = tree_df.filter(pl.col("category") == cat)
            for row in cat_rows.to_dicts():
                children.append(
                    {
                        "name": row["sub_category"],
                        "value": [round(row["revenue"], 2), round(row["margin"], 1)],
                    }
                )
            tree_data.append({"name": cat, "children": children})

        margin_min = tree_df["margin"].min()
        margin_max = tree_df["margin"].max()

        options = {
            "title": {"text": "Category → Sub-Category", "left": "center"},
            "tooltip": {
                "formatter": JsCode(
                    "function(p){"
                    "var v=p.value;"
                    "if(!v||v.length<2)return p.name;"
                    "return p.name+'<br/>Revenue: $'+v[0].toLocaleString()+'<br/>Margin: '+v[1].toFixed(1)+'%';"
                    "}"
                )
            },
            "visualMap": {
                "type": "continuous",
                "min": round(margin_min, 1) if margin_min is not None else -10,
                "max": round(margin_max, 1) if margin_max is not None else 30,
                "inRange": {"color": ["#ee6666", "#fac858", "#91cc75"]},
                "dimension": 1,
                "calculable": True,
                "orient": "horizontal",
                "left": "center",
                "bottom": "0%",
                "text": ["High Margin", "Low Margin"],
            },
            "series": [
                {
                    "type": "treemap",
                    "data": tree_data,
                    "visibleMin": 300,
                    "roam": False,
                    "visualDimension": 1,
                    "levels": [
                        {
                            "itemStyle": {
                                "borderColor": "#555",
                                "borderWidth": 3,
                                "gapWidth": 3,
                            },
                            "upperLabel": {"show": True, "height": 20, "color": "#fff"},
                        },
                        {
                            "itemStyle": {
                                "borderColor": "#aaa",
                                "borderWidth": 1,
                                "gapWidth": 1,
                            },
                            "emphasis": {"itemStyle": {"borderColor": "#333"}},
                        },
                    ],
                }
            ],
        }
        st_echarts(options=options, height="450px", key="treemap", theme="streamlit")

with row3_2:
    # Radar: Market Profiles (normalized)
    radar_df = (
        current_df.group_by("market")
        .agg(
            pl.col("sales").sum().alias("revenue"),
            pl.col("profit").sum().alias("profit"),
            pl.col("order_id").n_unique().alias("orders"),
            pl.col("quantity").sum().alias("quantity"),
        )
        .with_columns(
            (
                pl.col("revenue")
                / pl.when(pl.col("orders") != 0).then(pl.col("orders")).otherwise(1)
            ).alias("aov")
        )
    )

    if radar_df.is_empty():
        st.info("No data for radar chart.")
    else:
        # Normalize each metric to 0-100
        metrics = ["revenue", "profit", "orders", "aov", "quantity"]
        metric_labels = ["Revenue", "Profit", "Orders", "AOV", "Quantity"]

        normalized = radar_df.clone()
        for m in metrics:
            col_max = normalized[m].max()
            if col_max and col_max != 0:
                normalized = normalized.with_columns(
                    (pl.col(m) / col_max * 100).alias(m)
                )

        indicator = [{"name": label, "max": 100} for label in metric_labels]

        series_data = []
        for row in normalized.to_dicts():
            series_data.append(
                {"name": row["market"], "value": [round(row[m], 1) for m in metrics]}
            )

        options = {
            "title": {"text": "Market Profiles", "left": "center"},
            "tooltip": {"trigger": "item"},
            "legend": {
                "bottom": "0",
                "type": "scroll",
                "data": [d["name"] for d in series_data],
            },
            "radar": {
                "indicator": indicator,
                "center": ["50%", "50%"],
                "radius": "60%",
            },
            "series": [
                {"type": "radar", "data": series_data, "areaStyle": {"opacity": 0.1}}
            ],
        }
        st_echarts(options=options, height="450px", key="radar", theme="streamlit")

with row3_3:
    # Top 5 Sub-Categories by Market (stacked horizontal bar)
    top5 = (
        current_df.group_by("sub_category")
        .agg(pl.col("sales").sum().alias("total"))
        .sort("total", descending=True)
        .head(5)
    )
    top5_names = top5["sub_category"].to_list()

    if not top5_names:
        st.info("No data for top 5 chart.")
    else:
        stacked_df = (
            current_df.filter(pl.col("sub_category").is_in(top5_names))
            .group_by("sub_category", "market")
            .agg(pl.col("sales").sum().alias("sales"))
        )
        all_markets = sorted(stacked_df["market"].unique().to_list())
        series = []
        for mkt in all_markets:
            mkt_data = []
            for sc in top5_names:
                val = stacked_df.filter(
                    (pl.col("sub_category") == sc) & (pl.col("market") == mkt)
                )["sales"]
                mkt_data.append(round(val[0], 2) if not val.is_empty() else 0)
            series.append(
                {
                    "name": mkt,
                    "type": "bar",
                    "stack": "total",
                    "emphasis": {"focus": "series"},
                    "data": mkt_data[::-1],
                }
            )

        options = {
            "title": {"text": "Top 5: Revenue by Market", "left": "center"},
            "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
            "legend": {"bottom": "0", "type": "scroll", "textStyle": {"fontSize": 10}},
            "grid": {
                "left": "3%",
                "right": "4%",
                "bottom": "15%",
                "containLabel": True,
            },
            "xAxis": {"type": "value"},
            "yAxis": {"type": "category", "data": top5_names[::-1]},
            "series": series,
        }
        st_echarts(
            options=options, height="450px", key="top5_stacked_bar", theme="streamlit"
        )


# ==========================================
# ROW 4: "Deep Dive" with @st.fragment
# ==========================================
@st.fragment
def drill_down_section():
    left, right = st.columns(2)

    with left:
        # Scatter: x=avg_discount%, y=profit_margin%, size=revenue per sub-category
        sc_df = (
            current_df.group_by("sub_category")
            .agg(
                (pl.col("discount").mean() * 100).alias("avg_discount"),
                pl.col("profit").sum().alias("profit_sum"),
                pl.col("sales").sum().alias("revenue"),
            )
            .with_columns(
                (
                    pl.col("profit_sum")
                    / pl.when(pl.col("revenue") != 0)
                    .then(pl.col("revenue"))
                    .otherwise(1)
                    * 100
                ).alias("profit_margin")
            )
            .drop("profit_sum")
            .sort("sub_category")
        )

        if sc_df.is_empty():
            result = {"selection": {"point_indices": []}}
            scatter_data = []
            st.info("No data for scatter chart.")
        else:
            scatter_data = []
            for row in sc_df.to_dicts():
                scatter_data.append(
                    [
                        round(row["avg_discount"], 1),
                        round(row["profit_margin"], 1),
                        round(row["revenue"], 0),
                        row["sub_category"],
                    ]
                )

            rev_max = sc_df["revenue"].max() or 1

            scatter_opts = {
                "animation": False,
                "title": {"text": "Discount vs Profit Margin", "left": "center"},
                "tooltip": {
                    "trigger": "item",
                    "formatter": JsCode(
                        "function(p){"
                        "var v=p.value;"
                        "return v[3]+'<br/>Discount: '+v[0]+'%<br/>Margin: '+v[1]+'%<br/>Revenue: $'+v[2].toLocaleString();"
                        "}"
                    ),
                },
                "xAxis": {"name": "Avg Discount %", "type": "value"},
                "yAxis": {"name": "Profit Margin %", "type": "value"},
                "visualMap": {
                    "show": False,
                    "dimension": 2,
                    "min": 0,
                    "max": float(rev_max),
                    "inRange": {"symbolSize": [10, 50]},
                },
                "series": [
                    {
                        "type": "scatter",
                        "data": scatter_data,
                        "itemStyle": {"opacity": 0.7},
                        "emphasis": {
                            "itemStyle": {"borderColor": "#333", "borderWidth": 2}
                        },
                    }
                ],
            }
            result = st_echarts(
                options=scatter_opts,
                height="450px",
                key="drill_scatter",
                theme="streamlit",
                on_select="rerun",
                selection_mode="points",
            )

    with right:
        indices = result["selection"].get("point_indices", [])
        if indices and scatter_data:
            clicked_name = scatter_data[indices[0]][3]
            st.markdown(f"**Showing monthly trend for: {clicked_name}**")

            detail_df = current_df.filter(pl.col("sub_category") == clicked_name)
            monthly = (
                detail_df.with_columns(
                    pl.col("order_date").dt.truncate("1mo").alias("month")
                )
                .group_by("month")
                .agg(
                    pl.col("sales").sum().alias("revenue"),
                    pl.col("profit").sum().alias("profit"),
                )
                .sort("month")
            )

            if monthly.is_empty():
                st.info("No monthly data for this sub-category.")
            else:
                month_labels = monthly["month"].dt.to_string("%Y-%m").to_list()
                detail_opts = {
                    "title": {
                        "text": f"{clicked_name} — Monthly Trend",
                        "left": "center",
                    },
                    "tooltip": {
                        "trigger": "axis",
                        "valueFormatter": JsCode(
                            "function(v){return '$'+Math.round(v).toLocaleString()}"
                        ),
                    },
                    "legend": {"bottom": "0"},
                    "xAxis": {"type": "category", "data": month_labels},
                    "yAxis": [
                        {"type": "value", "name": "Revenue"},
                        {"type": "value", "name": "Profit"},
                    ],
                    "grid": {"bottom": "15%"},
                    "series": [
                        {
                            "name": "Revenue",
                            "type": "bar",
                            "data": monthly["revenue"].to_list(),
                        },
                        {
                            "name": "Profit",
                            "type": "line",
                            "yAxisIndex": 1,
                            "smooth": True,
                            "data": monthly["profit"].to_list(),
                        },
                    ],
                }
                st_echarts(
                    options=detail_opts,
                    height="450px",
                    key="drill_detail",
                    theme="streamlit",
                )
        else:
            st.info("👈 Click a bubble to drill into its monthly trend.")


with st.container(border=True):
    st.subheader(":material/touch_app: Deep Dive — Click to Explore")
    st.caption(
        "Uses `@st.fragment` + `on_select` for cross-chart interactivity. "
        "Clicking a bubble re-renders only this section, not the full page."
    )
    drill_down_section()

# ==========================================
# ROW 5: "Operational Insights"
# ==========================================
st.subheader(":material/settings: Operational Insights")
st.caption(
    "Examine shipping patterns, fulfillment speed, and order priority distribution."
)
row5_1, row5_2, row5_3, row5_4 = st.columns(4)

with row5_1:
    # Priority × Ship Mode Heatmap
    heatmap_df = current_df.group_by("order_priority", "ship_mode").agg(
        pl.len().alias("count")
    )

    priorities = ["Critical", "High", "Medium", "Low"]
    modes = ["Same Day", "First Class", "Second Class", "Standard Class"]

    heatmap_data = []
    for row in heatmap_df.to_dicts():
        if row["order_priority"] in priorities and row["ship_mode"] in modes:
            heatmap_data.append(
                [
                    modes.index(row["ship_mode"]),
                    priorities.index(row["order_priority"]),
                    row["count"],
                ]
            )

    options = {
        "title": {"text": "Priority vs. Shipping Mode", "left": "center"},
        "tooltip": {"position": "top"},
        "grid": {"height": "55%", "top": "15%"},
        "xAxis": {"type": "category", "data": modes},
        "yAxis": {"type": "category", "data": priorities},
        "visualMap": {
            "min": 0,
            "max": heatmap_df["count"].max() if not heatmap_df.is_empty() else 100,
            "calculable": True,
            "orient": "horizontal",
            "left": "center",
            "bottom": "0%",
            "inRange": {"color": ["#e0f3f8", "#4575b4"]},
        },
        "series": [
            {
                "name": "Orders",
                "type": "heatmap",
                "data": heatmap_data,
                "label": {"show": True},
                "emphasis": {
                    "itemStyle": {"shadowBlur": 10, "shadowColor": "rgba(0, 0, 0, 0.5)"}
                },
            }
        ],
    }
    st_echarts(
        options=options, height="450px", key="shipping_heatmap", theme="streamlit"
    )

with row5_2:
    # Shipping Cost vs Profit by Ship Mode — horizontal bar
    ship_df = (
        current_df.group_by("ship_mode")
        .agg(
            pl.col("shipping_cost").mean().alias("avg_shipping"),
            pl.col("profit").mean().alias("avg_profit"),
        )
        .sort("ship_mode")
    )

    if ship_df.is_empty():
        st.info("No shipping data.")
    else:
        ship_modes = ship_df["ship_mode"].to_list()
        options = {
            "title": {"text": "Avg Shipping Cost vs Profit by Mode", "left": "center"},
            "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
            "legend": {"bottom": "0"},
            "grid": {
                "left": "3%",
                "right": "4%",
                "bottom": "12%",
                "containLabel": True,
            },
            "yAxis": {"type": "category", "data": ship_modes},
            "xAxis": {"type": "value"},
            "series": [
                {
                    "name": "Avg Shipping Cost",
                    "type": "bar",
                    "data": ship_df["avg_shipping"].round(2).to_list(),
                    "itemStyle": {"color": "#5470c6"},
                },
                {
                    "name": "Avg Profit",
                    "type": "bar",
                    "data": ship_df["avg_profit"].round(2).to_list(),
                    "itemStyle": {"color": "#91cc75"},
                },
            ],
        }
        st_echarts(
            options=options, height="450px", key="ship_cost_profit", theme="streamlit"
        )

with row5_3:
    # Shipping Delay Distribution (ship_date - order_date)
    delay_df = (
        current_df.with_columns(
            (pl.col("ship_date") - pl.col("order_date"))
            .dt.total_days()
            .alias("ship_days")
        )
        .group_by("ship_days")
        .agg(pl.len().alias("count"))
        .sort("ship_days")
        .filter(pl.col("ship_days") >= 0)
    )

    if delay_df.is_empty():
        st.info("No shipping delay data.")
    else:
        day_labels = [f"{d}d" for d in delay_df["ship_days"].to_list()]
        options = {
            "title": {"text": "Shipping Delay", "left": "center"},
            "tooltip": {"trigger": "axis", "formatter": "{b}: {c} orders"},
            "xAxis": {"type": "category", "data": day_labels, "name": "Days to Ship"},
            "yAxis": {"type": "value"},
            "series": [
                {
                    "type": "bar",
                    "data": delay_df["count"].to_list(),
                    "itemStyle": {"color": "#5470c6"},
                }
            ],
        }
        st_echarts(options=options, height="450px", key="ship_delay", theme="streamlit")

with row5_4:
    # Order Priority Distribution (donut)
    priority_df = (
        current_df.group_by("order_priority")
        .agg(pl.len().alias("count"))
        .sort("count", descending=True)
    )

    if priority_df.is_empty():
        st.info("No priority data.")
    else:
        options = {
            "title": {"text": "Order Priority", "left": "center"},
            "tooltip": {"trigger": "item", "formatter": "{b}: {c} ({d}%)"},
            "series": [
                {
                    "type": "pie",
                    "radius": ["40%", "70%"],
                    "avoidLabelOverlap": True,
                    "itemStyle": {
                        "borderRadius": 10,
                        "borderColor": "#fff",
                        "borderWidth": 2,
                    },
                    "label": {"show": True, "formatter": "{b}: {d}%"},
                    "emphasis": {
                        "label": {"show": True, "fontSize": "14", "fontWeight": "bold"},
                        "itemStyle": {
                            "shadowBlur": 10,
                            "shadowOffsetX": 0,
                            "shadowColor": "rgba(0, 0, 0, 0.5)",
                        },
                    },
                    "data": [
                        {"name": r["order_priority"], "value": r["count"]}
                        for r in priority_df.to_dicts()
                    ],
                }
            ],
        }
        st_echarts(
            options=options, height="450px", key="priority_donut", theme="streamlit"
        )

# --- Data Preview ---
with st.expander("📝 Raw Data Preview"):
    st.dataframe(current_df.head(100).to_pandas(), use_container_width=True)

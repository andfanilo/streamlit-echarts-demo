import streamlit as st
from streamlit_echarts import st_echarts


st.title("Showcase")
st.caption("A gallery of ECharts chart types rendered with streamlit-echarts.")

# --- Row 1: Bar, Line, Pie ---
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Bar")
    st_echarts(
        options={
            "xAxis": {"type": "category", "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]},
            "yAxis": {"type": "value"},
            "series": [{"data": [120, 200, 150, 80, 70, 110, 130], "type": "bar"}],
            "tooltip": {"trigger": "axis"},
        },
        height="300px",
        key="showcase_bar",
    )

with col2:
    st.subheader("Line")
    st_echarts(
        options={
            "xAxis": {"type": "category", "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]},
            "yAxis": {"type": "value"},
            "series": [{"data": [820, 932, 901, 934, 1290, 1330, 1320], "type": "line", "smooth": True}],
            "tooltip": {"trigger": "axis"},
        },
        height="300px",
        key="showcase_line",
    )

with col3:
    st.subheader("Pie")
    st_echarts(
        options={
            "tooltip": {"trigger": "item"},
            "series": [
                {
                    "type": "pie",
                    "radius": ["40%", "70%"],
                    "data": [
                        {"value": 1048, "name": "Search"},
                        {"value": 735, "name": "Direct"},
                        {"value": 580, "name": "Email"},
                        {"value": 484, "name": "Ads"},
                    ],
                    "emphasis": {"itemStyle": {"shadowBlur": 10, "shadowColor": "rgba(0,0,0,0.5)"}},
                }
            ],
        },
        height="300px",
        key="showcase_pie",
    )

# --- Row 2: Scatter, Radar, Gauge ---
col4, col5, col6 = st.columns(3)

with col4:
    st.subheader("Scatter")
    st_echarts(
        options={
            "xAxis": {},
            "yAxis": {},
            "series": [
                {
                    "symbolSize": 15,
                    "data": [
                        [10.0, 8.04], [8.07, 6.95], [13.0, 7.58], [9.05, 8.81],
                        [11.0, 8.33], [14.0, 7.66], [13.4, 6.81], [10.0, 6.33],
                        [14.0, 8.96], [12.5, 6.82], [9.15, 7.20], [11.5, 7.20],
                        [3.03, 4.23], [12.2, 7.83], [2.02, 4.47], [1.05, 3.33],
                    ],
                    "type": "scatter",
                }
            ],
            "tooltip": {"trigger": "item"},
        },
        height="300px",
        key="showcase_scatter",
    )

with col5:
    st.subheader("Radar")
    st_echarts(
        options={
            "radar": {
                "indicator": [
                    {"name": "Sales", "max": 6500},
                    {"name": "Admin", "max": 16000},
                    {"name": "IT", "max": 30000},
                    {"name": "Support", "max": 38000},
                    {"name": "Dev", "max": 52000},
                    {"name": "Marketing", "max": 25000},
                ],
            },
            "series": [
                {
                    "type": "radar",
                    "data": [
                        {"value": [4200, 3000, 20000, 35000, 50000, 18000], "name": "Budget"},
                        {"value": [5000, 14000, 28000, 26000, 42000, 21000], "name": "Spending"},
                    ],
                }
            ],
            "tooltip": {},
        },
        height="300px",
        key="showcase_radar",
    )

with col6:
    st.subheader("Gauge")
    st_echarts(
        options={
            "series": [
                {
                    "type": "gauge",
                    "detail": {"formatter": "{value}%"},
                    "data": [{"value": 72, "name": "Score"}],
                }
            ],
            "tooltip": {"formatter": "{b}: {c}%"},
        },
        height="300px",
        key="showcase_gauge",
    )

# --- Row 3: Funnel, Heatmap, Sankey ---
col7, col8, col9 = st.columns(3)

with col7:
    st.subheader("Funnel")
    st_echarts(
        options={
            "tooltip": {"trigger": "item", "formatter": "{b}: {c}%"},
            "series": [
                {
                    "type": "funnel",
                    "data": [
                        {"value": 100, "name": "Show"},
                        {"value": 80, "name": "Click"},
                        {"value": 60, "name": "Visit"},
                        {"value": 40, "name": "Inquiry"},
                        {"value": 20, "name": "Order"},
                    ],
                }
            ],
        },
        height="300px",
        key="showcase_funnel",
    )

with col8:
    st.subheader("Heatmap")
    hours = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    categories = ["Email", "Ads", "Video", "Direct", "Search"]
    data = [
        [i, j, int((i * 3 + j * 7 + 5) % 11)]
        for i in range(5)
        for j in range(5)
    ]
    st_echarts(
        options={
            "xAxis": {"type": "category", "data": hours},
            "yAxis": {"type": "category", "data": categories},
            "visualMap": {"min": 0, "max": 10, "show": False},
            "series": [
                {
                    "type": "heatmap",
                    "data": data,
                    "label": {"show": True},
                }
            ],
            "tooltip": {},
        },
        height="300px",
        key="showcase_heatmap",
    )

with col9:
    st.subheader("Sunburst")
    st_echarts(
        options={
            "series": [
                {
                    "type": "sunburst",
                    "data": [
                        {
                            "name": "A",
                            "children": [
                                {"name": "A1", "value": 15},
                                {"name": "A2", "value": 10},
                            ],
                        },
                        {
                            "name": "B",
                            "children": [
                                {"name": "B1", "value": 20},
                                {"name": "B2", "value": 8},
                                {"name": "B3", "value": 12},
                            ],
                        },
                        {
                            "name": "C",
                            "children": [
                                {"name": "C1", "value": 18},
                                {"name": "C2", "value": 6},
                            ],
                        },
                    ],
                    "radius": ["15%", "90%"],
                    "emphasis": {"focus": "ancestor"},
                }
            ],
            "tooltip": {},
        },
        height="300px",
        key="showcase_sunburst",
    )

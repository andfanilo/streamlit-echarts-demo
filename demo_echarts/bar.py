import streamlit as st
from streamlit_echarts import JsCode
from streamlit_echarts import st_echarts


def render_basic_bar():
    options = {
        "xAxis": {
            "type": "category",
            "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        },
        "yAxis": {"type": "value"},
        "series": [{"data": [120, 200, 150, 80, 70, 110, 130], "type": "bar"}],
    }
    st_echarts(options=options, height="500px")


def render_bar_background():
    options = {
        "xAxis": {
            "type": "category",
            "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        },
        "yAxis": {"type": "value"},
        "series": [
            {
                "data": [120, 200, 150, 80, 70, 110, 130],
                "type": "bar",
                "showBackground": True,
                "backgroundStyle": {"color": "rgba(180, 180, 180, 0.2)"},
            }
        ],
    }
    st_echarts(options=options, height="500px")


def render_set_style_of_single_bar():
    options = {
        "xAxis": {
            "type": "category",
            "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        },
        "yAxis": {"type": "value"},
        "series": [
            {
                "data": [
                    120,
                    {"value": 200, "itemStyle": {"color": "#a90000"}},
                    150,
                    80,
                    70,
                    110,
                    130,
                ],
                "type": "bar",
            }
        ],
    }
    st_echarts(
        options=options,
        height="500px",
    )


def render_waterfall_chart():
    options = {
        "title": {"text": "Accumulated Waterfall Chart"},
        "tooltip": {
            "trigger": "axis",
            "axisPointer": {"type": "shadow"},
            "formatter": JsCode(
                """
                function (params) {
                  let tar;
                  if (params[1] && params[1].value !== '-') {
                    tar = params[1];
                  } else {
                    tar = params[2];
                  }
                  return tar && tar.name + '<br/>' + tar.seriesName + ' : ' + tar.value;
                }
                """
            ).js_code,
        },
        "legend": {"data": ["Expenses", "Income"]},
        "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
        "xAxis": {
            "type": "category",
            "data": [f"Nov {i}" for i in range(1, 12)],
        },
        "yAxis": {"type": "value"},
        "series": [
            {
                "name": "Placeholder",
                "type": "bar",
                "stack": "Total",
                "silent": True,
                "itemStyle": {
                    "borderColor": "transparent",
                    "color": "transparent",
                },
                "emphasis": {
                    "itemStyle": {
                        "borderColor": "transparent",
                        "color": "transparent",
                    }
                },
                "data": [0, 900, 1245, 1530, 1376, 1376, 1511, 1689, 1856, 1495, 1292],
            },
            {
                "name": "Income",
                "type": "bar",
                "stack": "Total",
                "label": {"show": True, "position": "top"},
                "data": [900, 345, 393, "-", "-", 135, 178, 286, "-", "-", "-"],
            },
            {
                "name": "Expenses",
                "type": "bar",
                "stack": "Total",
                "label": {"show": True, "position": "bottom"},
                "data": ["-", "-", "-", 108, 154, "-", "-", "-", 119, 361, 203],
            },
        ],
    }
    st_echarts(options=options, height="500px")


def render_stacked_horizontal_bar():
    options = {
        "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
        "legend": {
            "data": ["Direct", "Mail Ad", "Affiliate Ad", "Video Ad", "Search Engine"]
        },
        "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
        "xAxis": {"type": "value"},
        "yAxis": {
            "type": "category",
            "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        },
        "series": [
            {
                "name": "Direct",
                "type": "bar",
                "stack": "total",
                "label": {"show": True},
                "emphasis": {"focus": "series"},
                "data": [320, 302, 301, 334, 390, 330, 320],
            },
            {
                "name": "Mail Ad",
                "type": "bar",
                "stack": "total",
                "label": {"show": True},
                "emphasis": {"focus": "series"},
                "data": [120, 132, 101, 134, 90, 230, 210],
            },
            {
                "name": "Affiliate Ad",
                "type": "bar",
                "stack": "total",
                "label": {"show": True},
                "emphasis": {"focus": "series"},
                "data": [220, 182, 191, 234, 290, 330, 310],
            },
            {
                "name": "Video Ad",
                "type": "bar",
                "stack": "total",
                "label": {"show": True},
                "emphasis": {"focus": "series"},
                "data": [150, 212, 201, 154, 190, 330, 410],
            },
            {
                "name": "Search Engine",
                "type": "bar",
                "stack": "total",
                "label": {"show": True},
                "emphasis": {"focus": "series"},
                "data": [820, 832, 901, 934, 1290, 1330, 1320],
            },
        ],
    }
    st_echarts(options=options, height="500px")


def render_mixed_line_bar():
    options = {
        "tooltip": {
            "trigger": "axis",
            "axisPointer": {"type": "cross", "crossStyle": {"color": "#999"}},
        },
        "toolbox": {
            "feature": {
                "dataView": {"show": True, "readOnly": False},
                "magicType": {"show": True, "type": ["line", "bar"]},
                "restore": {"show": True},
                "saveAsImage": {"show": True},
            }
        },
        "legend": {"data": ["Evaporation", "Precipitation", "Temperature"]},
        "xAxis": [
            {
                "type": "category",
                "data": [
                    "Jan",
                    "Feb",
                    "Mar",
                    "Apr",
                    "May",
                    "Jun",
                    "Jul",
                    "Aug",
                    "Sep",
                    "Oct",
                    "Nov",
                    "Dec",
                ],
                "axisPointer": {"type": "shadow"},
            }
        ],
        "yAxis": [
            {
                "type": "value",
                "name": "Precipitation",
                "min": 0,
                "max": 250,
                "interval": 50,
                "axisLabel": {"formatter": "{value} ml"},
            },
            {
                "type": "value",
                "name": "Temperature",
                "min": 0,
                "max": 25,
                "interval": 5,
                "axisLabel": {"formatter": "{value} °C"},
            },
        ],
        "series": [
            {
                "name": "Evaporation",
                "type": "bar",
                "tooltip": {
                    "valueFormatter": JsCode(
                        "function (value) { return value + ' ml'; }"
                    ).js_code
                },
                "data": [
                    2.0,
                    4.9,
                    7.0,
                    23.2,
                    25.6,
                    76.7,
                    135.6,
                    162.2,
                    32.6,
                    20.0,
                    6.4,
                    3.3,
                ],
            },
            {
                "name": "Precipitation",
                "type": "bar",
                "tooltip": {
                    "valueFormatter": JsCode(
                        "function (value) { return value + ' ml'; }"
                    ).js_code
                },
                "data": [
                    2.6,
                    5.9,
                    9.0,
                    26.4,
                    28.7,
                    70.7,
                    175.6,
                    182.2,
                    48.7,
                    18.8,
                    6.0,
                    2.3,
                ],
            },
            {
                "name": "Temperature",
                "type": "line",
                "yAxisIndex": 1,
                "tooltip": {
                    "valueFormatter": JsCode(
                        "function (value) { return value + ' °C'; }"
                    ).js_code
                },
                "data": [
                    2.0,
                    2.2,
                    3.3,
                    4.5,
                    6.3,
                    10.2,
                    20.3,
                    23.4,
                    23.0,
                    16.5,
                    12.0,
                    6.2,
                ],
            },
        ],
    }
    st_echarts(options=options, height="500px")


def render_polar_bar_label_tangential():
    options = {
        "title": [{"text": "Tangential Polar Bar Label Position (middle)"}],
        "polar": {"radius": [30, "80%"]},
        "angleAxis": {"max": 4, "startAngle": 75},
        "radiusAxis": {"type": "category", "data": ["a", "b", "c", "d"]},
        "tooltip": {},
        "series": [
            {
                "type": "bar",
                "data": [2, 1.2, 2.4, 3.6],
                "coordinateSystem": "polar",
                "label": {
                    "show": True,
                    "position": "middle",
                    "formatter": "{b}: {c}",
                },
            }
        ],
    }
    st_echarts(options=options, height="500px")


def render_bar_stack_normalization():
    raw_data = [
        [100, 302, 301, 334, 390, 330, 320],
        [320, 132, 101, 134, 90, 230, 210],
        [220, 182, 191, 234, 290, 330, 310],
        [150, 212, 201, 154, 190, 330, 410],
        [820, 832, 901, 934, 1290, 1330, 1320],
    ]
    total_data = []
    for i in range(len(raw_data[0])):
        sum_val = 0
        for j in range(len(raw_data)):
            sum_val += raw_data[j][i]
        total_data.append(sum_val)

    series_names = ["Direct", "Mail Ad", "Affiliate Ad", "Video Ad", "Search Engine"]
    series = []
    for sid, name in enumerate(series_names):
        series.append(
            {
                "name": name,
                "type": "bar",
                "stack": "total",
                "barWidth": "60%",
                "label": {
                    "show": True,
                    "formatter": JsCode(
                        "function(params) { return Math.round(params.value * 1000) / 10 + '%'; }"
                    ).js_code,
                },
                "data": [
                    (0 if total_data[did] <= 0 else d / total_data[did])
                    for did, d in enumerate(raw_data[sid])
                ],
            }
        )

    options = {
        "legend": {"selectedMode": False},
        "yAxis": {"type": "value"},
        "xAxis": {
            "type": "category",
            "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        },
        "series": series,
    }
    st_echarts(options=options, height="500px")


def render_bar_series_layout_by():
    options = {
        "legend": {},
        "tooltip": {},
        "dataset": {
            "source": [
                ["product", "2012", "2013", "2014", "2015"],
                ["Matcha Latte", 41.1, 30.4, 65.1, 53.3],
                ["Milk Tea", 86.5, 92.1, 85.7, 83.1],
                ["Cheese Cocoa", 24.1, 67.2, 79.5, 86.4],
            ]
        },
        "xAxis": [
            {"type": "category", "gridIndex": 0},
            {"type": "category", "gridIndex": 1},
        ],
        "yAxis": [{"gridIndex": 0}, {"gridIndex": 1}],
        "grid": [{"bottom": "55%"}, {"top": "55%"}],
        "series": [
            # These series are in the first grid.
            {"type": "bar", "seriesLayoutBy": "row"},
            {"type": "bar", "seriesLayoutBy": "row"},
            {"type": "bar", "seriesLayoutBy": "row"},
            # These series are in the second grid.
            {"type": "bar", "xAxisIndex": 1, "yAxisIndex": 1},
            {"type": "bar", "xAxisIndex": 1, "yAxisIndex": 1},
            {"type": "bar", "xAxisIndex": 1, "yAxisIndex": 1},
            {"type": "bar", "xAxisIndex": 1, "yAxisIndex": 1},
        ],
    }
    st_echarts(options=options, height="500px")


def render_bar_drilldown():
    drilldown_data = {
        "animals": [["Cats", 4], ["Dogs", 2], ["Cows", 1], ["Sheep", 2], ["Pigs", 1]],
        "fruits": [["Apples", 4], ["Oranges", 2]],
        "cars": [["Toyota", 4], ["Opel", 2], ["Volkswagen", 2]],
    }

    if "bar_drilldown_group" not in st.session_state:
        st.session_state.bar_drilldown_group = None

    group = st.session_state.bar_drilldown_group

    if group is None:
        options = {
            "xAxis": {"data": ["Animals", "Fruits", "Cars"]},
            "yAxis": {},
            "animationDurationUpdate": 500,
            "series": {
                "type": "bar",
                "id": "sales",
                "data": [
                    {"value": 5, "groupId": "animals"},
                    {"value": 2, "groupId": "fruits"},
                    {"value": 4, "groupId": "cars"},
                ],
                "universalTransition": {"enabled": True, "divideShape": "clone"},
            },
        }
    else:
        sub_data = drilldown_data[group]
        options = {
            "xAxis": {"data": [item[0] for item in sub_data]},
            "yAxis": {},
            "animationDurationUpdate": 500,
            "series": {
                "type": "bar",
                "id": "sales",
                "dataGroupId": group,
                "data": [item[1] for item in sub_data],
                "universalTransition": {"enabled": True, "divideShape": "clone"},
            },
        }

    events = {
        "click": "function(params) { return params.data && params.data.groupId ? params.data.groupId : null }",
    }

    if group is not None:
        if st.button("Back", key="bar_drilldown_back"):
            st.session_state.bar_drilldown_group = None
            st.rerun()

    result = st_echarts(
        options=options,
        events=events,
        height="500px",
        replace_merge="series",
        key="render_bar_drilldown",
    )
    if result and result.chart_event and result.chart_event in drilldown_data:
        st.session_state.bar_drilldown_group = result.chart_event
        st.rerun()


ST_BAR_DEMOS = {
    "Basic bar": (
        render_basic_bar,
        "https://echarts.apache.org/examples/en/editor.html?c=bar-simple",
    ),
    "Bar with Background": (
        render_bar_background,
        "https://echarts.apache.org/examples/en/editor.html?c=bar-background",
    ),
    "Set Style Of Single Bar": (
        render_set_style_of_single_bar,
        "https://echarts.apache.org/examples/en/editor.html?c=bar-data-color",
    ),
    "Waterfall Chart": (
        render_waterfall_chart,
        "https://echarts.apache.org/examples/en/editor.html?c=bar-waterfall2",
    ),
    "Stacked Horizontal Bar": (
        render_stacked_horizontal_bar,
        "https://echarts.apache.org/examples/en/editor.html?c=bar-y-category-stack",
    ),
    "Mixed Line and Bar": (
        render_mixed_line_bar,
        "https://echarts.apache.org/examples/en/editor.html?c=mix-line-bar",
    ),
    "Tangential Polar Bar Label Position": (
        render_polar_bar_label_tangential,
        "https://echarts.apache.org/examples/en/editor.html?c=bar-polar-label-tangential",
    ),
    "Stacked Bar Normalization": (
        render_bar_stack_normalization,
        "https://echarts.apache.org/examples/en/editor.html?c=bar-stack-normalization",
    ),
    "Series Layout By Column or Row": (
        render_bar_series_layout_by,
        "https://echarts.apache.org/examples/en/editor.html?c=dataset-series-layout-by",
    ),
    "Bar Chart Drilldown": (
        render_bar_drilldown,
        "https://echarts.apache.org/examples/en/editor.html?c=bar-drilldown",
    ),
}

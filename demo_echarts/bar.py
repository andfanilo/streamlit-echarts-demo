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
        height="400px",
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


ST_BAR_DEMOS = {
    "Basic bar": (
        render_basic_bar,
        "https://echarts.apache.org/examples/en/editor.html?c=bar-simple",
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
}

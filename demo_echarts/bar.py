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
        "title": {
            "text": "阶梯瀑布图",
            "subtext": "From ExcelHome",
            "sublink": "http://e.weibo.com/1341556070/Aj1J2x5a5",
        },
        "tooltip": {
            "trigger": "axis",
            "axisPointer": {"type": "shadow"},
            "formatter": JsCode(
                "function(params){var tar;if(params[1].value!=='-'){tar=params[1]}else{tar=params[0]}return tar.name+'<br/>'+tar.seriesName+' : '+tar.value}"
            ).js_code,
        },
        "legend": {"data": ["支出", "收入"]},
        "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
        "xAxis": {
            "type": "category",
            "splitLine": {"show": False},
            "data": [f"11月 {i} 日" for i in range(1, 12)],
        },
        "yAxis": {"type": "value"},
        "series": [
            {
                "name": "辅助",
                "type": "bar",
                "stack": "总量",
                "itemStyle": {
                    "barBorderColor": "rgba(0,0,0,0)",
                    "color": "rgba(0,0,0,0)",
                },
                "emphasis": {
                    "itemStyle": {
                        "barBorderColor": "rgba(0,0,0,0)",
                        "color": "rgba(0,0,0,0)",
                    }
                },
                "data": [0, 900, 1245, 1530, 1376, 1376, 1511, 1689, 1856, 1495, 1292],
            },
            {
                "name": "收入",
                "type": "bar",
                "stack": "总量",
                "label": {"show": True, "position": "top"},
                "data": [900, 345, 393, "-", "-", 135, 178, 286, "-", "-", "-"],
            },
            {
                "name": "支出",
                "type": "bar",
                "stack": "总量",
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


ST_BAR_DEMOS = {
    "Bar: Basic bar": (
        render_basic_bar,
        "https://echarts.apache.org/examples/en/editor.html?c=bar-simple",
    ),
    "Bar: Set Style Of Single Bar": (
        render_set_style_of_single_bar,
        "https://echarts.apache.org/examples/en/editor.html?c=bar-data-color",
    ),
    "Bar: Waterfall Chart": (
        render_waterfall_chart,
        "https://echarts.apache.org/examples/en/editor.html?c=bar-waterfall2",
    ),
    "Bar: Stacked Horizontal Bar": (
        render_stacked_horizontal_bar,
        "https://echarts.apache.org/examples/en/editor.html?c=bar-y-category-stack",
    ),
}

import json
from streamlit_echarts import st_echarts
from streamlit_echarts import JsCode


def render_basic_line_chart():
    option = {
        "xAxis": {
            "type": "category",
            "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        },
        "yAxis": {"type": "value"},
        "series": [{"data": [820, 932, 901, 934, 1290, 1330, 1320], "type": "line"}],
    }
    st_echarts(
        options=option, height="400px",
    )


def render_basic_area_chart():
    options = {
        "xAxis": {
            "type": "category",
            "boundaryGap": False,
            "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        },
        "yAxis": {"type": "value"},
        "series": [
            {
                "data": [820, 932, 901, 934, 1290, 1330, 1320],
                "type": "line",
                "areaStyle": {},
            }
        ],
    }
    st_echarts(options=options)


def render_stacked_line_chart():
    options = {
        "title": {"text": "折线图堆叠"},
        "tooltip": {"trigger": "axis"},
        "legend": {"data": ["邮件营销", "联盟广告", "视频广告", "直接访问", "搜索引擎"]},
        "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
        "toolbox": {"feature": {"saveAsImage": {}}},
        "xAxis": {
            "type": "category",
            "boundaryGap": False,
            "data": ["周一", "周二", "周三", "周四", "周五", "周六", "周日"],
        },
        "yAxis": {"type": "value"},
        "series": [
            {
                "name": "邮件营销",
                "type": "line",
                "stack": "总量",
                "data": [120, 132, 101, 134, 90, 230, 210],
            },
            {
                "name": "联盟广告",
                "type": "line",
                "stack": "总量",
                "data": [220, 182, 191, 234, 290, 330, 310],
            },
            {
                "name": "视频广告",
                "type": "line",
                "stack": "总量",
                "data": [150, 232, 201, 154, 190, 330, 410],
            },
            {
                "name": "直接访问",
                "type": "line",
                "stack": "总量",
                "data": [320, 332, 301, 334, 390, 330, 320],
            },
            {
                "name": "搜索引擎",
                "type": "line",
                "stack": "总量",
                "data": [820, 932, 901, 934, 1290, 1330, 1320],
            },
        ],
    }
    st_echarts(options=options, height="400px")


def render_stacked_area_chart():
    options = {
        "title": {"text": "堆叠区域图"},
        "tooltip": {
            "trigger": "axis",
            "axisPointer": {"type": "cross", "label": {"backgroundColor": "#6a7985"}},
        },
        "legend": {"data": ["邮件营销", "联盟广告", "视频广告", "直接访问", "搜索引擎"]},
        "toolbox": {"feature": {"saveAsImage": {}}},
        "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
        "xAxis": [
            {
                "type": "category",
                "boundaryGap": False,
                "data": ["周一", "周二", "周三", "周四", "周五", "周六", "周日"],
            }
        ],
        "yAxis": [{"type": "value"}],
        "series": [
            {
                "name": "邮件营销",
                "type": "line",
                "stack": "总量",
                "areaStyle": {},
                "emphasis": {"focus": "series"},
                "data": [120, 132, 101, 134, 90, 230, 210],
            },
            {
                "name": "联盟广告",
                "type": "line",
                "stack": "总量",
                "areaStyle": {},
                "emphasis": {"focus": "series"},
                "data": [220, 182, 191, 234, 290, 330, 310],
            },
            {
                "name": "视频广告",
                "type": "line",
                "stack": "总量",
                "areaStyle": {},
                "emphasis": {"focus": "series"},
                "data": [150, 232, 201, 154, 190, 330, 410],
            },
            {
                "name": "直接访问",
                "type": "line",
                "stack": "总量",
                "areaStyle": {},
                "emphasis": {"focus": "series"},
                "data": [320, 332, 301, 334, 390, 330, 320],
            },
            {
                "name": "搜索引擎",
                "type": "line",
                "stack": "总量",
                "label": {"show": True, "position": "top"},
                "areaStyle": {},
                "emphasis": {"focus": "series"},
                "data": [820, 932, 901, 934, 1290, 1330, 1320],
            },
        ],
    }
    st_echarts(options=options, height="400px")


def render_line_race():
    with open("./data/life-expectancy-table.json") as f:
        raw_data = json.load(f)
    countries = [
        "Finland",
        "France",
        "Germany",
        "Iceland",
        "Norway",
        "Poland",
        "Russia",
        "United Kingdom",
    ]

    datasetWithFilters = [
        {
            "id": f"dataset_{country}",
            "fromDatasetId": "dataset_raw",
            "transform": {
                "type": "filter",
                "config": {
                    "and": [
                        {"dimension": "Year", "gte": 1950},
                        {"dimension": "Country", "=": country},
                    ]
                },
            },
        }
        for country in countries
    ]

    seriesList = [
        {
            "type": "line",
            "datasetId": f"dataset_{country}",
            "showSymbol": False,
            "name": country,
            "endLabel": {
                "show": True,
                "formatter": JsCode(
                    "function (params) { return params.value[3] + ': ' + params.value[0];}"
                ).js_code,
            },
            "labelLayout": {"moveOverlap": "shiftY"},
            "emphasis": {"focus": "series"},
            "encode": {
                "x": "Year",
                "y": "Income",
                "label": ["Country", "Income"],
                "itemName": "Year",
                "tooltip": ["Income"],
            },
        }
        for country in countries
    ]

    option = {
        "animationDuration": 10000,
        "dataset": [{"id": "dataset_raw", "source": raw_data}] + datasetWithFilters,
        "title": {"text": "Income in Europe since 1950"},
        "tooltip": {"order": "valueDesc", "trigger": "axis"},
        "xAxis": {"type": "category", "nameLocation": "middle"},
        "yAxis": {"name": "Income"},
        "grid": {"right": 140},
        "series": seriesList,
    }
    st_echarts(options=option, height="600px")


ST_LINE_DEMOS = {
    "Line: Basic Line Chart": (
        render_basic_line_chart,
        "https://echarts.apache.org/examples/en/editor.html?c=line-simple",
    ),
    "Line: Basic Area Chart": (
        render_basic_area_chart,
        "https://echarts.apache.org/examples/en/editor.html?c=area-basic",
    ),
    "Line: Stacked Line Chart": (
        render_stacked_line_chart,
        "https://echarts.apache.org/examples/en/editor.html?c=line-stack",
    ),
    "Line: Stacked Area Chart": (
        render_stacked_area_chart,
        "https://echarts.apache.org/examples/en/editor.html?c=area-stack",
    ),
    "Line: Line Race": (
        render_line_race,
        "https://echarts.apache.org/examples/en/editor.html?c=line-race",
    ),
}

import json
import random
import datetime
import math
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


def render_smoothed_line_chart():
    options = {
        "xAxis": {
            "type": "category",
            "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        },
        "yAxis": {"type": "value"},
        "series": [
            {"data": [820, 932, 901, 934, 1290, 1330, 1320], "type": "line", "smooth": True}
        ],
    }
    st_echarts(options=options, height="400px")


def render_bump_chart():
    names = [
        "Orange",
        "Tomato",
        "Apple",
        "Sakana",
        "Banana",
        "Iwashi",
        "Snappy Fish",
        "Lemon",
        "Pasta",
    ]
    years = ["2001", "2002", "2003", "2004", "2005", "2006"]

    def generate_ranking_data():
        ranking_map = {name: [] for name in names}
        default_ranking = list(range(1, len(names) + 1))
        for _ in years:
            shuffled_ranking = default_ranking.copy()
            random.shuffle(shuffled_ranking)
            for i, name in enumerate(names):
                ranking_map[name].append(shuffled_ranking[i])
        return ranking_map

    ranking_map = generate_ranking_data()
    series_list = []
    for name, data in ranking_map.items():
        series = {
            "name": name,
            "symbolSize": 20,
            "type": "line",
            "smooth": True,
            "emphasis": {"focus": "series"},
            "endLabel": {"show": True, "formatter": "{a}", "distance": 20},
            "lineStyle": {"width": 4},
            "data": data,
        }
        series_list.append(series)

    options = {
        "title": {"text": "Bump Chart (Ranking)"},
        "tooltip": {"trigger": "item"},
        "grid": {"left": 30, "right": 110, "bottom": 30, "containLabel": True},
        "toolbox": {"feature": {"saveAsImage": {}}},
        "xAxis": {
            "type": "category",
            "splitLine": {"show": True},
            "axisLabel": {"margin": 30, "fontSize": 16},
            "boundaryGap": False,
            "data": years,
        },
        "yAxis": {
            "type": "value",
            "axisLabel": {"margin": 30, "fontSize": 16, "formatter": "#{value}"},
            "inverse": True,
            "interval": 1,
            "min": 1,
            "max": len(names),
        },
        "series": series_list,
    }
    st_echarts(options=options, height="600px")


def render_intraday_chart_with_breaks():
    def generate_data():
        series_data = []
        start_time = datetime.datetime(2024, 4, 9, 9, 30, tzinfo=datetime.timezone.utc)
        end_time = datetime.datetime(2024, 4, 9, 15, 0, tzinfo=datetime.timezone.utc)
        break_start = datetime.datetime(2024, 4, 9, 11, 30, tzinfo=datetime.timezone.utc)
        break_end = datetime.datetime(2024, 4, 9, 13, 0, tzinfo=datetime.timezone.utc)

        current_time = start_time
        val = 1669.0

        while current_time <= end_time:
            if current_time <= break_start or current_time >= break_end:
                change = (
                    math.floor(
                        (random.random() - 0.5 * math.sin(val / 1000)) * 20 * 100
                    )
                    / 100.0
                )
                val += change
                val = round(val, 2)
                series_data.append([int(current_time.timestamp() * 1000), val])

            current_time += datetime.timedelta(minutes=1)

        return {
            "seriesData": series_data,
            "breakStart": int(break_start.timestamp() * 1000),
            "breakEnd": int(break_end.timestamp() * 1000),
        }

    data = generate_data()

    options = {
        "useUTC": True,
        "title": {
            "text": "Intraday Chart with Breaks (Single Day)",
            "left": "center",
        },
        "tooltip": {"show": True, "trigger": "axis"},
        "xAxis": [
            {
                "type": "time",
                "interval": 1000 * 60 * 30,
                "axisLabel": {
                    "showMinLabel": True,
                    "showMaxLabel": True,
                    "formatter": JsCode(
                        """
          (value, index, extra) => {
            if (!extra || !extra.break) {
              return echarts.time.format(value, '{HH}:{mm}', true);
            }
            if (extra.break.type === 'start') {
              return (
                echarts.time.format(extra.break.start, '{HH}:{mm}', true) +
                '/' +
                echarts.time.format(extra.break.end, '{HH}:{mm}', true)
              );
            }
            return '';
          }
        """
                    ).js_code,
                },
                "breakLabelLayout": {"moveOverlap": False},
                "breaks": [{"start": data["breakStart"], "end": data["breakEnd"], "gap": 0}],
                "breakArea": {
                    "expandOnClick": False,
                    "zigzagAmplitude": 0,
                    "zigzagZ": 200,
                },
            }
        ],
        "yAxis": {"type": "value", "min": "dataMin"},
        "dataZoom": [{"type": "inside", "xAxisIndex": 0}, {"type": "slider", "xAxisIndex": 0}],
        "series": [{"type": "line", "symbolSize": 0, "data": data["seriesData"]}],
    }
    st_echarts(options=options, height="600px")


ST_LINE_DEMOS = {
    "Line: Basic Line Chart": (
        render_basic_line_chart,
        "https://echarts.apache.org/examples/en/editor.html?c=line-simple",
    ),
    "Line: Smoothed Line Chart": (
        render_smoothed_line_chart,
        "https://echarts.apache.org/examples/en/editor.html?c=line-smooth",
    ),
    "Line: Bump Chart (Ranking)": (
        render_bump_chart,
        "https://echarts.apache.org/examples/en/editor.html?c=bump-chart",
    ),
    "Line: Intraday Chart with Breaks (Single Day)": (
        render_intraday_chart_with_breaks,
        "https://echarts.apache.org/examples/en/editor.html?c=intraday-breaks-2",
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

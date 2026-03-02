from random import randint

import pandas as pd
from streamlit_echarts import st_echarts


def render_calendar_horizontal():
    def get_virtual_data(year):
        date_list = pd.date_range(
            start=f"{year}-01-01", end=f"{year + 1}-01-01", freq="D"
        )
        return [[d.strftime("%Y-%m-%d"), randint(1, 10000)] for d in date_list]

    option = {
        "tooltip": {"position": "top"},
        "visualMap": {
            "min": 0,
            "max": 10000,
            "calculable": True,
            "orient": "horizontal",
            "left": "center",
            "top": "top",
        },
        "calendar": [
            {"range": "2020", "cellSize": ["auto", 20]},
            {"top": 260, "range": "2019", "cellSize": ["auto", 20]},
            {"top": 450, "range": "2018", "cellSize": ["auto", 20], "right": 5},
        ],
        "series": [
            {
                "type": "heatmap",
                "coordinateSystem": "calendar",
                "calendarIndex": 0,
                "data": get_virtual_data(2020),
            },
            {
                "type": "heatmap",
                "coordinateSystem": "calendar",
                "calendarIndex": 1,
                "data": get_virtual_data(2019),
            },
            {
                "type": "heatmap",
                "coordinateSystem": "calendar",
                "calendarIndex": 2,
                "data": get_virtual_data(2018),
            },
        ],
    }
    st_echarts(option, height="640px", key="echarts")


def render_calendar_pie():
    cell_size = [80, 80]
    pie_radius = 30

    def get_virtual_data():
        date_list = pd.date_range(start="2017-02-01", end="2017-03-01", freq="D")
        return [[d.strftime("%Y-%m-%d"), randint(1, 10000)] for d in date_list]

    scatter_data = get_virtual_data()
    pie_series = [
        {
            "type": "pie",
            "id": f"pie-{idx}",
            "center": item[0],
            "radius": pie_radius,
            "coordinateSystem": "calendar",
            "label": {"formatter": "{c}", "position": "inside"},
            "data": [
                {"name": "Work", "value": randint(1, 24)},
                {"name": "Entertainment", "value": randint(1, 24)},
                {"name": "Sleep", "value": randint(1, 24)},
            ],
        }
        for idx, item in enumerate(scatter_data)
    ]

    option = {
        "tooltip": {},
        "legend": {"data": ["Work", "Entertainment", "Sleep"], "bottom": 20},
        "calendar": {
            "top": "middle",
            "left": "center",
            "orient": "vertical",
            "cellSize": cell_size,
            "yearLabel": {"show": False, "fontSize": 30},
            "dayLabel": {
                "margin": 20,
                "firstDay": 1,
                "nameMap": ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            },
            "monthLabel": {"show": False},
            "range": ["2017-02"],
        },
        "series": [
            {
                "id": "label",
                "type": "scatter",
                "coordinateSystem": "calendar",
                "symbolSize": 0,
                "label": {
                    "show": True,
                    "formatter": "{@[0]}",
                    "offset": [-cell_size[0] / 2 + 10, -cell_size[1] / 2 + 10],
                    "fontSize": 14,
                },
                "data": scatter_data,
            },
            *pie_series,
        ],
    }
    st_echarts(option, height="800px")


ST_CALENDAR_DEMOS = {
    "Horizontal calendars": (
        render_calendar_horizontal,
        "https://echarts.apache.org/examples/en/editor.html?c=calendar-horizontal",
    ),
    "Calendar Pie": (
        render_calendar_pie,
        "https://echarts.apache.org/examples/en/editor.html?c=calendar-pie",
    ),
}

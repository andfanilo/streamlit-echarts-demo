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


ST_CALENDAR_DEMOS = {
    "Calendar: Horizontal calendars": (
        render_calendar_horizontal,
        "https://echarts.apache.org/examples/en/editor.html?c=calendar-horizontal",
    ),
}

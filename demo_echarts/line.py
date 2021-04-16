import json
import streamlit as st
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

from streamlit_echarts import st_echarts


def render_dataset():
    option = {
        "legend": {},
        "tooltip": {"trigger": "axis", "showContent": False},
        "dataset": {
            "source": [
                ["product", "2012", "2013", "2014", "2015", "2016", "2017"],
                ["Milk Tea", 56.5, 82.1, 88.7, 70.1, 53.4, 85.1],
                ["Matcha Latte", 51.1, 51.4, 55.1, 53.3, 73.8, 68.7],
                ["Cheese Cocoa", 40.1, 62.2, 69.5, 36.4, 45.2, 32.5],
                ["Walnut Brownie", 25.2, 37.1, 41.2, 18, 33.9, 49.1],
            ]
        },
        "xAxis": {"type": "category"},
        "yAxis": {"gridIndex": 0},
        "grid": {"top": "55%"},
        "series": [
            {
                "type": "line",
                "smooth": True,
                "seriesLayoutBy": "row",
                "emphasis": {"focus": "series"},
            },
            {
                "type": "line",
                "smooth": True,
                "seriesLayoutBy": "row",
                "emphasis": {"focus": "series"},
            },
            {
                "type": "line",
                "smooth": True,
                "seriesLayoutBy": "row",
                "emphasis": {"focus": "series"},
            },
            {
                "type": "line",
                "smooth": True,
                "seriesLayoutBy": "row",
                "emphasis": {"focus": "series"},
            },
            {
                "type": "pie",
                "id": "pie",
                "radius": "30%",
                "center": ["50%", "25%"],
                "emphasis": {"focus": "data"},
                "label": {"formatter": "{b}: {@2012} ({d}%)"},
                "encode": {"itemName": "product", "value": "2012", "tooltip": "2012"},
            },
        ],
    }
    st_echarts(option, height="500px", key="echarts")


def render_dataset_sort_bar():
    options = {
        "dataset": [
            {
                "dimensions": ["name", "age", "profession", "score", "date"],
                "source": [
                    ["Hannah Krause", 41, "Engineer", 314, "2011-02-12"],
                    ["Zhao Qian", 20, "Teacher", 351, "2011-03-01"],
                    ["Jasmin Krause ", 52, "Musician", 287, "2011-02-14"],
                    ["Li Lei", 37, "Teacher", 219, "2011-02-18"],
                    ["Karle Neumann", 25, "Engineer", 253, "2011-04-02"],
                    ["Adrian Groß", 19, "Teacher", "-", "2011-01-16"],
                    ["Mia Neumann", 71, "Engineer", 165, "2011-03-19"],
                    ["Böhm Fuchs", 36, "Musician", 318, "2011-02-24"],
                    ["Han Meimei", 67, "Engineer", 366, "2011-03-12"],
                ],
            },
            {
                "transform": {
                    "type": "sort",
                    "config": {"dimension": "score", "order": "desc"},
                }
            },
        ],
        "xAxis": {"type": "category", "axisLabel": {"interval": 0, "rotate": 30}},
        "yAxis": {},
        "series": {
            "type": "bar",
            "encode": {"x": "name", "y": "score"},
            "datasetIndex": 1,
        },
    }
    st_echarts(options=options, height="500px")


def render_dataset_encode0():
    options = {
        "dataset": {
            "source": [
                ["score", "amount", "product"],
                [89.3, 58212, "Matcha Latte"],
                [57.1, 78254, "Milk Tea"],
                [74.4, 41032, "Cheese Cocoa"],
                [50.1, 12755, "Cheese Brownie"],
                [89.7, 20145, "Matcha Cocoa"],
                [68.1, 79146, "Tea"],
                [19.6, 91852, "Orange Juice"],
                [10.6, 101852, "Lemon Juice"],
                [32.7, 20112, "Walnut Brownie"],
            ]
        },
        "grid": {"containLabel": True},
        "xAxis": {"name": "amount"},
        "yAxis": {"type": "category"},
        "visualMap": {
            "orient": "horizontal",
            "left": "center",
            "min": 10,
            "max": 100,
            "text": ["High Score", "Low Score"],
            "dimension": 0,
            "inRange": {"color": ["#65B581", "#FFCE34", "#FD665F"]},
        },
        "series": [{"type": "bar", "encode": {"x": "amount", "y": "product"}}],
    }
    st_echarts(options=options, height="500px")


def render_dataset_default():
    options = {
        "legend": {},
        "tooltip": {},
        "dataset": {
            "source": [
                ["product", "2012", "2013", "2014", "2015", "2016", "2017"],
                ["Milk Tea", 86.5, 92.1, 85.7, 83.1, 73.4, 55.1],
                ["Matcha Latte", 41.1, 30.4, 65.1, 53.3, 83.8, 98.7],
                ["Cheese Cocoa", 24.1, 67.2, 79.5, 86.4, 65.2, 82.5],
                ["Walnut Brownie", 55.2, 67.1, 69.2, 72.4, 53.9, 39.1],
            ]
        },
        "series": [
            {
                "type": "pie",
                "radius": "20%",
                "center": ["25%", "30%"],
                # No encode specified, by default, it is '2012'.
            },
            {
                "type": "pie",
                "radius": "20%",
                "center": ["75%", "30%"],
                "encode": {"itemName": "product", "value": "2013"},
            },
            {
                "type": "pie",
                "radius": "20%",
                "center": ["25%", "75%"],
                "encode": {"itemName": "product", "value": "2014"},
            },
            {
                "type": "pie",
                "radius": "20%",
                "center": ["75%", "75%"],
                "encode": {"itemName": "product", "value": "2015"},
            },
        ],
    }
    st_echarts(options=options, height="500px")


ST_DATASET_DEMOS = {
    "Sort Data in Bar Chart": (
        render_dataset_sort_bar,
        "https://echarts.apache.org/examples/en/editor.html?c=data-transform-sort-bar",
    ),
    "Simple Encode": (
        render_dataset_encode0,
        "https://echarts.apache.org/examples/en/editor.html?c=dataset-encode0",
    ),
    "Default arrangement": (
        render_dataset_default,
        "https://echarts.apache.org/examples/en/editor.html?c=dataset-default",
    ),
    "Share Dataset": (
        render_dataset,
        "https://echarts.apache.org/examples/en/editor.html?c=dataset-link",
    ),
}

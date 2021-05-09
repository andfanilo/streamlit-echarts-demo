import json

from streamlit_echarts import st_echarts


def render_drink_flavors():
    with open("./data/drink-flavors.json", "r") as f:
        data = json.loads(f.read())

    option = {
        "title": {
            "text": "WORLD COFFEE RESEARCH SENSORY LEXICON",
            "subtext": "Source: https://worldcoffeeresearch.org/work/sensory-lexicon/",
            "textStyle": {"fontSize": 14, "align": "center"},
            "subtextStyle": {"align": "center"},
            "sublink": "https://worldcoffeeresearch.org/work/sensory-lexicon/",
        },
        "series": {
            "type": "sunburst",
            "data": data,
            "radius": [0, "95%"],
            "sort": None,
            "emphasis": {"focus": "ancestor"},
            "levels": [
                {},
                {
                    "r0": "15%",
                    "r": "35%",
                    "itemStyle": {"borderWidth": 2},
                    "label": {"rotate": "tangential"},
                },
                {"r0": "35%", "r": "70%", "label": {"align": "right"}},
                {
                    "r0": "70%",
                    "r": "72%",
                    "label": {"position": "outside", "padding": 3, "silent": False},
                    "itemStyle": {"borderWidth": 3},
                },
            ],
        },
    }
    st_echarts(option, height="700px")


ST_SUNBURST_DEMOS = {
    "Sunburst: Drink flavors": (
        render_drink_flavors,
        "https://echarts.apache.org/examples/en/editor.html?c=sunburst-drink",
    ),
}

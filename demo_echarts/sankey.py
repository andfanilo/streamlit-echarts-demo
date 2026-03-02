import json
from streamlit_echarts import st_echarts


def render_sankey_simple():
    options = {
        "series": {
            "type": "sankey",
            "layout": "none",
            "emphasis": {"focus": "adjacency"},
            "data": [
                {"name": "a"},
                {"name": "b"},
                {"name": "a1"},
                {"name": "a2"},
                {"name": "b1"},
                {"name": "c"},
            ],
            "links": [
                {"source": "a", "target": "a1", "value": 5},
                {"source": "a", "target": "a2", "value": 3},
                {"source": "b", "target": "b1", "value": 8},
                {"source": "a", "target": "b1", "value": 3},
                {"source": "b1", "target": "a1", "value": 1},
                {"source": "b1", "target": "c", "value": 2},
            ],
        },
    }
    st_echarts(options=options, height="500px")


def render_sankey_level_settings():
    with open("./data/product.json", "r") as f:
        data = json.loads(f.read())

    option = {
        "title": {"text": "Sankey Diagram"},
        "tooltip": {"trigger": "item", "triggerOn": "mousemove"},
        "series": [
            {
                "type": "sankey",
                "data": data["nodes"],
                "links": data["links"],
                "emphasis": {"focus": "adjacency"},
                "levels": [
                    {
                        "depth": 0,
                        "itemStyle": {"color": "#fbb4ae"},
                        "lineStyle": {"color": "source", "opacity": 0.6},
                    },
                    {
                        "depth": 1,
                        "itemStyle": {"color": "#b3cde3"},
                        "lineStyle": {"color": "source", "opacity": 0.6},
                    },
                    {
                        "depth": 2,
                        "itemStyle": {"color": "#ccebc5"},
                        "lineStyle": {"color": "source", "opacity": 0.6},
                    },
                    {
                        "depth": 3,
                        "itemStyle": {"color": "#decbe4"},
                        "lineStyle": {"color": "source", "opacity": 0.6},
                    },
                ],
                "lineStyle": {"curveness": 0.5},
            }
        ],
    }
    st_echarts(option, height="500px")


ST_SANKEY_DEMOS = {
    "Basic Sankey": (
        render_sankey_simple,
        "https://echarts.apache.org/examples/en/editor.html?c=sankey-simple",
    ),
    "Sankey with Level Settings": (
        render_sankey_level_settings,
        "https://echarts.apache.org/examples/en/editor.html?c=sankey-levels",
    ),
}

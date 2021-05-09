import json
from streamlit_echarts import st_echarts


def render_simple_graph():
    option = {
        "title": {"text": "Graph 简单示例"},
        "tooltip": {},
        "animationDurationUpdate": 1500,
        "animationEasingUpdate": "quinticInOut",
        "series": [
            {
                "type": "graph",
                "layout": "none",
                "symbolSize": 50,
                "roam": True,
                "label": {"show": True},
                "edgeSymbol": ["circle", "arrow"],
                "edgeSymbolSize": [4, 10],
                "edgeLabel": {"fontSize": 20},
                "data": [
                    {"name": "节点1", "x": 300, "y": 300},
                    {"name": "节点2", "x": 800, "y": 300},
                    {"name": "节点3", "x": 550, "y": 100},
                    {"name": "节点4", "x": 550, "y": 500},
                ],
                "links": [
                    {
                        "source": 0,
                        "target": 1,
                        "symbolSize": [5, 20],
                        "label": {"show": True},
                        "lineStyle": {"width": 5, "curveness": 0.2},
                    },
                    {
                        "source": "节点2",
                        "target": "节点1",
                        "label": {"show": True},
                        "lineStyle": {"curveness": 0.2},
                    },
                    {"source": "节点1", "target": "节点3"},
                    {"source": "节点2", "target": "节点3"},
                    {"source": "节点2", "target": "节点4"},
                    {"source": "节点1", "target": "节点4"},
                ],
                "lineStyle": {"opacity": 0.9, "width": 2, "curveness": 0},
            }
        ],
    }
    st_echarts(option, height="500px")


def render_force_layout():
    with open("./data/les-miserables.json", "r") as f:
        graph = json.loads(f.read())

    for idx, _ in enumerate(graph["nodes"]):
        graph["nodes"][idx]["symbolSize"] = 5

    option = {
        "title": {
            "text": "Les Miserables",
            "subtext": "Default layout",
            "top": "bottom",
            "left": "right",
        },
        "tooltip": {},
        "legend": [{"data": [a["name"] for a in graph["categories"]]}],
        "series": [
            {
                "name": "Les Miserables",
                "type": "graph",
                "layout": "force",
                "data": graph["nodes"],
                "links": graph["links"],
                "categories": graph["categories"],
                "roam": True,
                "label": {"position": "right"},
                "draggable": True,
                "force": {"repulsion": 100},
            }
        ],
    }
    st_echarts(option, height="500px")


def render_les_miserables():
    with open("./data/les-miserables.json", "r") as f:
        graph = json.loads(f.read())

    for idx, node in enumerate(graph["nodes"]):
        graph["nodes"][idx]["label"] = {"show": node["symbolSize"] > 30}

    option = {
        "title": {
            "text": "Les Miserables",
            "subtext": "Default layout",
            "top": "bottom",
            "left": "right",
        },
        "tooltip": {},
        "legend": [{"data": [a["name"] for a in graph["categories"]]}],
        "animationDuration": 1500,
        "animationEasingUpdate": "quinticInOut",
        "series": [
            {
                "name": "Les Miserables",
                "type": "graph",
                "layout": "none",
                "data": graph["nodes"],
                "links": graph["links"],
                "categories": graph["categories"],
                "roam": True,
                "label": {"position": "right", "formatter": "{b}"},
                "lineStyle": {"color": "source", "curveness": 0.3},
                "emphasis": {"focus": "adjacency", "lineStyle": {"width": 10}},
            }
        ],
    }
    st_echarts(option, height="500px")


ST_GRAPH_DEMOS = {
    "Graph: Simple Graph": (
        render_simple_graph,
        "https://echarts.apache.org/examples/en/editor.html?c=graph-simple",
    ),
    "Graph: Force Layout": (
        render_force_layout,
        "https://echarts.apache.org/examples/en/editor.html?c=graph-force",
    ),
    "Graph: Les Miserables": (
        render_les_miserables,
        "https://echarts.apache.org/examples/en/editor.html?c=graph",
    ),
}

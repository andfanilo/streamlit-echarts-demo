import json

from streamlit_echarts import st_echarts


def render_basic_tree():
    with open("./data/flare.json", "r") as f:
        data = json.loads(f.read())

    for idx, _ in enumerate(data["children"]):
        data["children"][idx]["collapsed"] = idx % 2 == 0

    option = {
        "tooltip": {"trigger": "item", "triggerOn": "mousemove"},
        "series": [
            {
                "type": "tree",
                "data": [data],
                "top": "1%",
                "left": "7%",
                "bottom": "1%",
                "right": "20%",
                "symbolSize": 7,
                "label": {
                    "position": "left",
                    "verticalAlign": "middle",
                    "align": "right",
                    "fontSize": 9,
                },
                "leaves": {
                    "label": {
                        "position": "right",
                        "verticalAlign": "middle",
                        "align": "left",
                    }
                },
                "emphasis": {"focus": "descendant"},
                "expandAndCollapse": True,
                "animationDuration": 550,
                "animationDurationUpdate": 750,
            }
        ],
    }
    st_echarts(option, height="500px")


ST_TREE_DEMOS = {
    "Tree: From Left to Right Tree": (
        render_basic_tree,
        "https://echarts.apache.org/examples/en/editor.html?c=tree-basic",
    ),
}

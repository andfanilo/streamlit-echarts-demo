import json

from streamlit_echarts import JsCode
from streamlit_echarts import st_echarts


def render_disk_usage():
    with open("./data/disk.tree.json", "r") as f:
        diskData = json.loads(f.read())

    option = {
        "title": {"text": "Disk Usage", "left": "center"},
        "tooltip": {
            "formatter": JsCode(
                "function(info){var value=info.value;var treePathInfo=info.treePathInfo;var treePath=[];for(var i=1;i<treePathInfo.length;i+=1){treePath.push(treePathInfo[i].name)}return['<div class=\"tooltip-title\">'+treePath.join('/')+'</div>','Disk Usage: '+ value +' KB'].join('')};"
            ).js_code,
        },
        "series": [
            {
                "name": "Disk Usage",
                "type": "treemap",
                "visibleMin": 300,
                "label": {"show": True, "formatter": "{b}"},
                "itemStyle": {"borderColor": "#fff"},
                "levels": [
                    {"itemStyle": {"borderWidth": 0, "gapWidth": 5}},
                    {"itemStyle": {"gapWidth": 1}},
                    {
                        "colorSaturation": [0.35, 0.5],
                        "itemStyle": {"gapWidth": 1, "borderColorSaturation": 0.6},
                    },
                ],
                "data": diskData,
            }
        ],
    }
    st_echarts(option, height="500px")


ST_TREEMAP_DEMOS = {
    "Treemap: Disk Usage": (
        render_disk_usage,
        "https://echarts.apache.org/examples/en/editor.html?c=treemap-disk",
    ),
}

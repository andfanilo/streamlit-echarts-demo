from streamlit_echarts import st_echarts


def render_custom_funnel():
    option = {
        "title": {"text": "漏斗图", "subtext": "纯属虚构"},
        "tooltip": {"trigger": "item", "formatter": "{a} <br/>{b} : {c}%"},
        "toolbox": {
            "feature": {
                "dataView": {"readOnly": False},
                "restore": {},
                "saveAsImage": {},
            }
        },
        "legend": {"data": ["展现", "点击", "访问", "咨询", "订单"]},
        "series": [
            {
                "name": "预期",
                "type": "funnel",
                "left": "10%",
                "width": "80%",
                "label": {"formatter": "{b}预期"},
                "labelLine": {"show": False},
                "itemStyle": {"opacity": 0.7},
                "emphasis": {
                    "label": {"position": "inside", "formatter": "{b}预期: {c}%"}
                },
                "data": [
                    {"value": 60, "name": "访问"},
                    {"value": 40, "name": "咨询"},
                    {"value": 20, "name": "订单"},
                    {"value": 80, "name": "点击"},
                    {"value": 100, "name": "展现"},
                ],
            },
            {
                "name": "实际",
                "type": "funnel",
                "left": "10%",
                "width": "80%",
                "maxSize": "80%",
                "label": {"position": "inside", "formatter": "{c}%", "color": "#fff"},
                "itemStyle": {"opacity": 0.5, "borderColor": "#fff", "borderWidth": 2},
                "emphasis": {
                    "label": {"position": "inside", "formatter": "{b}实际: {c}%"}
                },
                "data": [
                    {"value": 30, "name": "访问"},
                    {"value": 10, "name": "咨询"},
                    {"value": 5, "name": "订单"},
                    {"value": 50, "name": "点击"},
                    {"value": 80, "name": "展现"},
                ],
                "z": 100,
            },
        ],
    }
    st_echarts(option, height="500px")


ST_FUNNEL_DEMOS = {
    "Funnel: Customized funnel": (
        render_custom_funnel,
        "https://echarts.apache.org/examples/en/editor.html?c=funnel-customize",
    ),
}

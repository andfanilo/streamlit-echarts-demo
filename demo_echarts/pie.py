from streamlit_echarts import st_echarts


def render_pie_simple():
    options = {
        "title": {"text": "某站点用户访问来源", "subtext": "纯属虚构", "left": "center"},
        "tooltip": {"trigger": "item"},
        "legend": {"orient": "vertical", "left": "left",},
        "series": [
            {
                "name": "访问来源",
                "type": "pie",
                "radius": "50%",
                "data": [
                    {"value": 1048, "name": "搜索引擎"},
                    {"value": 735, "name": "直接访问"},
                    {"value": 580, "name": "邮件营销"},
                    {"value": 484, "name": "联盟广告"},
                    {"value": 300, "name": "视频广告"},
                ],
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 10,
                        "shadowOffsetX": 0,
                        "shadowColor": "rgba(0, 0, 0, 0.5)",
                    }
                },
            }
        ],
    }
    st_echarts(
        options=options, height="600px",
    )


def render_pie_donutradius():
    options = {
        "tooltip": {"trigger": "item"},
        "legend": {"top": "5%", "left": "center"},
        "series": [
            {
                "name": "访问来源",
                "type": "pie",
                "radius": ["40%", "70%"],
                "avoidLabelOverlap": False,
                "itemStyle": {
                    "borderRadius": 10,
                    "borderColor": "#fff",
                    "borderWidth": 2,
                },
                "label": {"show": False, "position": "center"},
                "emphasis": {
                    "label": {"show": True, "fontSize": "40", "fontWeight": "bold"}
                },
                "labelLine": {"show": False},
                "data": [
                    {"value": 1048, "name": "搜索引擎"},
                    {"value": 735, "name": "直接访问"},
                    {"value": 580, "name": "邮件营销"},
                    {"value": 484, "name": "联盟广告"},
                    {"value": 300, "name": "视频广告"},
                ],
            }
        ],
    }
    st_echarts(
        options=options, height="500px",
    )


def render_nightingale_rose_diagram():
    option = {
        "legend": {"top": "bottom"},
        "toolbox": {
            "show": True,
            "feature": {
                "mark": {"show": True},
                "dataView": {"show": True, "readOnly": False},
                "restore": {"show": True},
                "saveAsImage": {"show": True},
            },
        },
        "series": [
            {
                "name": "面积模式",
                "type": "pie",
                "radius": [50, 250],
                "center": ["50%", "50%"],
                "roseType": "area",
                "itemStyle": {"borderRadius": 8},
                "data": [
                    {"value": 40, "name": "rose 1"},
                    {"value": 38, "name": "rose 2"},
                    {"value": 32, "name": "rose 3"},
                    {"value": 30, "name": "rose 4"},
                    {"value": 28, "name": "rose 5"},
                    {"value": 26, "name": "rose 6"},
                    {"value": 22, "name": "rose 7"},
                    {"value": 18, "name": "rose 8"},
                ],
            }
        ],
    }
    st_echarts(
        options=option, height="600px",
    )


ST_PIE_DEMOS = {
    "Pie: Simple Pie": (
        render_pie_simple,
        "https://echarts.apache.org/examples/en/editor.html?c=pie-simple",
    ),
    "Pie: Doughnut Chart": (
        render_pie_donutradius,
        "https://echarts.apache.org/examples/en/editor.html?c=pie-borderRadius",
    ),
    "Pie: Nightingale Rose Diagram": (
        render_nightingale_rose_diagram,
        "https://echarts.apache.org/examples/en/editor.html?c=pie-roseType-simple",
    ),
}

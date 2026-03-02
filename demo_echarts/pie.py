from streamlit_echarts import st_echarts


def render_pie_simple():
    options = {
        "title": {
            "text": "Referer of a Website",
            "subtext": "Fake Data",
            "left": "center",
        },
        "tooltip": {"trigger": "item"},
        "legend": {"orient": "vertical", "left": "left"},
        "series": [
            {
                "name": "Access From",
                "type": "pie",
                "radius": "50%",
                "data": [
                    {"value": 1048, "name": "Search Engine"},
                    {"value": 735, "name": "Direct"},
                    {"value": 580, "name": "Email"},
                    {"value": 484, "name": "Union Ads"},
                    {"value": 300, "name": "Video Ads"},
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
    st_echarts(options=options, height="500px")


def render_pie_donutradius():
    options = {
        "tooltip": {"trigger": "item"},
        "legend": {"top": "5%", "left": "center"},
        "series": [
            {
                "name": "Access From",
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
                    "label": {"show": True, "fontSize": 40, "fontWeight": "bold"}
                },
                "labelLine": {"show": False},
                "data": [
                    {"value": 1048, "name": "Search Engine"},
                    {"value": 735, "name": "Direct"},
                    {"value": 580, "name": "Email"},
                    {"value": 484, "name": "Union Ads"},
                    {"value": 300, "name": "Video Ads"},
                ],
            }
        ],
    }
    st_echarts(options=options, height="500px")


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
                "name": "Nightingale Chart",
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
    st_echarts(options=option, height="500px")


def render_pie_half_doughnut():
    options = {
        "tooltip": {"trigger": "item"},
        "legend": {"top": "5%", "left": "center"},
        "series": [
            {
                "name": "Access From",
                "type": "pie",
                "radius": ["40%", "70%"],
                "center": ["50%", "70%"],
                "startAngle": 180,
                "endAngle": 360,
                "data": [
                    {"value": 1048, "name": "Search Engine"},
                    {"value": 735, "name": "Direct"},
                    {"value": 580, "name": "Email"},
                    {"value": 484, "name": "Union Ads"},
                    {"value": 300, "name": "Video Ads"},
                ],
            }
        ],
    }
    st_echarts(options=options, height="500px")


def render_pie_nest():
    options = {
        "tooltip": {"trigger": "item", "formatter": "{a} <br/>{b}: {c} ({d}%)"},
        "legend": {
            "data": [
                "Direct",
                "Marketing",
                "Search Engine",
                "Email",
                "Union Ads",
                "Video Ads",
                "Baidu",
                "Google",
                "Bing",
                "Others",
            ]
        },
        "series": [
            {
                "name": "Access From",
                "type": "pie",
                "selectedMode": "single",
                "radius": [0, "30%"],
                "label": {"position": "inner", "fontSize": 14},
                "labelLine": {"show": False},
                "data": [
                    {"value": 1548, "name": "Search Engine"},
                    {"value": 775, "name": "Direct"},
                    {"value": 679, "name": "Marketing", "selected": True},
                ],
            },
            {
                "name": "Access From",
                "type": "pie",
                "radius": ["45%", "60%"],
                "labelLine": {"length": 30},
                "label": {
                    "formatter": "{a|{a}}{abg|}\n{hr|}\n  {b|{b}：}{c}  {per|{d}%}  ",
                    "backgroundColor": "#F6F8FC",
                    "borderColor": "#8C8D8E",
                    "borderWidth": 1,
                    "borderRadius": 4,
                    "rich": {
                        "a": {"color": "#6E7079", "lineHeight": 22, "align": "center"},
                        "hr": {
                            "borderColor": "#8C8D8E",
                            "width": "100%",
                            "borderWidth": 1,
                            "height": 0,
                        },
                        "b": {
                            "color": "#4C5058",
                            "fontSize": 14,
                            "fontWeight": "bold",
                            "lineHeight": 33,
                        },
                        "per": {
                            "color": "#fff",
                            "backgroundColor": "#4C5058",
                            "padding": [3, 4],
                            "borderRadius": 4,
                        },
                    },
                },
                "data": [
                    {"value": 1048, "name": "Baidu"},
                    {"value": 335, "name": "Direct"},
                    {"value": 310, "name": "Email"},
                    {"value": 251, "name": "Google"},
                    {"value": 234, "name": "Union Ads"},
                    {"value": 147, "name": "Bing"},
                    {"value": 135, "name": "Video Ads"},
                    {"value": 102, "name": "Others"},
                ],
            },
        ],
    }
    st_echarts(options=options, height="500px")


def render_pie_pad_angle():
    options = {
        "tooltip": {"trigger": "item"},
        "legend": {"top": "5%", "left": "center"},
        "series": [
            {
                "name": "Access From",
                "type": "pie",
                "radius": ["40%", "70%"],
                "avoidLabelOverlap": False,
                "padAngle": 5,
                "itemStyle": {"borderRadius": 10},
                "label": {"show": False, "position": "center"},
                "emphasis": {
                    "label": {"show": True, "fontSize": 40, "fontWeight": "bold"}
                },
                "labelLine": {"show": False},
                "data": [
                    {"value": 1048, "name": "Search Engine"},
                    {"value": 735, "name": "Direct"},
                    {"value": 580, "name": "Email"},
                    {"value": 484, "name": "Union Ads"},
                    {"value": 300, "name": "Video Ads"},
                ],
            }
        ],
    }
    st_echarts(options=options, height="500px")


ST_PIE_DEMOS = {
    "Simple Pie": (
        render_pie_simple,
        "https://echarts.apache.org/examples/en/editor.html?c=pie-simple",
    ),
    "Doughnut Chart": (
        render_pie_donutradius,
        "https://echarts.apache.org/examples/en/editor.html?c=pie-borderRadius",
    ),
    "Half Doughnut Chart": (
        render_pie_half_doughnut,
        "https://echarts.apache.org/examples/en/editor.html?c=pie-half-donut",
    ),
    "Nightingale Rose Diagram": (
        render_nightingale_rose_diagram,
        "https://echarts.apache.org/examples/en/editor.html?c=pie-roseType-simple",
    ),
    "Nested Pies": (
        render_pie_nest,
        "https://echarts.apache.org/examples/en/editor.html?c=pie-nest",
    ),
    "Pie with padAngle": (
        render_pie_pad_angle,
        "https://echarts.apache.org/examples/en/editor.html?c=pie-padAngle",
    ),
}

from random import random

from streamlit_echarts import JsCode
from streamlit_echarts import st_echarts


def render_matrix_simple():
    options = {
        "matrix": {
            "x": {
                "data": [
                    {
                        "value": "A",
                        "children": [
                            "A1",
                            "A2",
                            {"value": "A3", "children": ["A31", "A32"]},
                        ],
                    }
                ]
            },
            "y": {"data": ["U", "V"]},
            "top": 150,
            "bottom": 150,
        },
        "visualMap": {
            "type": "continuous",
            "min": 0,
            "max": 80,
            "top": "middle",
            "dimension": 2,
            "calculable": True,
        },
        "series": {
            "type": "heatmap",
            "coordinateSystem": "matrix",
            "data": [
                ["A1", "U", 10],
                ["A1", "V", 20],
                ["A2", "U", 30],
                ["A2", "V", 40],
                ["A31", "U", 50],
                ["A3", "V", 60],
            ],
            "label": {"show": True},
        },
    }
    st_echarts(options=options, height="600px")


def render_matrix_correlation_scatter():
    x_cnt = 10
    y_cnt = 6
    x_data = [{"value": f"X{i + 1}"} for i in range(x_cnt)]
    y_data = [{"value": f"Y{i + 1}"} for i in range(y_cnt)]

    data = []
    for i in range(1, x_cnt + 1):
        for j in range(1, y_cnt + 1):
            data.append([f"X{i}", f"Y{j}", random() * 2 - 1])

    options = {
        "matrix": {"x": {"data": x_data}, "y": {"data": y_data}, "top": 80},
        "visualMap": {
            "type": "continuous",
            "min": -1,
            "max": 1,
            "dimension": 2,
            "calculable": True,
            "orient": "horizontal",
            "top": 5,
            "left": "center",
            "inRange": {
                "color": [
                    "#313695",
                    "#4575b4",
                    "#74add1",
                    "#abd9e9",
                    "#e0f3f8",
                    "#ffffbf",
                    "#fee090",
                    "#fdae61",
                    "#f46d43",
                    "#d73027",
                    "#a50026",
                ],
                "symbolSize": [15, 40],
            },
        },
        "series": {
            "type": "scatter",
            "coordinateSystem": "matrix",
            "data": data,
            "itemStyle": {"opacity": 1},
            "label": {
                "show": True,
                "formatter": JsCode(
                    "function(params) { return params.value[2].toFixed(2); }"
                ).js_code,
            },
        },
    }
    st_echarts(options=options, height="600px")


def render_matrix_grid_layout():
    import datetime

    def generate_single_series_data(day_count, inverse_xy):
        day_start = datetime.datetime(2025, 5, 5)
        series_data = []
        last_val = round(random() * 300)
        turn_count = None
        sign = -1
        for idx in range(day_count):
            if turn_count is None or idx >= turn_count:
                turn_count = idx + round((day_count / 4) * ((random() - 0.5) * 0.1))
                sign = -sign
            delta_mag = 50
            delta = round(random() * delta_mag - delta_mag / 2 + (sign * delta_mag) / 3)
            last_val = max(0, last_val + delta)
            x_time = day_start + datetime.timedelta(days=idx * 7)
            data_x_val = x_time.strftime("%Y-%m-%d")
            item = [data_x_val, last_val]
            if inverse_xy:
                item.reverse()
            series_data.append(item)
        return series_data

    media_definition_list = [
        {
            "query": {"maxWidth": 500},
            "matrix": {"x": {"data": [None]}, "y": {"data": [None] * 10}},
            "sectionCoordMap": {
                "section_title_1": [0, 0],
                "section_header_1": [0, [1, 2]],
                "section_sidebar_1": [0, [3, 4]],
                "section_main_content_area_1": [0, [5, 7]],
                "section_footer_1": [0, [8, 9]],
            },
        },
        {
            "matrix": {"x": {"data": [None] * 4}, "y": {"data": [None] * 10}},
            "sectionCoordMap": {
                "section_title_1": [[0, 3], 0],
                "section_header_1": [[0, 3], [1, 2]],
                "section_sidebar_1": [0, [3, 9]],
                "section_main_content_area_1": [[1, 3], [3, 7]],
                "section_footer_1": [[1, 3], [8, 9]],
            },
        },
    ]

    section_definition_map = {
        "section_title_1": {
            "option": {
                "title": [
                    {
                        "coordinateSystem": "matrix",
                        "text": "Resize the Canvas to Check the Responsiveness",
                        "left": "center",
                        "top": 10,
                    }
                ]
            }
        },
        "section_header_1": {
            "option": {
                "title": [
                    {
                        "coordinateSystem": "matrix",
                        "text": "Header Section",
                        "textStyle": {"fontSize": 14},
                        "left": "center",
                        "top": 5,
                    }
                ],
                "xAxis": {"type": "time", "id": "header_1", "gridId": "header_1"},
                "yAxis": {
                    "id": "header_1",
                    "gridId": "header_1",
                    "splitNumber": 2,
                    "splitLine": {"show": False},
                },
                "grid": {
                    "id": "header_1",
                    "coordinateSystem": "matrix",
                    "tooltip": {"trigger": "axis"},
                    "top": 30,
                    "bottom": 10,
                    "left": 10,
                    "right": 10,
                    "outerBounds": {"top": 30, "left": 20, "bottom": 20, "right": 20},
                },
                "series": {
                    "type": "line",
                    "id": "header_1",
                    "xAxisId": "header_1",
                    "yAxisId": "header_1",
                    "symbol": "none",
                    "data": generate_single_series_data(100, False),
                },
            }
        },
        "section_sidebar_1": {
            "option": {
                "title": {
                    "coordinateSystem": "matrix",
                    "text": "Sidebar Section",
                    "textStyle": {"fontSize": 14},
                    "left": "center",
                    "top": 15,
                },
                "xAxis": {
                    "id": "sidebar_1",
                    "gridId": "sidebar_1",
                    "splitLine": {"show": False},
                    "axisLabel": {"hideOverlap": True},
                },
                "yAxis": {
                    "type": "time",
                    "id": "sidebar_1",
                    "gridId": "sidebar_1",
                    "axisLabel": {"hideOverlap": True},
                },
                "grid": {
                    "id": "sidebar_1",
                    "coordinateSystem": "matrix",
                    "tooltip": {"trigger": "axis"},
                    "top": 50,
                    "bottom": 30,
                    "left": 40,
                    "right": 30,
                    "outerBounds": {"top": 30, "left": 20, "bottom": 20, "right": 20},
                },
                "series": {
                    "type": "bar",
                    "id": "sidebar_1",
                    "xAxisId": "sidebar_1",
                    "yAxisId": "sidebar_1",
                    "data": generate_single_series_data(10, True),
                },
            }
        },
        "section_main_content_area_1": {
            "option": {
                "title": {
                    "text": "Main Content Area",
                    "coordinateSystem": "matrix",
                    "textStyle": {"fontSize": 14},
                    "left": "center",
                    "top": 15,
                },
                "xAxis": {
                    "type": "time",
                    "id": "main_content_area_1",
                    "gridId": "main_content_area_1",
                },
                "yAxis": {"id": "main_content_area_1", "gridId": "main_content_area_1"},
                "grid": {
                    "id": "main_content_area_1",
                    "coordinateSystem": "matrix",
                    "tooltip": {"trigger": "axis"},
                    "top": 50,
                    "bottom": 10,
                    "left": 10,
                    "right": 10,
                    "outerBounds": {"top": 30, "left": 20, "bottom": 20, "right": 20},
                },
                "series": {
                    "type": "line",
                    "id": "main_content_area_1",
                    "xAxisId": "main_content_area_1",
                    "yAxisId": "main_content_area_1",
                    "symbol": "none",
                    "data": generate_single_series_data(100, False),
                },
            }
        },
        "section_footer_1": {
            "option": {
                "title": {
                    "coordinateSystem": "matrix",
                    "text": "Footer Section",
                    "textStyle": {"fontSize": 14},
                    "left": "center",
                    "top": 15,
                },
                "xAxis": {"type": "time", "id": "footer_1", "gridId": "footer_1"},
                "yAxis": {
                    "id": "footer_1",
                    "gridId": "footer_1",
                    "splitNumber": 2,
                    "splitLine": {"show": False},
                },
                "grid": {
                    "id": "footer_1",
                    "coordinateSystem": "matrix",
                    "tooltip": {"trigger": "axis"},
                    "top": 50,
                    "bottom": 10,
                    "left": 20,
                    "right": 20,
                    "outerBounds": {"top": 30, "left": 20, "bottom": 20, "right": 20},
                },
                "series": {
                    "type": "bar",
                    "id": "footer_1",
                    "xAxisId": "footer_1",
                    "yAxisId": "footer_1",
                    "data": generate_single_series_data(10, False),
                },
            }
        },
    }

    option = {
        "matrix": {
            "x": {"show": False, "data": []},
            "y": {"show": False, "data": []},
            "body": {"itemStyle": {"borderColor": "none"}},
            "backgroundStyle": {"borderColor": "none"},
            "top": 0,
            "bottom": 0,
            "left": 0,
            "right": 0,
        },
        "tooltip": {},
    }

    # Assemble
    option["media"] = [
        {"query": m["query"] if "query" in m else {}, "option": {"matrix": m["matrix"]}}
        for m in media_definition_list
    ]

    for section_id, definition in section_definition_map.items():
        option_id_map_will_set_coord = {}
        for component_main_type, content in definition["option"].items():
            if component_main_type not in option:
                option[component_main_type] = []
            elif not isinstance(option[component_main_type], list):
                option[component_main_type] = [option[component_main_type]]

            items = content if isinstance(content, list) else [content]
            for component in items:
                comp_id = component.get("id")
                if comp_id is None:
                    comp_id = f"{section_id}_{component_main_type}_{round(random() * 1000000)}"
                    component["id"] = comp_id
                option[component_main_type].append(component)

                if component.get("coordinateSystem") == "matrix":
                    if component_main_type not in option_id_map_will_set_coord:
                        option_id_map_will_set_coord[component_main_type] = []
                    option_id_map_will_set_coord[component_main_type].append(comp_id)

        for media_idx, media_def in enumerate(media_definition_list):
            option_in_media = option["media"][media_idx]["option"]
            coord = media_def["sectionCoordMap"].get(section_id)
            if coord:
                for comp_type, ids in option_id_map_will_set_coord.items():
                    if comp_type not in option_in_media:
                        option_in_media[comp_type] = []
                    for cid in ids:
                        option_in_media[comp_type].append({"id": cid, "coord": coord})

    st_echarts(options=option, height="800px")


def render_matrix_mbti():
    mbti_types = [
        "ENFJ",
        "ENFP",
        "ENTJ",
        "ENTP",
        "ESFJ",
        "ESFP",
        "ESTJ",
        "ESTP",
        "INFJ",
        "INFP",
        "INTJ",
        "INTP",
        "ISFJ",
        "ISFP",
        "ISTJ",
        "ISTP",
    ]

    colors = {
        "green": "#2D9A69",
        "purple": "#7D568F",
        "blue": "#3A8DAB",
        "yellow": "#E0A433",
        "greenLighter": "#10CA77",
        "purpleLighter": "#9253AF",
        "blueLighter": "#26A9D9",
        "yellowLighter": "#F4AC24",
        "greenDarker": "#0FB369",
        "purpleDarker": "#854AA0",
        "blueDarker": "#2298C3",
        "yellowDarker": "#F2A30D",
    }

    font_size = {"group": 16, "item": 11, "value": 12}

    def get_color(mbti_str, lightness=0):
        if "NF" in mbti_str:
            if lightness < 0:
                return colors["greenLighter"]
            if lightness > 0:
                return colors["greenDarker"]
            return colors["green"]
        if "NT" in mbti_str:
            if lightness < 0:
                return colors["purpleLighter"]
            if lightness > 0:
                return colors["purpleDarker"]
            return colors["purple"]
        if "S" in mbti_str and "J" in mbti_str:
            if lightness < 0:
                return colors["blueLighter"]
            if lightness > 0:
                return colors["blueDarker"]
            return colors["blue"]
        if "S" in mbti_str and "P" in mbti_str:
            if lightness < 0:
                return colors["yellowLighter"]
            if lightness > 0:
                return colors["yellowDarker"]
            return colors["yellow"]
        return "#000"

    def generate_group(group_name):
        color_map = {
            "NF": colors["green"],
            "NT": colors["purple"],
            "SJ": colors["blue"],
            "SP": colors["yellow"],
        }
        group_members = {
            "NF": ["INFJ", "INFP", "ENFJ", "ENFP"],
            "NT": ["INTJ", "INTP", "ENTJ", "ENTP"],
            "SJ": ["ISFJ", "ISTJ", "ESFJ", "ESTJ"],
            "SP": ["ISFP", "ISTP", "ESFP", "ESTP"],
        }
        return {
            "value": group_name,
            "label": {
                "color": color_map[group_name],
                "fontSize": font_size["group"],
                "fontWeight": "bolder",
                "padding": 0,
            },
            "children": [
                {
                    "value": m,
                    "label": {
                        "color": color_map[group_name],
                        "fontSize": font_size["item"],
                        "fontWeight": "bold",
                    },
                }
                for m in group_members[group_name]
            ],
        }

    x_data = [
        generate_group("NF"),
        generate_group("NT"),
        generate_group("SJ"),
        generate_group("SP"),
    ]
    y_data = [
        generate_group("NF"),
        generate_group("NT"),
        generate_group("SJ"),
        generate_group("SP"),
    ]

    original_data = [
        ["ENFJ", "ENFJ", 0.86],
        ["ENFJ", "ENFP", 0.91],
        ["ENFJ", "ENTJ", 0.42],
        ["ENFJ", "ENTP", 0.73],
        ["ENFJ", "ESFJ", 0.64],
        ["ENFJ", "ESFP", 0.8],
        ["ENFJ", "ESTJ", 0.22],
        ["ENFJ", "ESTP", 0.41],
        ["ENFJ", "INFJ", 0.74],
        ["ENFJ", "INFP", 0.73],
        ["ENFJ", "INTJ", 0.16],
        ["ENFJ", "INTP", 0.35],
        ["ENFJ", "ISFJ", 0.3],
        ["ENFJ", "ISFP", 0.4],
        ["ENFJ", "ISTJ", 0.18],
        ["ENFJ", "ISTP", 0.09],
        ["ENFP", "ENFJ", 0.91],
        ["ENFP", "ENFP", 0.97],
        ["ENFP", "ENTJ", 0.37],
        ["ENFP", "ENTP", 0.85],
        ["ENFP", "ESFJ", 0.42],
        ["ENFP", "ESFP", 0.93],
        ["ENFP", "ESTJ", 0.27],
        ["ENFP", "ESTP", 0.76],
        ["ENFP", "INFJ", 0.51],
        ["ENFP", "INFP", 0.73],
        ["ENFP", "INTJ", 0.13],
        ["ENFP", "INTP", 0.36],
        ["ENFP", "ISFJ", 0.11],
        ["ENFP", "ISFP", 0.49],
        ["ENFP", "ISTJ", 0.04],
        ["ENFP", "ISTP", 0.14],
        ["ENTJ", "ENFJ", 0.42],
        ["ENTJ", "ENFP", 0.37],
        ["ENTJ", "ENTJ", 0.91],
        ["ENTJ", "ENTP", 0.81],
        ["ENTJ", "ESFJ", 0.53],
        ["ENTJ", "ESFP", 0.51],
        ["ENTJ", "ESTJ", 0.87],
        ["ENTJ", "ESTP", 0.74],
        ["ENTJ", "INFJ", 0.25],
        ["ENTJ", "INFP", 0.13],
        ["ENTJ", "INTJ", 0.46],
        ["ENTJ", "INTP", 0.47],
        ["ENTJ", "ISFJ", 0.29],
        ["ENTJ", "ISFP", 0.06],
        ["ENTJ", "ISTJ", 0.66],
        ["ENTJ", "ISTP", 0.41],
        ["ENTP", "ENFJ", 0.73],
        ["ENTP", "ENFP", 0.64],
        ["ENTP", "ENTJ", 0.81],
        ["ENTP", "ENTP", 0.94],
        ["ENTP", "ESFJ", 0.32],
        ["ENTP", "ESFP", 0.87],
        ["ENTP", "ESTJ", 0.7],
        ["ENTP", "ESTP", 0.92],
        ["ENTP", "INFJ", 0.11],
        ["ENTP", "INFP", 0.35],
        ["ENTP", "INTJ", 0.22],
        ["ENTP", "INTP", 0.51],
        ["ENTP", "ISFJ", 0.05],
        ["ENTP", "ISFP", 0.14],
        ["ENTP", "ISTJ", 0.11],
        ["ENTP", "ISTP", 0.35],
        ["ESFJ", "ESFJ", 0.94],
        ["ESFJ", "ESFP", 0.4],
        ["ESFJ", "ESTJ", 0.77],
        ["ESFJ", "ESTP", 0.37],
        ["ESFJ", "INFJ", 0.74],
        ["ESFJ", "INFP", 0.17],
        ["ESFJ", "INTJ", 0.32],
        ["ESFJ", "INTP", 0.05],
        ["ESFJ", "ISFJ", 0.79],
        ["ESFJ", "ISFP", 0.57],
        ["ESFJ", "ISTJ", 0.71],
        ["ESFJ", "ISTP", 0.19],
        ["ESFP", "ESFP", 0.7],
        ["ESFP", "ESTJ", 0.39],
        ["ESFP", "ESTP", 0.75],
        ["ESFP", "INFJ", 0.43],
        ["ESFP", "INFP", 0.58],
        ["ESFP", "INTJ", 0.22],
        ["ESFP", "INTP", 0.39],
        ["ESFP", "ISFJ", 0.12],
        ["ESFP", "ISFP", 0.58],
        ["ESFP", "ISTJ", 0.08],
        ["ESFP", "ISTP", 0.26],
        ["ESTJ", "ESTJ", 0.96],
        ["ESTJ", "ESTP", 0.78],
        ["ESTJ", "INFJ", 0.14],
        ["ESTJ", "INFP", 0.03],
        ["ESTJ", "INTJ", 0.33],
        ["ESTJ", "INTP", 0.22],
        ["ESTJ", "ISFJ", 0.48],
        ["ESTJ", "ISFP", 0.22],
        ["ESTJ", "ISTJ", 0.79],
        ["ESTJ", "ISTP", 0.55],
        ["ESTP", "ESTP", 0.95],
        ["ESTP", "INFJ", 0.05],
        ["ESTP", "INFP", 0.24],
        ["ESTP", "INTJ", 0.17],
        ["ESTP", "INTP", 0.39],
        ["ESTP", "ISFJ", 0.12],
        ["ESTP", "ISFP", 0.43],
        ["ESTP", "ISTJ", 0.2],
        ["ESTP", "ISTP", 0.62],
        ["INFJ", "INFJ", 0.95],
        ["INFJ", "INFP", 0.85],
        ["INFJ", "INTJ", 0.65],
        ["INFJ", "INTP", 0.5],
        ["INFJ", "ISFJ", 0.85],
        ["INFJ", "ISFP", 0.58],
        ["INFJ", "ISTJ", 0.53],
        ["INFJ", "ISTP", 0.23],
        ["INFP", "INFP", 0.97],
        ["INFP", "INTJ", 0.7],
        ["INFP", "INTP", 0.84],
        ["INFP", "ISFJ", 0.46],
        ["INFP", "ISFP", 0.78],
        ["INFP", "ISTJ", 0.21],
        ["INFP", "ISTP", 0.49],
        ["INTJ", "INTJ", 0.86],
        ["INTJ", "INTP", 0.89],
        ["INTJ", "ISFJ", 0.79],
        ["INTJ", "ISFP", 0.45],
        ["INTJ", "ISTJ", 0.85],
        ["INTJ", "ISTP", 0.78],
        ["INTP", "INTP", 0.96],
        ["INTP", "ISFJ", 0.38],
        ["INTP", "ISFP", 0.43],
        ["INTP", "ISTJ", 0.51],
        ["INTP", "ISTP", 0.81],
        ["ISFJ", "ISFJ", 0.95],
        ["ISFJ", "ISFP", 0.76],
        ["ISFJ", "ISTJ", 0.93],
        ["ISFJ", "ISTP", 0.62],
        ["ISFP", "ISFP", 0.97],
        ["ISFP", "ISTJ", 0.47],
        ["ISFP", "ISTP", 0.76],
        ["ISTJ", "ISTJ", 0.96],
        ["ISTJ", "ISTP", 0.78],
        ["ISTP", "ISTP", 0.96],
    ]

    data_map = {f"{a}-{b}": v for a, b, v in original_data}

    heatmap_data = []
    scatter_data = []
    decal_size = 1

    for a in mbti_types:
        for b in mbti_types:
            key = f"{a}-{b}"
            alt_key = f"{b}-{a}"

            if key in data_map:
                val = data_map[key]
            elif alt_key in data_map:
                val = data_map[alt_key]
            else:
                val = 0

            value = [a, b, val]

            color_a = get_color(a, 1)
            color_b = get_color(b, 1)

            heatmap_data.append(
                {
                    "value": value,
                    "itemStyle": {
                        "decal": {
                            "shape": "circle",
                            "symbolSize": 1,
                            "color": color_a,
                            "backgroundColor": color_b,
                            "dashArrayX": [
                                [decal_size, decal_size],
                                [0, decal_size, decal_size, 0],
                            ],
                            "dashArrayY": [decal_size, 0],
                        },
                        "borderColor": get_color(b),
                        "borderWidth": 0,
                    },
                }
            )
            scatter_data.append(
                {
                    "value": value,
                    "label": {
                        "color": get_color(b) if val < 0.2 else "#fff",
                        "opacity": 0.6 if val < 0.15 else 1,
                    },
                }
            )

    font_family = "Ubuntu Condensed, sans-serif"

    detail_series = [
        {
            "id": "detail-heatmap",
            "type": "heatmap",
            "coordinateSystem": "matrix",
            "data": heatmap_data,
            "label": {"show": False},
            "emphasis": {"itemStyle": {"borderWidth": 5}},
        },
        {
            "id": "detail-scatter",
            "type": "scatter",
            "coordinateSystem": "matrix",
            "symbolSize": 0,
            "data": scatter_data,
            "color": "#fff",
            "label": {
                "show": True,
                "formatter": JsCode(
                    "function(params) { return Math.round(params.value[2] * 100) + '%'; }"
                ).js_code,
                "fontWeight": "bold",
                "color": "inherit",
            },
            "silent": True,
        },
    ]

    options = {
        "backgroundColor": "#F0F7F9",
        "textStyle": {"fontFamily": font_family},
        "title": {
            "text": "MBTI Partner Compatibility",
            "subtext": "Data from: https://www.personalitydata.org/16-types/enfj-relationships#partner-matrix",
            "sublink": "https://www.personalitydata.org/16-types/enfj-relationships#partner-matrix",
            "left": "center",
            "top": 5,
            "textStyle": {"fontSize": 20, "color": "#57576A"},
            "itemGap": 5,
        },
        "tooltip": {
            "formatter": JsCode(
                """
                function(params) {
                    const get_color = (mbti_str) => {
                        if (mbti_str.indexOf('NF') >= 0) return '#2D9A69';
                        if (mbti_str.indexOf('NT') >= 0) return '#7D568F';
                        if (mbti_str.indexOf('S') >= 0 && mbti_str.indexOf('J') >= 0) return '#3A8DAB';
                        if (mbti_str.indexOf('S') >= 0 && mbti_str.indexOf('P') >= 0) return '#E0A433';
                        return '#000';
                    };
                    return '<span style="color:' + get_color(params.value[1]) + ';font-weight:bold">' + params.value[1] + '</span> / ' +
                           '<span style="color:' + get_color(params.value[0]) + ';font-weight:bold">' + params.value[0] + '</span> : ' +
                           Math.round(params.value[2] * 100) + '%';
                }
                """
            ).js_code,
            "borderColor": "#eee",
            "padding": [2, 8],
        },
        "matrix": {
            "x": {
                "data": x_data,
                "itemStyle": {"borderColor": "transparent", "borderWidth": 0},
                "dividerLineStyle": {"width": 0},
                "label": {"fontFamily": font_family},
                "levels": [{"levelSize": 25}, {"levelSize": 30}],
            },
            "y": {
                "data": y_data,
                "itemStyle": {"borderColor": "transparent", "borderWidth": 0},
                "dividerLineStyle": {"width": 0},
                "label": {"fontFamily": font_family},
            },
            "body": {
                "itemStyle": {"borderWidth": 0},
                "label": {"fontFamily": font_family},
            },
            "top": 50,
            "backgroundStyle": {
                "color": "transparent",
                "borderColor": "transparent",
                "borderWidth": 0,
            },
        },
        "visualMap": [
            {
                "type": "continuous",
                "min": 0,
                "max": 1,
                "dimension": 2,
                "calculable": True,
                "orient": "horizontal",
                "top": 5,
                "left": "center",
                "inRange": {"opacity": [0, 1]},
                "seriesIndex": [0, 1],
                "show": False,
            }
        ],
        "series": detail_series,
        "aria": {"enabled": True, "decal": {"show": True}},
        "animation": False,
    }

    st_echarts(options=options, height="800px")


ST_MATRIX_DEMOS = {
    "Simple Matrix": (
        render_matrix_simple,
        "https://echarts.apache.org/examples/en/editor.html?c=matrix-simple",
    ),
    "Correlation Matrix (Scatter)": (
        render_matrix_correlation_scatter,
        "https://echarts.apache.org/examples/en/editor.html?c=matrix-correlation-scatter",
    ),
    "Matrix Grid Layout": (
        render_matrix_grid_layout,
        "https://echarts.apache.org/examples/en/editor.html?c=matrix-grid-layout",
    ),
    "MBTI Partner Compatibility": (
        render_matrix_mbti,
        "https://echarts.apache.org/examples/en/editor.html?c=matrix-mbti",
    ),
}

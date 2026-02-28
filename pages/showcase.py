import json
import streamlit as st
from streamlit_echarts import st_echarts, Map, JsCode

# Page configuration
st.set_page_config(page_title="ECharts Gallery", layout="wide")

# --- SIDEBAR ---
with st.sidebar:
    st.title("📊 Gallery Settings")
    period = st.selectbox("Data Period", ["Last 7 days", "Last 30 days", "Last 90 days", "Year to Date"])

# Default animation speed
anim_speed = 1000

# Data variation helper based on period
# We use multipliers and offsets to simulate data changes
period_map = {
    "Last 7 days": {"m": 0.5, "target": 0.15},
    "Last 30 days": {"m": 1.0, "target": 0.45},
    "Last 90 days": {"m": 2.5, "target": 0.72},
    "Year to Date": {"m": 5.0, "target": 0.88}
}
conf = period_map.get(period)
m = conf["m"]

# --- HEADER ---
st.title("🚀 ECharts Gallery")
st.markdown(
    "**streamlit-echarts** is the easiest way to display interactive ECharts components in your Streamlit apps. "
    "Create beautiful, high-performance, and deeply customizable visualizations with just a few lines of Python."
)

# Shared base options for animation
base_options = {
    "animationDuration": anim_speed,
    "animationDurationUpdate": anim_speed,
    "animationEasing": "cubicOut",
    "animationEasingUpdate": "cubicOut"
}

# ==========================================
# ROW 1: BUSINESS ESSENTIALS
# ==========================================
row1_1, row1_2, row1_3, row1_4 = st.columns(4)

with row1_1:
    options = {
        **base_options,
        "title": {"text": "Revenue Trend", "left": "center"},
        "toolbox": {
            "feature": {
                "dataZoom": {"yAxisIndex": "none"},
                "magicType": {"type": ["line", "bar"]},
                "restore": {},
                "saveAsImage": {}
            }
        },
        "tooltip": {"trigger": "axis"},
        "xAxis": {"type": "category", "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]},
        "yAxis": {"type": "value"},
        "series": [{"name": "Revenue", "data": [int(x * m) for x in [820, 932, 901, 934, 1290, 1330, 1320]], "type": "line", "areaStyle": {}, "smooth": True}],
        "grid": {"left": "10%", "right": "10%", "bottom": "15%", "top": "20%"}
    }
    st_echarts(options=options, height="400px", key="revenue_trend")

with row1_2:
    target_val = conf["target"] * 100
    options = {
        **base_options,
        "title": {"text": "Sales Target", "left": "center", "textStyle": {"fontSize": 16}},
        "toolbox": {
            "feature": {
                "restore": {},
                "saveAsImage": {}
            }
        },
        "series": [{
            "type": "pie",
            "radius": ["60%", "80%"],
            "silent": True,
            "label": {
                "show": True, 
                "position": "center", 
                "formatter": "{d}%", # Use native percentage formatter
                "fontSize": 24, 
                "fontWeight": "bold"
            },
            "data": [
                {"value": target_val, "name": "Achieved", "itemStyle": {"color": "#5470c6"}},
                {"value": 100 - target_val, "name": "Remaining", "itemStyle": {"color": "#eee"}}
            ]
        }]
    }
    st_echarts(options=options, height="400px", key="sales_target")

with row1_3:
    # Vary ratios so slices actually move
    ratios = {
        "Last 7 days": [40, 30, 20, 10],
        "Last 30 days": [35, 35, 20, 10],
        "Last 90 days": [30, 30, 25, 15],
        "Year to Date": [25, 25, 25, 25]
    }.get(period)
    options = {
        **base_options,
        "title": {"text": "Market Share", "left": "center"},
        "toolbox": {
            "feature": {
                "dataView": {"readOnly": False},
                "saveAsImage": {}
            }
        },
        "tooltip": {"trigger": "item"},
        "legend": {"bottom": "0", "left": "center", "textStyle": {"fontSize": 10}},
        "series": [{
            "type": "pie", 
            "radius": ["40%", "70%"], 
            "avoidLabelOverlap": False,
            "itemStyle": {"borderRadius": 10, "borderColor": "#fff", "borderWidth": 2},
            "label": {"show": False},
            "data": [
                {"value": ratios[0], "name": "Organic"}, 
                {"value": ratios[1], "name": "Retail"},
                {"value": ratios[2], "name": "Direct"},
                {"value": ratios[3], "name": "Partners"}
            ]
        }]
    }
    st_echarts(options=options, height="400px", key="market_share")

with row1_4:
    options = {
        **base_options,
        "title": {"text": "YoY Growth", "left": "center"},
        "toolbox": {
            "feature": {
                "magicType": {"type": ["stack", "tiled", "bar", "line"]},
                "dataView": {"readOnly": False},
                "restore": {},
                "saveAsImage": {}
            }
        },
        "legend": {"top": "30", "left": "center", "textStyle": {"fontSize": 10}},
        "tooltip": {"trigger": "axis"},
        "xAxis": {"type": "category", "data": ["2021", "2022", "2023", "2024"]},
        "yAxis": {"type": "value", "axisLabel": {"formatter": "{value}%"}},
        "series": [
            {
                "name": "Organic", 
                "data": [int(15*m/5+5), int(20*m/5+2), int(18*m/5+8), int(25*m/5)], 
                "type": "bar", "stack": "total", "itemStyle": {"color": "#5470c6"}
            },
            {
                "name": "Retail", 
                "data": [int(10*m/5+2), int(12*m/5+5), int(15*m/5+3), int(20*m/5+1)], 
                "type": "bar", "stack": "total", "itemStyle": {"color": "#91cc75"}
            },
            {
                "name": "Direct", 
                "data": [int(8*m/5+5), int(15*m/5+2), int(12*m/5+8), int(18*m/5)], 
                "type": "bar", "stack": "total", "itemStyle": {"color": "#fac858"}
            },
            {
                "name": "Partner", 
                "data": [int(5*m/5+2), int(8*m/5+5), int(10*m/5+3), int(12*m/5+1)], 
                "type": "bar", "stack": "total", "itemStyle": {"color": "#ee6666"}
            }
        ]
    }
    st_echarts(options=options, height="400px", key="yoy_growth")

# ==========================================
# ROW 2: REGIONAL & PERFORMANCE
# ==========================================
row2_1, row2_2 = st.columns([2, 1])

with row2_1:
    with open("./data/USA.json", "r") as f:
        usa_map_json = json.load(f)
        usa_map = Map("USA", usa_map_json, {"Alaska": {"left": -131, "top": 25, "width": 15}})
    
    # City coordinates for effectScatter
    geo_coord_map = {
        "New York": [-74.0060, 40.7128],
        "Chicago": [-87.6298, 41.8781],
        "San Francisco": [-122.4194, 37.7749],
        "Dallas": [-96.7970, 32.7767],
        "Miami": [-80.1918, 25.7617]
    }
    # Dynamic scatter data with colors changing based on m
    pulse_color = {
        "Last 7 days": "#7CFFB2", # Greenish
        "Last 30 days": "#FDDD60", # Yellowish
        "Last 90 days": "#FF6E76", # Reddish
        "Year to Date": "#fb7293"  # Pinkish
    }.get(period)
    
    scatter_data = [{"name": name, "value": coord + [100]} for name, coord in geo_coord_map.items()]

    map_options = {
        **base_options,
        "title": {"text": "Live Sales Pulse (USA)", "left": "center"},
        "tooltip": {"trigger": "item"},
        "visualMap": {
            "min": 0, 
            "max": 40000000 * (m/5.0), # Dynamically adjust scale max
            "calculable": True, "left": "right",
            "inRange": {"color": ["#e0f3f8", "#ffffbf", "#fee090", "#fdae61", "#f46d43", "#d73027", "#a50026"]}
        },
        "geo": {
            "map": "USA",
            "roam": True,
            "emphasis": {"label": {"show": True}},
            "itemStyle": {"areaColor": "#f3f3f3", "borderColor": "#999"}
        },
        "series": [
            {
                "name": "Sales",
                "type": "map",
                "geoIndex": 0,
                "data": [
                    {"name": "California", "value": int(38041430 * m/5.0)}, 
                    {"name": "Texas", "value": int(26059203 * m/5.0)},
                    {"name": "Florida", "value": int(19317568 * m/5.0)},
                    {"name": "New York", "value": int(19570261 * m/5.0)},
                    {"name": "Illinois", "value": int(12875255 * m/5.0)}
                ]
            },
            {
                "name": "Live Pulse",
                "type": "effectScatter",
                "coordinateSystem": "geo",
                "data": scatter_data,
                "symbolSize": 10 + (m * 2),
                "showEffectOn": "render",
                "rippleEffect": {"brushType": "stroke", "scale": 4},
                "label": {"formatter": "{b}", "position": "right", "show": True},
                "itemStyle": {"color": pulse_color, "shadowBlur": 10, "shadowColor": "#333"},
                "zlevel": 1
            }
        ]
    }
    st_echarts(options=map_options, map=usa_map, height="450px", key="usa_map")

with row2_2:
    options = {
        **base_options,
        "title": {"text": "Operations KPI", "left": "center"},
        "radar": {"indicator": [
            {"name": "Efficiency", "max": 100}, 
            {"name": "Quality", "max": 100}, 
            {"name": "Safety", "max": 100}, 
            {"name": "Speed", "max": 100}, 
            {"name": "Cost", "max": 100}
        ]},
        "series": [{"type": "radar", "data": [
            {"value": [int(85*m/5+10), int(90*m/5+5), int(95*m/5), int(80*m/5+15), int(70*m/5+25)], "name": "Current"},
            {"value": [80, 80, 90, 85, 80], "name": "Target"}
        ]}]
    }
    st_echarts(options=options, height="450px", key="radar_kpi")

# ==========================================
# ROW 3: ADVANCED ANALYSIS
# ==========================================
row3_1, row3_2, row3_3 = st.columns(3)

with row3_1:
    options = {
        **base_options,
        "title": {"text": "Productivity Heatmap", "left": "center"},
        "tooltip": {"position": "top"},
        "xAxis": {"type": "category", "data": ["Mon", "Tue", "Wed", "Thu", "Fri"]},
        "yAxis": {"type": "category", "data": ["Morn", "After", "Even"]},
        "visualMap": {
            "min": 0, 
            "max": 15, 
            "calculable": True, 
            "orient": "horizontal", 
            "left": "center", 
            "bottom": 0,
            "inRange": {
                "color": ["#fff7bc", "#fec44f", "#d95f0e"] # Warm Yellow-Orange-Red gradient
            }
        },
        "series": [{"type": "heatmap", "data": [[i, j, int((i*3+j*7)%11 * m/3 + 2)] for i in range(5) for j in range(3)], "label": {"show": True}}]
    }
    st_echarts(options=options, height="350px", key="productivity_heatmap")

with row3_2:
    options = {
        **base_options,
        "title": {"text": "Stock Performance (CANDL)", "left": "center"},
        "tooltip": {"trigger": "axis", "axisPointer": {"type": "cross"}},
        "xAxis": {"data": ["2024-01", "2024-02", "2024-03", "2024-04"]},
        "yAxis": {"scale": True},
        "series": [{"type": "candlestick", "data": [
            [2320+m*10, 2345+m*12, 2287+m*8, 2362+m*15], 
            [2345+m*12, 2310+m*5, 2300+m*5, 2355+m*15], 
            [2310+m*5, 2380+m*20, 2305+m*5, 2390+m*25], 
            [2380+m*20, 2360+m*15, 2340+m*15, 2395+m*30]
        ]}]
    }
    st_echarts(options=options, height="350px", key="stock_performance")

with row3_3:
    # Vary the distribution so rectangles actually resize
    budget_dist = {
        "Last 7 days": [50, 20, 30],
        "Last 30 days": [40, 40, 20],
        "Last 90 days": [30, 50, 20],
        "Year to Date": [45, 35, 20]
    }.get(period)
    
    options = {
        **base_options,
        "title": {"text": "Budget Allocation", "left": "center"},
        "series": [{"type": "treemap", "data": [
            {"name": "R&D", "value": budget_dist[0], "children": [{"name": "Core", "value": budget_dist[0]*0.7}, {"name": "Lab", "value": budget_dist[0]*0.3}]}, 
            {"name": "Marketing", "value": budget_dist[1], "children": [{"name": "Online", "value": budget_dist[1]*0.8}, {"name": "Offline", "value": budget_dist[1]*0.2}]},
            {"name": "Ops", "value": budget_dist[2]}
        ]}]
    }
    st_echarts(options=options, height="350px", key="budget_allocation")

# ==========================================
# ROW 4: PROCESS & RELATIONS
# ==========================================
row4_1, row4_2 = st.columns(2)

with row4_1:
    with open("./data/product.json", "r") as f:
        product_data = json.load(f)
    
    # Scale values instead of aggressive filtering to ensure chart is never empty
    # We use m/5.0 as a scaling factor (0.1 to 1.0)
    scale = m / 5.0
    processed_links = [
        {"source": l["source"], "target": l["target"], "value": l["value"] * scale}
        for l in product_data["links"]
        if l["value"] > 0.001 # Only filter out truly negligible noise
    ]
    
    # Only include nodes that are present in our filtered links
    active_node_names = set()
    for l in processed_links:
        active_node_names.add(l["source"])
        active_node_names.add(l["target"])
    
    processed_nodes = [n for n in product_data["nodes"] if n["name"] in active_node_names]

    options = {
        **base_options,
        "title": {"text": "Supply Chain Sustainability Flow", "left": "center"},
        "tooltip": {"trigger": "item", "triggerOn": "mousemove"},
        "series": [{
            "type": "sankey",
            "data": processed_nodes,
            "links": processed_links,
            "emphasis": {"focus": "adjacency"},
            "lineStyle": {"curveness": 0.5},
            "layoutIterations": 32,
            "nodeAlign": "left"
        }]
    }
    st_echarts(options=options, height="400px", key="sankey_flow")

with row4_2:
    options = {
        **base_options,
        "title": {"text": "Corporate Service Ecosystem", "left": "center"},
        "tooltip": {},
        "series": [{
            "type": "graph",
            "layout": "force",
            "symbolSize": 20 + m*4,
            "roam": True,
            "label": {"show": True, "fontSize": 10},
            "edgeLabel": {"fontSize": 10},
            "data": [
                {"name": "API Gateway", "category": 0},
                {"name": "Auth Service", "category": 1},
                {"name": "User DB", "category": 1},
                {"name": "Order Service", "category": 2},
                {"name": "Payment Gateway", "category": 2},
                {"name": "Stock Service", "category": 3},
                {"name": "Logistics API", "category": 3}
            ],
            "links": [
                {"source": "API Gateway", "target": "Auth Service"},
                {"source": "Auth Service", "target": "User DB"},
                {"source": "API Gateway", "target": "Order Service"},
                {"source": "Order Service", "target": "Payment Gateway"},
                {"source": "Order Service", "target": "Stock Service"},
                {"source": "Stock Service", "target": "Logistics API"}
            ],
            "categories": [{"name": "Entry"}, {"name": "Identity"}, {"name": "Commerce"}, {"name": "Inventory"}],
            "force": {"repulsion": 100 * m}
        }]
    }
    st_echarts(options=options, height="400px", key="graph_ecosystem")

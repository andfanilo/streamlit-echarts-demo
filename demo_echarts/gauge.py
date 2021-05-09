import random
import time
import streamlit as st
from streamlit_echarts import st_echarts


def render_ring_gauge():
    option = {
        "series": [
            {
                "type": "gauge",
                "startAngle": 90,
                "endAngle": -270,
                "pointer": {"show": False},
                "progress": {
                    "show": True,
                    "overlap": False,
                    "roundCap": True,
                    "clip": False,
                    "itemStyle": {"borderWidth": 1, "borderColor": "#464646"},
                },
                "axisLine": {"lineStyle": {"width": 40}},
                "splitLine": {"show": False, "distance": 0, "length": 10},
                "axisTick": {"show": False},
                "axisLabel": {"show": False, "distance": 50},
                "data": [
                    {
                        "value": random.randint(1, 99),
                        "name": "Perfect",
                        "title": {"offsetCenter": ["0%", "-30%"]},
                        "detail": {"offsetCenter": ["0%", "-20%"]},
                    },
                    {
                        "value": random.randint(1, 99),
                        "name": "Good",
                        "title": {"offsetCenter": ["0%", "0%"]},
                        "detail": {"offsetCenter": ["0%", "10%"]},
                    },
                    {
                        "value": random.randint(1, 99),
                        "name": "Commonly",
                        "title": {"offsetCenter": ["0%", "30%"]},
                        "detail": {"offsetCenter": ["0%", "40%"]},
                    },
                ],
                "title": {"fontSize": 14},
                "detail": {
                    "width": 50,
                    "height": 14,
                    "fontSize": 14,
                    "color": "auto",
                    "borderColor": "auto",
                    "borderRadius": 20,
                    "borderWidth": 1,
                    "formatter": "{value}%",
                },
            }
        ]
    }

    st_echarts(option, height="500px", key="echarts")
    time.sleep(2)
    st.experimental_rerun()


ST_GAUGE_DEMOS = {
    "Gauge: Ring Gauge": (
        render_ring_gauge,
        "https://echarts.apache.org/examples/en/editor.html?c=gauge-ring",
    ),
}

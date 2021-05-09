from streamlit_echarts import st_echarts


def render_basic_candlestick():
    option = {
        "xAxis": {"data": ["2017-10-24", "2017-10-25", "2017-10-26", "2017-10-27"]},
        "yAxis": {},
        "series": [
            {
                "type": "k",
                "data": [
                    [20, 34, 10, 38],
                    [40, 35, 30, 50],
                    [31, 38, 33, 44],
                    [38, 15, 5, 42],
                ],
            }
        ],
    }
    st_echarts(option, height="500px")


ST_CANDLESTICK_DEMOS = {
    "Candlestick: Basic Candlestick": (
        render_basic_candlestick,
        "https://echarts.apache.org/examples/en/editor.html?c=candlestick-simple",
    ),
}

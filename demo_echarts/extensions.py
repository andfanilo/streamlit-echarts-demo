import streamlit as st
from streamlit_echarts import st_echarts


def render_wordcloud():
    data = [
        {"name": name, "value": value}
        for name, value in [
            ("生活资源", "999"),
            ("供热管理", "888"),
            ("供气质量", "777"),
            ("生活用水管理", "688"),
            ("一次供水问题", "588"),
            ("交通运输", "516"),
            ("城市交通", "515"),
            ("环境保护", "483"),
            ("房地产管理", "462"),
            ("城乡建设", "449"),
            ("社会保障与福利", "429"),
            ("社会保障", "407"),
            ("文体与教育管理", "406"),
            ("公共安全", "406"),
            ("公交运输管理", "386"),
            ("出租车运营管理", "385"),
            ("供热管理", "375"),
            ("市容环卫", "355"),
            ("自然资源管理", "355"),
            ("粉尘污染", "335"),
            ("噪声污染", "324"),
        ]
    ]
    wordcloud_option = {"series": [{"type": "wordCloud", "data": data}]}
    st_echarts(wordcloud_option)


def render_liquidfill():
    liquidfill_option = {
        "series": [{"type": "liquidFill", "data": [0.6, 0.5, 0.4, 0.3]}]
    }
    st_echarts(liquidfill_option)


ST_EXTENSIONS_DEMOS = {
    "Extension: Wordcloud": (
        render_wordcloud,
        "https://github.com/ecomfe/echarts-wordcloud",
    ),
    "Extension: Liquidfill": (
        render_liquidfill,
        "https://github.com/ecomfe/echarts-liquidfill",
    ),
}

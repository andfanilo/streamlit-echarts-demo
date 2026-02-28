import inspect
import textwrap

import streamlit as st

from demo_echarts import ST_DEMOS
from demo_pyecharts import ST_PY_DEMOS


st.title("Examples")

with st.sidebar:
    st.header("Configuration")
    selected_api = (
        "pyecharts" if st.toggle("Use PyECharts API", value=False) else "echarts"
    )

    page_options = (
        list(ST_PY_DEMOS.keys())
        if selected_api == "pyecharts"
        else list(ST_DEMOS.keys())
    )
    selected_page = st.selectbox(
        label="Choose an example",
        options=page_options,
    )
    demo, url = (
        ST_DEMOS[selected_page]
        if selected_api == "echarts"
        else ST_PY_DEMOS[selected_page]
    )

    if selected_api == "echarts":
        st.caption(
            """ECharts demos are extracted from https://echarts.apache.org/examples/en/index.html,
        by copying/formattting the 'option' json object into st_echarts.
        Definitely check the echarts example page, convert the JSON specs to Python Dicts and you should get a nice viz."""
        )
    if selected_api == "pyecharts":
        st.caption(
            """Pyecharts demos are extracted from https://github.com/pyecharts/pyecharts-gallery,
        by converting the pyecharts object to JSON via dump_options() and passing it to st_echarts.
        Pyecharts is still using ECharts 4 underneath, which is why the theming between st_echarts with raw options and st_echarts with pyecharts options may differ."""
        )

demo()

sourcelines, _ = inspect.getsourcelines(demo)
with st.expander("Source Code"):
    st.code(textwrap.dedent("".join(sourcelines[1:])))
st.markdown(f"Credit: {url}")

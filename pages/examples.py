import inspect
import textwrap

import streamlit as st

from demo_echarts import ST_DEMOS_BY_CATEGORY
from demo_pyecharts import ST_PY_DEMOS_BY_CATEGORY


st.title("Examples")

with st.sidebar:
    st.header("Configuration")
    selected_api = (
        "pyecharts" if st.toggle("Use PyECharts API", value=False) else "echarts"
    )

    demos_by_category = (
        ST_PY_DEMOS_BY_CATEGORY
        if selected_api == "pyecharts"
        else ST_DEMOS_BY_CATEGORY
    )

    selected_category = st.selectbox(
        label="Category",
        options=list(demos_by_category.keys()),
    )

    demos_in_category = demos_by_category[selected_category]
    selected_demo = st.selectbox(
        label="Demo",
        options=list(demos_in_category.keys()),
    )

    demo, url = demos_in_category[selected_demo]

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

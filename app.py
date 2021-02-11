import inspect
import textwrap

import streamlit as st

from demo_echarts import ST_DEMOS
from demo_pyecharts import ST_PY_DEMOS


def main():
    st.title(":tada: Hello echarts 5")
    st.sidebar.header("Configuration")
    select_lang = st.sidebar.selectbox(
        "Choose your preferred API:", ("echarts", "pyecharts")
    )

    demo = None

    if select_lang == "echarts":
        page = st.sidebar.selectbox("Choose an example", options=list(ST_DEMOS.keys()))
        demo = ST_DEMOS[page]
    if select_lang == "pyecharts":
        page = st.sidebar.selectbox(
            "Choose an example", options=list(ST_PY_DEMOS.keys())
        )
        demo = ST_PY_DEMOS[page]

    demo()

    sourcelines, _ = inspect.getsourcelines(demo)
    with st.beta_expander("Source Code"):
        st.code(textwrap.dedent("".join(sourcelines[1:])))


if __name__ == "__main__":
    st.set_page_config(page_title="Streamlit Echarts Demo", page_icon=":chart:")
    main()

import inspect
import textwrap

import streamlit as st

from demo_echarts import ST_DEMOS
from demo_pyecharts import ST_PY_DEMOS


def _get_index(arr, val):
    """Replacement for index function
    Returns index of first occurence of val in arr, else 0
    """
    found_indexes = [i for i, el in enumerate(arr) if el == val]
    return found_indexes[0] if found_indexes else 0


def main():
    st.title(":chart_with_upwards_trend: Hello echarts 5")
    st.sidebar.header("Configuration")
    query_params = st.experimental_get_query_params()  # this returns a Dict[str, List]

    api = st.sidebar.selectbox(
        label="Choose your preferred API:",
        options=("echarts", "pyecharts"),
        index=_get_index(("echarts", "pyecharts"), query_params.get("api", [""])[0]),
    )

    page = query_params.get("page", [""])[0]
    demo = None

    if api == "echarts":
        page = st.sidebar.selectbox(
            label="Choose an example",
            options=list(ST_DEMOS.keys()),
            index=_get_index(list(ST_DEMOS.keys()), page),
        )
        demo = ST_DEMOS[page]
    if api == "pyecharts":
        page = st.sidebar.selectbox(
            label="Choose an example",
            options=list(ST_PY_DEMOS.keys()),
            index=_get_index(list(ST_PY_DEMOS.keys()), page),
        )
        demo = ST_PY_DEMOS[page]

    demo()
    st.experimental_set_query_params(api=api, page=page)

    sourcelines, _ = inspect.getsourcelines(demo)
    with st.beta_expander("Source Code"):
        st.code(textwrap.dedent("".join(sourcelines[1:])))


if __name__ == "__main__":
    st.set_page_config(
        page_title="Streamlit Echarts Demo", page_icon=":chart_with_upwards_trend:"
    )
    main()

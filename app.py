import inspect
import textwrap

import streamlit as st

from demo_echarts import ST_DEMOS
from demo_pyecharts import ST_PY_DEMOS


def handle_api_change(new_val):
    session_state = st.beta_session_state()
    session_state.api = [new_val]
    #st.experimental_set_query_params(api=new_val)


def handle_page_change(new_val):
    session_state = st.beta_session_state()
    session_state.page = [new_val]
    #st.experimental_set_query_params(page=new_val)


def main():
    st.title(":chart_with_upwards_trend: Hello echarts 5")
    st.sidebar.header("Configuration")

    # use Karrie's hack :) https://github.com/streamlit/streamlit/pull/1169#issuecomment-673001896
    # and tomkomt's: https://github.com/streamlit/streamlit/issues/2370#issuecomment-730411715
    query_params = st.experimental_get_query_params()  # this returns a Dict[str, List]
    app_state = st.experimental_get_query_params()

    session_state = st.beta_session_state(
        first_query_params=query_params, api=[0], page=[0]
    )
    first_query_params = session_state.first_query_params

    if len(first_query_params.keys()) == 0:
        session_state.first_query_params = app_state

    api_options = ("echarts", "pyecharts")
    preselected_api_index = (
        eval(str(first_query_params["api"][0])) if "api" in app_state else 0
    )
    selected_api = st.sidebar.selectbox(
        label="Choose your preferred API:",
        options=api_options,
        index=preselected_api_index
        if preselected_api_index > -1 and preselected_api_index < len(api_options)
        else 0,
        on_change=handle_api_change,
    )

    page_options = (
        list(ST_PY_DEMOS.keys()) if selected_api == "pyecharts" else list(ST_DEMOS.keys())
    )
    preselected_page_index = (
        eval(str(first_query_params["page"][0])) if "page" in app_state else 0
    )
    selected_page = st.sidebar.selectbox(
        label="Choose an example",
        options=page_options,
        index=preselected_page_index
        if preselected_page_index > -1 and preselected_api_index < len(page_options)
        else 0,
        on_change=handle_page_change,
    )
    demo, url = ST_DEMOS[selected_page]

    demo()

    app_state["api"] = [api_options.index(selected_api)]
    app_state["page"] = [page_options.index(selected_page)]
    st.experimental_set_query_params(**app_state)

    sourcelines, _ = inspect.getsourcelines(demo)
    with st.beta_expander("Source Code"):
        st.code(textwrap.dedent("".join(sourcelines[1:])))
    st.markdown(f"Credit: {url}")


if __name__ == "__main__":
    st.set_page_config(
        page_title="Streamlit Echarts Demo", page_icon=":chart_with_upwards_trend:"
    )
    main()

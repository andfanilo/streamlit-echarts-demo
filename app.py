import streamlit as st

st.set_page_config(
    page_title="Streamlit ECharts Demo",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
)

pg = st.navigation(
    [
        st.Page(
            "pages/showcase.py",
            title="Showcase",
            icon=":material/dashboard:",
            default=True,
        ),
        st.Page("pages/demo_app.py", title="API Guide", icon=":material/menu_book:"),
        st.Page("pages/examples.py", title="Examples", icon=":material/code:"),
    ]
)
pg.run()

with st.sidebar:
    st.markdown(
        ":material/code: [streamlit-echarts](https://github.com/andfanilo/streamlit-echarts)"
    )
    st.caption("Made in :streamlit: by [@andfanilo](https://andfanilo.com)")
    st.markdown(
        '<div style="margin-top: 0.75em;"><a href="https://www.buymeacoffee.com/andfanilo" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174" style="border-radius: 12px;"></a></div>',
        unsafe_allow_html=True,
    )

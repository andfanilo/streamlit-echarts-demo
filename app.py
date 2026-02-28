import streamlit as st

st.set_page_config(
    page_title="Streamlit ECharts Demo",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
)

pg = st.navigation([
    st.Page("pages/showcase.py", title="Showcase", icon=":material/dashboard:", default=True),
    st.Page("pages/demo_app.py", title="API Guide", icon=":material/menu_book:"),
    st.Page("pages/examples.py", title="Examples", icon=":material/code:"),
])
pg.run()

with st.sidebar:
    st.markdown(
        '<h6>Made in &nbsp<img src="https://streamlit.io/images/brand/streamlit-mark-color.png" alt="Streamlit logo" height="16">&nbsp by <a href="https://andfanilo.com">@andfanilo</a></h6>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div style="margin-top: 0.75em;"><a href="https://www.buymeacoffee.com/andfanilo" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a></div>',
        unsafe_allow_html=True,
    )

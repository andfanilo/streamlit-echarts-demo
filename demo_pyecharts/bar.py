import random
import streamlit as st
import pyecharts.options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts


def render_random_bar_chart():
    b = (
        Bar()
        .add_xaxis(["Microsoft", "Amazon", "IBM", "Oracle", "Google", "Alibaba"])
        .add_yaxis("2017-2018 Revenue in (billion $)", random.sample(range(100), 10))
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="Top cloud providers 2018", subtitle="2017-2018 Revenue"
            ),
            toolbox_opts=opts.ToolboxOpts(),
        )
    )
    st_pyecharts(
        b, key="echarts"
    )  # Add key argument to not remount component at every Streamlit run
    st.button("Randomize data")


ST_BAR_DEMOS = {
    "Bar: Random data": (
        render_random_bar_chart,
        "https://gallery.pyecharts.org/#/Line/line_base",
    )
}

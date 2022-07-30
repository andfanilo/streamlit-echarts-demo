from pyecharts import options as opts

from pyecharts.charts import Pie
from pyecharts.faker import Faker
from streamlit_echarts import st_pyecharts

def render_basic_pie_chart():
    c = (
        Pie()
        .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
        .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    st_pyecharts(c)


ST_PIE_DEMOS = {
    "Pie: Basic Pie": (
        render_basic_pie_chart,
        "https://gallery.pyecharts.org/#/Pie/pie_base",
    )
}
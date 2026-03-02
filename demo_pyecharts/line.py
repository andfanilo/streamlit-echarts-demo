import json
import pyecharts.options as opts

from pyecharts.charts import Line
from pyecharts.faker import Faker
from streamlit_echarts import st_echarts


def render_basic_line_chart():
    c = (
        Line()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts(title="Line-基本示例"))
    )
    st_echarts(options=json.loads(c.dump_options()))


ST_LINE_DEMOS = {
    "Basic Line": (
        render_basic_line_chart,
        "https://gallery.pyecharts.org/#/Line/line_base",
    )
}

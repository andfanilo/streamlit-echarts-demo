import json

from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
from streamlit_echarts import Map as st_Map
from streamlit_echarts import st_pyecharts


def render_map():
    with open("./data/countries.geo.json", "r") as f:
        map = st_Map("world", json.loads(f.read()),)
    c = Map(init_opts=opts.InitOpts(bg_color="white"))
    c.add("Demo", [list(z) for z in zip(Faker.country, Faker.values())], "world")
    c.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    c.set_global_opts(
        title_opts=opts.TitleOpts(title="Map world"),
        visualmap_opts=opts.VisualMapOpts(max_=200),
    )
    st_pyecharts(c, map=map, height=500)


ST_MAP_DEMOS = {
    "Map: Map World": (
        render_map,
        "https://gallery.pyecharts.org/#/Map/map_world",
    )
}

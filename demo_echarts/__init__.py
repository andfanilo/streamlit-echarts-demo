from .bar import render_set_style_of_single_bar
from .line import render_basic_line_chart
from .line import render_line_race
from .pie import render_nightingale_rose_diagram
from .scatter import render_anscombe_quartet

ST_DEMOS = {
    "Basic Line": (
        render_basic_line_chart,
        "https://echarts.apache.org/examples/en/editor.html?c=line-simple",
    ),
    "Racing Line": (
        render_line_race,
        "https://echarts.apache.org/examples/en/editor.html?c=line-race",
    ),
    "Set Style Of Single Bar": (
        render_set_style_of_single_bar,
        "https://echarts.apache.org/examples/en/editor.html?c=bar-data-color",
    ),
    "Nightingale Rose Diagram": (
        render_nightingale_rose_diagram,
        "https://echarts.apache.org/examples/en/editor.html?c=pie-roseType-simple",
    ),
    "Anscombe's Quartet": (
        render_anscombe_quartet,
        "https://echarts.apache.org/examples/en/editor.html?c=scatter-anscombe-quartet",
    ),
}

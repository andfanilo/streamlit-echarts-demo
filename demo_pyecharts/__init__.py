from .bar import ST_BAR_DEMOS
from .line import ST_LINE_DEMOS
from .map import ST_MAP_DEMOS
from .pie import ST_PIE_DEMOS
from .graph import ST_GRAPH_DEMOS

ST_PY_DEMOS_BY_CATEGORY = {
    "Bar": ST_BAR_DEMOS,
    "Line": ST_LINE_DEMOS,
    "Map": ST_MAP_DEMOS,
    "Pie": ST_PIE_DEMOS,
    "Graph": ST_GRAPH_DEMOS,
}

ST_PY_DEMOS = {k: v for demos in ST_PY_DEMOS_BY_CATEGORY.values() for k, v in demos.items()}

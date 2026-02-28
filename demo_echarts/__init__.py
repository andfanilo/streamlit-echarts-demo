from .bar import ST_BAR_DEMOS
from .boxplot import ST_BOXPLOT_DEMOS
from .calendar import ST_CALENDAR_DEMOS
from .candlestick import ST_CANDLESTICK_DEMOS
from .dataset import ST_DATASET_DEMOS
from .events import ST_EVENTS_DEMOS
from .extensions import ST_EXTENSIONS_DEMOS
from .funnel import ST_FUNNEL_DEMOS
from .gauge import ST_GAUGE_DEMOS
from .graph import ST_GRAPH_DEMOS
from .heatmap import ST_HEATMAP_DEMOS
from .line import ST_LINE_DEMOS
from .map import ST_MAP_DEMOS
from .parallel import ST_PARALLEL_DEMOS
from .pictorial_bar import ST_PICTORIAL_BAR_DEMOS
from .pie import ST_PIE_DEMOS
from .radar import ST_RADAR_DEMOS
from .sankey import ST_SANKEY_DEMOS
from .scatter import ST_SCATTER_DEMOS
from .sunburst import ST_SUNBURST_DEMOS
from .themeriver import ST_THEMERIVER_DEMOS
from .tree import ST_TREE_DEMOS
from .treemap import ST_TREEMAP_DEMOS

ST_DEMOS_BY_CATEGORY = {
    "Line": ST_LINE_DEMOS,
    "Bar": ST_BAR_DEMOS,
    "Pie": ST_PIE_DEMOS,
    "Scatter": ST_SCATTER_DEMOS,
    "Map": ST_MAP_DEMOS,
    "Candlestick": ST_CANDLESTICK_DEMOS,
    "Radar": ST_RADAR_DEMOS,
    "Boxplot": ST_BOXPLOT_DEMOS,
    "Heatmap": ST_HEATMAP_DEMOS,
    "Graph": ST_GRAPH_DEMOS,
    "Tree": ST_TREE_DEMOS,
    "Treemap": ST_TREEMAP_DEMOS,
    "Sunburst": ST_SUNBURST_DEMOS,
    "Parallel": ST_PARALLEL_DEMOS,
    "Sankey": ST_SANKEY_DEMOS,
    "Funnel": ST_FUNNEL_DEMOS,
    "Gauge": ST_GAUGE_DEMOS,
    "Pictorial Bar": ST_PICTORIAL_BAR_DEMOS,
    "Theme River": ST_THEMERIVER_DEMOS,
    "Calendar": ST_CALENDAR_DEMOS,
    "Dataset": ST_DATASET_DEMOS,
    "Events": ST_EVENTS_DEMOS,
    "Extensions": ST_EXTENSIONS_DEMOS,
}

ST_DEMOS = {k: v for demos in ST_DEMOS_BY_CATEGORY.values() for k, v in demos.items()}

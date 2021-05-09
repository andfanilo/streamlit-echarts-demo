from .bar import ST_BAR_DEMOS
from .line import ST_LINE_DEMOS
from .pie import ST_PIE_DEMOS
from .scatter import ST_SCATTER_DEMOS
from .map import ST_MAP_DEMOS
from .candlestick import ST_CANDLESTICK_DEMOS
from .radar import ST_RADAR_DEMOS
from .boxplot import ST_BOXPLOT_DEMOS
from .heatmap import ST_HEATMAP_DEMOS
from .graph import ST_GRAPH_DEMOS
from .tree import ST_TREE_DEMOS
from .treemap import ST_TREEMAP_DEMOS
from .sunburst import ST_SUNBURST_DEMOS
from .parallel import ST_PARALLEL_DEMOS
from .sankey import ST_SANKEY_DEMOS
from .funnel import ST_FUNNEL_DEMOS
from .gauge import ST_GAUGE_DEMOS

ST_DEMOS = {
    **ST_LINE_DEMOS,
    **ST_BAR_DEMOS,
    **ST_PIE_DEMOS,
    **ST_SCATTER_DEMOS,
    **ST_MAP_DEMOS,
    **ST_CANDLESTICK_DEMOS,
    **ST_RADAR_DEMOS,
    **ST_BOXPLOT_DEMOS,
    **ST_HEATMAP_DEMOS,
    **ST_GRAPH_DEMOS,
    **ST_TREE_DEMOS,
    **ST_TREEMAP_DEMOS,
    **ST_SUNBURST_DEMOS,
    **ST_PARALLEL_DEMOS,
    **ST_SANKEY_DEMOS,
    **ST_FUNNEL_DEMOS,
    **ST_GAUGE_DEMOS,
}

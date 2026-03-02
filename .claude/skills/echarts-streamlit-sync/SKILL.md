---
name: echarts-streamlit-sync
description: Transform ECharts example URLs into Streamlit st_echarts components. Use when a user provides an ECharts editor URL and wants to add or update it as a demo in the streamlit-echarts-demo project.
---

# ECharts Streamlit Sync

Extracts ECharts examples and transforms them into Python code for `streamlit-echarts`.

## Source Discovery

### Local Source Extraction (Preferred)
- Repository: `../echarts-examples`
- Source files: `../echarts-examples/public/examples/ts/<example-id>.ts`
- URL mapping: `https://echarts.apache.org/examples/en/editor.html?c=<example-id>` → file `<example-id>.ts`
- Metadata: comment block at top of each file has `title`, `category`, `titleCN`, `difficulty`

### Web Extraction (Fallback)
Only if local source is unavailable. Navigate to the editor URL and extract the `option` object.

## Workflow

### 1. Extract & Read Source
Given a URL like `?c=pie-padAngle`, read `../echarts-examples/public/examples/ts/pie-padAngle.ts`.

### 2. Identify Target File
From the `category` in the source comment, determine target: `demo_echarts/<category>.py`.

Existing categories and their files:
```
bar, boxplot, calendar, candlestick, dataset, events, extensions,
funnel, gauge, graph, heatmap, line, map, parallel, pictorial_bar,
pie, radar, sankey, scatter, sunburst, themeriver, tree, treemap
```

If the category doesn't have a file yet, create a new `demo_echarts/<category>.py` and register it in `demo_echarts/__init__.py` (add to both the imports and `ST_DEMOS_BY_CATEGORY`).

### 3. Transform JS → Python
Apply the `js-echarts-to-streamlit` skill rules. Key reminders:
- JS objects → Python dicts with quoted keys
- `true`/`false`/`null` → `True`/`False`/`None`
- JS functions/gradients → `JsCode("...").js_code`
- Data logic (loops, map, reduce) → Python equivalents
- **Only include properties present in the source** — don't add extra `grid`, `tooltip`, etc.
- Preserve `series` as dict or list matching the original

### 4. Write the Render Function

```python
def render_<descriptive_name>():
    options = { ... }
    st_echarts(options=options, height="500px")
```

- Function name: `render_` + snake_case description derived from the example
- Height: `500px` standard, `700px` only for exceptionally dense charts
- Import `JsCode` only if the function uses it
- Import `streamlit as st` only if using `session_state`/`st.button`/`st.rerun`

### 5. Register in Demo Dictionary

Add entry to `ST_<CATEGORY>_DEMOS` dict at bottom of the file:

```python
ST_PIE_DEMOS = {
    ...,
    "Chart Title from Source": (
        render_function_name,
        "https://echarts.apache.org/examples/en/editor.html?c=example-id",
    ),
}
```

- Dict key: use the `title` from the source file comment block
- Tuple: `(render_function, url_string)`
- Placement: user may specify position (e.g., "as first demo", "as second demo"); default to appending at end

### 6. Verify Conversion
When asked to check an existing conversion:
1. Read both the JS source and the Python function side by side
2. Compare every property — flag any missing, extra, or mismatched values
3. Check gradient colors, data arrays, formatter strings character by character
4. Report findings concisely: what matches, what differs

## Interactive Charts (Drilldown Pattern)
For examples using `myChart.on('click', ...)` with `setOption` for drill-down:

- Use `st.session_state` to track current view state
- Use `events` param to capture clicks: `events = {"click": "function(params) { return ... }"}`
- Check `result.chart_event` to update state and `st.rerun()`
- Use `st.button("Back")` instead of `graphic` onclick handlers
- Omit `universalTransition` (doesn't work across Streamlit reruns)
- Always use `key=` param on `st_echarts` for stateful charts

## New Category Checklist
When adding a category that doesn't exist yet:

1. Create `demo_echarts/<category>.py` with render function + `ST_<CATEGORY>_DEMOS` dict
2. In `demo_echarts/__init__.py`:
   - Add `from .<category> import ST_<CATEGORY>_DEMOS`
   - Add `"Display Name": ST_<CATEGORY>_DEMOS` to `ST_DEMOS_BY_CATEGORY`

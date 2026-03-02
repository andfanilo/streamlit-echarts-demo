---
name: js-echarts-to-streamlit
description: Transforms JavaScript ECharts options and demos into Python dictionary configurations compatible with streamlit-echarts.
---

# JS ECharts to Streamlit ECharts Transformation Guide

This skill converts standard JavaScript/TypeScript Apache ECharts examples into Python code rendered with `streamlit-echarts`.

## Core Transformation Rules

### 1. Data Structures & Primitives
- JS objects `{ key: value }` → Python dicts `{"key": value}` (all keys quoted)
- JS `true`/`false` → `True`/`False`
- JS `null` → `None`
- JS single-quoted strings → Python double-quoted strings
- JS trailing commas are fine in Python too

### 2. Data Preparation & Logic
- Convert `.map()`, `.filter()`, `.reduce()`, `for` loops → Python list comprehensions or loops
- Convert `Math.floor()`, `Math.random()` → `math.floor()`, `random.random()`
- Convert `Array.from({length: n}, (_, i) => ...)` → `list(range(n))` or comprehensions
- Replace `$.get('data.json', ...)` → `with open('data.json') as f: data = json.load(f)`
- When JS uses randomized data (e.g., shuffle for bump charts), use Python `random` module equivalently

### 3. Handling JavaScript via JsCode (Critical)

**Import:** `from streamlit_echarts import JsCode`

Wrap any raw JavaScript expression with `JsCode("...").js_code`. Use cases:

**Formatters (tooltip, label, axisLabel):**
```python
# JS: formatter: function(params) { return params.value + '%'; }
"formatter": JsCode("function(params) { return params.value + '%'; }").js_code

# JS: valueFormatter: function(value) { return value + ' ml'; }
"valueFormatter": JsCode("function(value) { return value + ' ml'; }").js_code
```

**Gradients:**
```python
# JS: color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{offset: 0, color: 'rgb(128, 255, 165)'}, {offset: 1, color: 'rgb(1, 191, 236)'}])
"color": JsCode(
    "new echarts.graphic.LinearGradient(0, 0, 0, 1, [{offset: 0, color: 'rgb(128, 255, 165)'}, {offset: 1, color: 'rgb(1, 191, 236)'}])"
).js_code
```

**Important:** Only use JsCode when the value must be a JS function or JS object constructor. Do NOT wrap plain strings, numbers, or static formatters like `"{value} °C"` — those stay as Python strings.

### 4. Series as Dict vs List
ECharts accepts `series` as either an object or array. Preserve the original structure:
- JS `series: { type: 'bar', ... }` → `"series": {"type": "bar", ...}` (dict)
- JS `series: [{ type: 'bar', ... }]` → `"series": [{"type": "bar", ...}]` (list)

### 5. Faithful Conversion
- Only include properties that exist in the JS source — do NOT add extra `grid`, `tooltip`, or other properties
- Preserve exact data values, colors, and option structure
- Use `len(names)` instead of hardcoded numbers when the JS uses `names.length`

### 6. Interactivity & Drilldown Pattern
For examples that use `myChart.on('click', ...)` to dynamically change options (e.g., drilldown):

```python
import streamlit as st

def render_interactive_chart():
    if "drill_state" not in st.session_state:
        st.session_state.drill_state = None

    # Build options conditionally based on session_state
    if st.session_state.drill_state is None:
        options = {
            ...  # top-level view
            "series": {
                "type": "bar",
                "id": "sales",
                "data": [
                    {"value": 5, "groupId": "animals"},
                    ...
                ],
                "universalTransition": {"enabled": True, "divideShape": "clone"},
            },
        }
    else:
        options = {
            ...  # drilled-down view
            "series": {
                "type": "bar",
                "id": "sales",
                "dataGroupId": drill_state,
                "data": [...],
                "universalTransition": {"enabled": True, "divideShape": "clone"},
            },
        }

    # Capture click events via JS function that returns data
    events = {
        "click": "function(params) { return params.data && params.data.groupId ? params.data.groupId : null }",
    }

    # Back button when drilled down
    if st.session_state.drill_state is not None:
        if st.button("Back", key="drill_back"):
            st.session_state.drill_state = None
            st.rerun()

    result = st_echarts(
        options=options, events=events, height="500px",
        replace_merge="series", key="render_drill",
    )
    if result and result.chart_event and result.chart_event in valid_groups:
        st.session_state.drill_state = result.chart_event
        st.rerun()
```

**Key points:**
- `events` dict maps event names to JS function strings that return data
- `result.chart_event` contains the returned value
- Use `st.session_state` to track state across Streamlit reruns
- Use `key=` on `st_echarts` so the component is tracked across option changes
- Use `st.button` for "Back" navigation instead of `graphic` onclick handlers

#### `universalTransition` and `replace_merge`
ECharts `universalTransition` requires merge-mode `setOption` so it can compare old vs new series by `id`. Pass `replace_merge="series"` to enable this:
- Keep the same `"id"` on the series across both views so ECharts can match them
- Include `"universalTransition": {"enabled": True, "divideShape": "clone"}` in each series
- Use `"dataGroupId"` on the drilled-down series and `"groupId"` on individual data items in the top-level series
- Without `replace_merge`, `st_echarts` uses `notMerge: true` which fully replaces options and prevents the morph animation

### 7. Limitations
- **DOM/Instance methods:** `myChart.getWidth()`, `myChart.dispatchAction()` etc. are not available from Python
- **Timer-based animations:** `setInterval`/`setTimeout` for rotating highlights or live data won't work
- **Graphic onclick:** `graphic` elements with `onclick` handlers must be replaced with Streamlit widgets (e.g., `st.button`)

## Function & Registration Pattern

```python
from streamlit_echarts import st_echarts

def render_chart_name():
    options = { ... }
    st_echarts(options=options, height="500px")

ST_CATEGORY_DEMOS = {
    "Chart Title": (
        render_chart_name,
        "https://echarts.apache.org/examples/en/editor.html?c=example-id",
    ),
}
```

- Function name: `render_<descriptive_name>()`
- Height: `500px` standard, `700px` for dense charts (e.g., Sunburst)
- Demo dict key: use the `title` from the source file's comment block

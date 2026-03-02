---
name: echarts-streamlit-sync
description: Transform ECharts example URLs into Streamlit st_echarts components. Use when a user provides an ECharts editor URL and wants to add or update it as a demo in the streamlit-echarts-demo project.
---

# ECharts Streamlit Sync

This skill automates the extraction and transformation of ECharts configurations from the official editor into Python code compatible with `streamlit-echarts`.

## Workflow

1.  **Extract**: Navigate to the provided ECharts editor URL (e.g., `https://echarts.apache.org/examples/en/editor.html?c=...`).
2.  **Capture**: Use `take_snapshot` or `evaluate_script` to get the `option` object from the Monaco editor.
3.  **Transform**:
    -   Convert JavaScript objects to Python dictionaries.
    -   Replace JavaScript functions (e.g., `formatter`, `valueFormatter`) with `JsCode("...").js_code`.
    -   Use Python list comprehensions for repetitive data (e.g., months, range of dates).
    -   Ensure boolean/null values are Python-compatible (`True`, `False`, `None`).
4.  **Integrate**:
    -   Identify the target file in `demo_echarts/` or `demo_pyecharts/` based on the category (e.g., `bar.py` for "Bar" charts).
    -   Create a `render_<name>` function.
    -   Add the function and URL to the matching `ST_*_DEMOS` dictionary.

## Transformation Patterns

### JavaScript Formatter to JsCode
**JS**:
```javascript
formatter: function (params) { return params.value + ' ml'; }
```
**Python**:
```python
"formatter": JsCode("function (params) { return params.value + ' ml'; }").js_code
```

### xAxis Data Generation
**JS**:
```javascript
data: (function () {
  let list = [];
  for (let i = 1; i <= 12; i++) { list.push('Month ' + i); }
  return list;
})()
```
**Python**:
```python
"data": [f"Month {i}" for i in range(1, 13)]
```

### Dictionary Update
Always add to `ST_<CATEGORY>_DEMOS`:
```python
ST_BAR_DEMOS = {
    ...,
    "New Chart Name": (render_new_chart, "https://echarts.apache.org/examples/en/editor.html?c=...")
}
```

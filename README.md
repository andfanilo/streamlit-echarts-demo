# Streamlit - Echarts - Demo

Streamlit ECharts demo on Streamlit Sharing

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/andfanilo/streamlit-echarts-demo/master/app.py)

## Install

```sh
uv pip install -r requirements.txt
```

For local development against the `streamlit-echarts` source:

```sh
uv pip install -e ../streamlit-echarts --force-reinstall
```

## Run

```sh
streamlit run app.py
```

## Requirements

- Python >= 3.10
- `streamlit >= 1.53`
- `streamlit-echarts[pyecharts] >= 0.6.0` (v2, with ECharts 6)
- `pyecharts >= 2.0` (pulled in via the `[pyecharts]` extra)

## Contribute

- Add the example source code in the corresponding module in `demo_echarts` or `demo_pyecharts`.
- Add a line for your demo in `ST_xxx_DEMOS` at the end of the module.
- Check that your demo has been added with `streamlit run app.py`.
- Request a PR.

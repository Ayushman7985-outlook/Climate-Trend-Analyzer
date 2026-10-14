# Project Guide: Climate Trend Analyzer

## 1. What the project does
The application turns monthly climate-like observations into cleaned records, yearly summaries, a descriptive temperature trend, anomaly candidates, charts, and an interactive dashboard.

## 2. Three possible versions
- **Easy:** Pandas cleaning + Matplotlib charts. Best for a first working submission.
- **Intermediate (selected):** cleaning, yearly summaries, Linear Regression trend, Isolation Forest anomalies, tests, and Streamlit.
- **Advanced:** documented public datasets, regional comparisons, seasonal decomposition, uncertainty estimates, robust trend tests, and carefully validated forecasting.

The intermediate version offers strong portfolio breadth without requiring a GPU.

## 3. Module responsibilities
- `data_generator.py`: creates clearly labelled synthetic data.
- `preprocessing.py`: validates columns, parses dates, handles duplicates and missing values, creates calendar features.
- `analysis.py`: aggregates by year, estimates a descriptive linear trend, and flags statistical anomaly candidates.
- `visualize.py`: saves charts.
- `app/streamlit_app.py`: displays metrics, charts, data, and anomaly candidates.
- `tests/test_pipeline.py`: checks key pipeline behaviors.

## 4. Interpretation
Temperature slope is measured in °C per year. The linear fit summarizes this dataset only. Rainfall totals are sums of monthly rainfall and are meaningful only if the input values represent monthly totals. Anomaly detection is unsupervised and can flag rare but valid observations as well as data problems.

## 5. Proof checklist
- [ ] Terminal output after `python main.py`
- [ ] Dataset preview in `data/raw/climate_observations.csv`
- [ ] Cleaned data and missing-value check
- [ ] `temperature_trend.png`
- [ ] `monthly_rainfall.png`
- [ ] `temperature_vs_rainfall.png`
- [ ] Dashboard screenshot
- [ ] Test result from `python -m pytest -q`
- [ ] GitHub repository and rendered README

## 6. Interview explanation
“I built a modular climate analytics pipeline that generates or accepts monthly observations, validates and cleans the records, engineers calendar features, summarizes yearly patterns, fits a descriptive linear trend, flags multivariate outliers using Isolation Forest, and communicates results through saved plots and a Streamlit dashboard. The demo data are synthetic, so I distinguish software validation from scientific conclusions.”

## 7. Responsible use
Never label generated records as real measurements. When using a public dataset, include the dataset URL, retrieval date, units, geographic scope, station or grid identifiers where relevant, license, and any transformations. Avoid presenting a simple linear extrapolation as an official climate projection.

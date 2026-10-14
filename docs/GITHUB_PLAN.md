# GitHub Publishing and Proof Plan

## Suggested repository
`climate-trend-analyzer`

## Description
`Python climate-data analytics demo with preprocessing, trend analysis, anomaly detection, visualizations, tests, and a Streamlit dashboard.`

## Topics
`python`, `data-science`, `climate-data`, `time-series-analysis`, `pandas`, `scikit-learn`, `streamlit`, `data-visualization`

## Suggested commit sequence
1. `chore: initialize climate trend analyzer structure`
2. `feat: generate reproducible synthetic climate dataset`
3. `feat: add climate data cleaning pipeline`
4. `feat: add yearly trend and anomaly analysis`
5. `feat: export climate charts and summary report`
6. `feat: add Streamlit climate dashboard`
7. `test: cover preprocessing and analysis pipeline`
8. `docs: add setup guide and project limitations`

## Commands
Run from the project root:
```bash
git init
git branch -M main
git add .
git commit -m "feat: build climate trend analyzer pipeline"
git remote add origin https://github.com/YOUR-USERNAME/climate-trend-analyzer.git
git push -u origin main
```
If the remote already contains a README or license, pull/reconcile it before pushing. Do not commit virtual environments or secrets.

## Evidence assets
Capture genuine screenshots after execution:
- `docs/screenshots/01_terminal_pipeline.png`
- `docs/screenshots/02_raw_dataset.png`
- `docs/screenshots/03_temperature_trend.png`
- `docs/screenshots/04_monthly_rainfall.png`
- `docs/screenshots/05_anomaly_table.png`
- `docs/screenshots/06_streamlit_dashboard.png`
- `docs/screenshots/07_tests_passed.png`
- `docs/screenshots/08_github_readme.png`

## Resume bullets (edit to match actual results)
- Built a modular Python pipeline to validate monthly climate-like records, engineer date features, and generate yearly temperature and rainfall summaries.
- Implemented descriptive Linear Regression trend fitting and Isolation Forest anomaly candidate detection, with exported CSVs and visual reports.
- Developed a Streamlit dashboard and automated tests to improve interpretability and reproducibility; clearly documented synthetic-data limitations.

Only claim the steps and results you personally ran and verified.

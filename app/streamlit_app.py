"""Interactive dashboard for Climate Trend Analyzer."""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import pandas as pd
import streamlit as st
from src.config import CLEAN_DATA_PATH, YEARLY_SUMMARY_PATH, ANOMALY_PATH, INSIGHTS_PATH
from src.data_generator import generate_synthetic_data
from src.preprocessing import clean_climate_data
from src.analysis import run_analysis

st.set_page_config(page_title="Climate Trend Analyzer", page_icon="🌦️", layout="wide")
st.title("🌦️ Climate Trend Analyzer")
st.caption("Exploratory climate analytics demo — synthetic data, not official observations.")

if st.button("Generate data and refresh analysis"):
    from src.config import RAW_DATA_PATH
    generate_synthetic_data().to_csv(RAW_DATA_PATH, index=False)
    clean_climate_data()
    run_analysis()
    st.success("Demo data and analysis refreshed. Reload the page if needed.")

if not CLEAN_DATA_PATH.exists() or not YEARLY_SUMMARY_PATH.exists():
    st.info("Run `python main.py` from the project root before opening the dashboard.")
    st.stop()

df = pd.read_csv(CLEAN_DATA_PATH, parse_dates=["date"])
yearly = pd.read_csv(YEARLY_SUMMARY_PATH)
anomalies = pd.read_csv(ANOMALY_PATH) if ANOMALY_PATH.exists() else pd.DataFrame()

c1, c2, c3 = st.columns(3)
c1.metric("Monthly observations", f"{len(df):,}")
c2.metric("Years covered", f"{df['year'].min()}–{df['year'].max()}")
c3.metric("Anomalies flagged", f"{len(anomalies):,}")

st.subheader("Yearly temperature trend")
st.line_chart(yearly.set_index("year")[["mean_temperature_c", "linear_fit_temperature_c"]])
st.subheader("Monthly rainfall pattern")
monthly = df.groupby("month")["rainfall_mm"].mean()
st.bar_chart(monthly)
st.subheader("Observation data")
st.dataframe(df, use_container_width=True)
st.subheader("Statistical anomaly candidates")
if anomalies.empty:
    st.write("No anomaly output is available yet. Run `python main.py`.")
else:
    st.dataframe(anomalies, use_container_width=True)
st.subheader("Automated summary")
if INSIGHTS_PATH.exists():
    st.code(INSIGHTS_PATH.read_text(encoding="utf-8"))
st.warning("Synthetic values are used for demonstration. Do not cite them as real climate evidence.")

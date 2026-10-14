"""Trend summaries, anomaly detection, and simple illustrative trend estimates."""
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.linear_model import LinearRegression
from .config import CLEAN_DATA_PATH, ANOMALY_PATH, YEARLY_SUMMARY_PATH, INSIGHTS_PATH

def build_yearly_summary(df):
    summary = (df.groupby("year", as_index=False)
        .agg(mean_temperature_c=("temperature_c", "mean"),
             total_rainfall_mm=("rainfall_mm", "sum"),
             mean_humidity_pct=("humidity_pct", "mean"),
             observation_count=("date", "count")))
    return summary

def detect_anomalies(df, contamination=0.03):
    features = df[["temperature_c", "rainfall_mm", "humidity_pct"]].copy()
    model = IsolationForest(contamination=contamination, random_state=42)
    result = df.copy()
    result["anomaly_score"] = model.fit_predict(features)
    result["is_anomaly"] = result["anomaly_score"].eq(-1)
    return result

def estimate_temperature_trend(yearly):
    """Fit a straight line to yearly average temperature; not a climate projection."""
    X = yearly[["year"]].to_numpy()
    y = yearly["mean_temperature_c"].to_numpy()
    model = LinearRegression().fit(X, y)
    slope = float(model.coef_[0])
    fitted = model.predict(X)
    return model, slope, fitted

def run_analysis(input_path=CLEAN_DATA_PATH):
    df = pd.read_csv(input_path, parse_dates=["date"])
    yearly = build_yearly_summary(df)
    flagged = detect_anomalies(df)
    _, slope, fitted = estimate_temperature_trend(yearly)
    yearly["linear_fit_temperature_c"] = fitted
    yearly.to_csv(YEARLY_SUMMARY_PATH, index=False)
    flagged.loc[flagged["is_anomaly"]].to_csv(ANOMALY_PATH, index=False)

    first = yearly.iloc[0]
    last = yearly.iloc[-1]
    trend = "increased" if slope > 0 else "decreased" if slope < 0 else "remained broadly flat"
    text = [
        "CLIMATE TREND ANALYZER — AUTOMATED SUMMARY",
        "Dataset type: synthetic demonstration data; not real measured observations.",
        f"Period: {int(first['year'])}–{int(last['year'])}",
        f"Estimated linear temperature trend: {slope:.3f} °C/year",
        f"Across the fitted period, yearly average temperature {trend} in this dataset.",
        f"Rows flagged by Isolation Forest: {int(flagged['is_anomaly'].sum())} of {len(flagged)}",
        "Interpretation caution: anomaly flags are statistical candidates, not proof of climate events.",
        "The linear fit is descriptive and must not be presented as an authoritative future climate projection."
    ]
    INSIGHTS_PATH.write_text("\n".join(text), encoding="utf-8")
    return df, yearly, flagged, slope

if __name__ == "__main__":
    _, yearly, flagged, slope = run_analysis()
    print(f"Yearly summary saved to {YEARLY_SUMMARY_PATH}")
    print(f"Anomaly rows saved to {ANOMALY_PATH}")
    print(f"Estimated temperature slope: {slope:.3f} °C/year")
    print(f"Anomalies detected: {int(flagged['is_anomaly'].sum())}")

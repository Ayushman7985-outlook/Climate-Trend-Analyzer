import pandas as pd
from src.data_generator import generate_synthetic_data
from src.preprocessing import clean_climate_data
from src.analysis import build_yearly_summary, detect_anomalies

def test_generator_has_expected_columns():
    df = generate_synthetic_data(start="2000-01-01", end="2001-12-01")
    assert {"date", "temperature_c", "rainfall_mm", "humidity_pct"} <= set(df.columns)
    assert len(df) == 24

def test_cleaning_fills_missing_values(tmp_path):
    raw_path = tmp_path / "raw.csv"
    clean_path = tmp_path / "clean.csv"
    df = generate_synthetic_data(start="2000-01-01", end="2010-12-01")
    df.loc[0, "temperature_c"] = float("nan")
    df.to_csv(raw_path, index=False)
    clean = clean_climate_data(raw_path, clean_path)
    assert clean["temperature_c"].isna().sum() == 0
    assert clean_path.exists()

def test_yearly_summary_and_anomaly_flags():
    df = generate_synthetic_data(start="2000-01-01", end="2010-12-01")
    summary = build_yearly_summary(df.assign(year=df["date"].dt.year))
    assert len(summary) == 11
    flagged = detect_anomalies(df)
    assert "is_anomaly" in flagged.columns

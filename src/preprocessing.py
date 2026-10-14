"""Data loading, validation, and basic cleaning."""
import pandas as pd
from .config import RAW_DATA_PATH, CLEAN_DATA_PATH

REQUIRED_COLUMNS = ["date", "temperature_c", "rainfall_mm", "humidity_pct"]

def clean_climate_data(input_path=RAW_DATA_PATH, output_path=CLEAN_DATA_PATH):
    df = pd.read_csv(input_path)
    missing_columns = set(REQUIRED_COLUMNS) - set(df.columns)
    if missing_columns:
        raise ValueError(f"Dataset is missing required columns: {sorted(missing_columns)}")

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    for col in ["temperature_c", "rainfall_mm", "humidity_pct"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=["date"]).sort_values("date")
    df = df.drop_duplicates(subset=["date"], keep="last")
    # Keep physically plausible ranges; replace invalid values with missing values.
    df.loc[~df["rainfall_mm"].between(0, 2000), "rainfall_mm"] = float("nan")
    df.loc[~df["humidity_pct"].between(0, 100), "humidity_pct"] = float("nan")
    df.loc[~df["temperature_c"].between(-90, 65), "temperature_c"] = float("nan")

    for col in ["temperature_c", "rainfall_mm", "humidity_pct"]:
        df[col] = df[col].interpolate(limit_direction="both")
        df[col] = df[col].fillna(df[col].median())

    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["season"] = df["month"].map({
        12: "Winter", 1: "Winter", 2: "Winter",
        3: "Pre-monsoon", 4: "Pre-monsoon", 5: "Pre-monsoon",
        6: "Monsoon", 7: "Monsoon", 8: "Monsoon", 9: "Monsoon",
        10: "Post-monsoon", 11: "Post-monsoon"
    })
    df.to_csv(output_path, index=False)
    return df

if __name__ == "__main__":
    clean = clean_climate_data()
    print(f"Cleaned dataset: {len(clean)} rows; {clean.isna().sum().sum()} missing cells remain.")
    print(f"Saved to {CLEAN_DATA_PATH}")

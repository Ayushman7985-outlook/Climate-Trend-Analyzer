"""Create clearly labelled synthetic climate observations for a reproducible demo."""
import numpy as np
import pandas as pd
from .config import RAW_DATA_PATH

def generate_synthetic_data(start="1990-01-01", end="2025-12-01", seed=42):
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start, end=end, freq="MS")
    month = dates.month.to_numpy()
    years_from_start = (dates.year.to_numpy() - dates.year.min()).astype(float)

    # Illustrative seasonal cycle plus a small artificial warming signal.
    seasonal_temp = 17 + 10 * np.sin(2 * np.pi * (month - 4) / 12)
    warming = 0.035 * years_from_start
    temperature = seasonal_temp + warming + rng.normal(0, 1.4, len(dates))

    # Monsoon-like rainfall pattern for demonstration, not a real location.
    rain_season = np.exp(-0.5 * ((month - 7.5) / 1.8) ** 2)
    rainfall = np.maximum(0, 22 + 150 * rain_season + rng.normal(0, 18, len(dates)))
    humidity = np.clip(48 + 0.18 * rainfall + rng.normal(0, 7, len(dates)), 20, 100)

    # Inject a small number of artificial anomalies so detection can be demonstrated.
    if len(dates) > 80:
        hot_idx = [int(len(dates) * 0.35), int(len(dates) * 0.78)]
        dry_idx = [int(len(dates) * 0.55)]
        temperature[hot_idx] += 8
        rainfall[dry_idx] = 0.2

    df = pd.DataFrame({
        "date": dates,
        "temperature_c": np.round(temperature, 2),
        "rainfall_mm": np.round(rainfall, 2),
        "humidity_pct": np.round(humidity, 2),
        "data_source": "synthetic_demo"
    })
    # Add a couple of missing values to make the cleaning step demonstrable.
    if len(df) > 100:
        df.loc[13, "humidity_pct"] = np.nan
        df.loc[64, "rainfall_mm"] = np.nan
    return df

if __name__ == "__main__":
    df = generate_synthetic_data()
    df.to_csv(RAW_DATA_PATH, index=False)
    print(f"Saved {len(df):,} synthetic monthly rows to {RAW_DATA_PATH}")
    print("NOTICE: these are simulated observations, not measured climate records.")

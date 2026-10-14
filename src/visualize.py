"""Save reproducible charts for the project report and GitHub README."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from .config import CLEAN_DATA_PATH, YEARLY_SUMMARY_PATH, IMAGES_DIR

def create_charts():
    df = pd.read_csv(CLEAN_DATA_PATH, parse_dates=["date"])
    yearly = pd.read_csv(YEARLY_SUMMARY_PATH)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(yearly["year"], yearly["mean_temperature_c"], label="Yearly mean")
    ax.plot(yearly["year"], yearly["linear_fit_temperature_c"], linestyle="--", label="Linear fit")
    ax.set(title="Yearly Mean Temperature Trend (Synthetic Demo)", xlabel="Year", ylabel="Temperature (°C)")
    ax.legend(); fig.tight_layout()
    fig.savefig(IMAGES_DIR / "temperature_trend.png", dpi=150); plt.close(fig)

    monthly = df.groupby("month", as_index=False).agg(
        mean_temperature_c=("temperature_c", "mean"),
        mean_rainfall_mm=("rainfall_mm", "mean"))
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(monthly["month"], monthly["mean_rainfall_mm"])
    ax.set(title="Average Rainfall by Month (Synthetic Demo)", xlabel="Month", ylabel="Rainfall (mm)")
    fig.tight_layout(); fig.savefig(IMAGES_DIR / "monthly_rainfall.png", dpi=150); plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.scatter(df["rainfall_mm"], df["temperature_c"], alpha=0.55)
    ax.set(title="Temperature vs Rainfall (Synthetic Demo)", xlabel="Rainfall (mm)", ylabel="Temperature (°C)")
    fig.tight_layout(); fig.savefig(IMAGES_DIR / "temperature_vs_rainfall.png", dpi=150); plt.close(fig)
    print(f"Charts saved in {IMAGES_DIR}")

if __name__ == "__main__":
    create_charts()

"""Run the complete reproducible analysis pipeline."""
from src.data_generator import generate_synthetic_data
from src.config import RAW_DATA_PATH
from src.preprocessing import clean_climate_data
from src.analysis import run_analysis
from src.visualize import create_charts

def main():
    raw = generate_synthetic_data()
    raw.to_csv(RAW_DATA_PATH, index=False)
    print(f"1/4 Generated {len(raw)} synthetic monthly records.")
    clean = clean_climate_data()
    print(f"2/4 Cleaned data: {len(clean)} rows.")
    _, yearly, flagged, slope = run_analysis()
    print(f"3/4 Analysis complete: slope={slope:.3f} °C/year; anomalies={int(flagged['is_anomaly'].sum())}.")
    create_charts()
    print("4/4 Complete. See outputs/ and data/processed/.")
    print("Reminder: this run uses synthetic demonstration data.")

if __name__ == "__main__":
    main()

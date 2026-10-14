from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
OUTPUT_DIR = ROOT_DIR / "outputs"
IMAGES_DIR = OUTPUT_DIR / "images"

for directory in (RAW_DATA_DIR, PROCESSED_DATA_DIR, OUTPUT_DIR, IMAGES_DIR):
    directory.mkdir(parents=True, exist_ok=True)

RAW_DATA_PATH = RAW_DATA_DIR / "climate_observations.csv"
CLEAN_DATA_PATH = PROCESSED_DATA_DIR / "climate_cleaned.csv"
ANOMALY_PATH = OUTPUT_DIR / "anomalies.csv"
YEARLY_SUMMARY_PATH = OUTPUT_DIR / "yearly_summary.csv"
INSIGHTS_PATH = OUTPUT_DIR / "insights.txt"

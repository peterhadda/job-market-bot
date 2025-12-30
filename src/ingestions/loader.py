import pandas as pd
from pathlib import Path

# Get project root
BASE_DIR = Path(__file__).resolve().parents[2]

def get_data():
    DATA_PATH = BASE_DIR / "data" / "raw" / "jobs.csv"
    df = pd.read_csv(DATA_PATH)
    return df

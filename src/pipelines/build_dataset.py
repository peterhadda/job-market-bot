import pandas as pd
from src.ingestions.loader import get_data
from src.preprocessing.normalizer import normalize_jobs

from pathlib import Path


# Get project root
BASE_DIR = Path(__file__).resolve().parents[2]
output_dir = BASE_DIR / "data" / "processed"
df=get_data()

df=normalize_jobs(df)
output_path = output_dir / "jobs_clean.csv"
df.to_csv(output_path, index=False)



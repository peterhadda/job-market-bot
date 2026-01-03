import pandas as pd
from src.ingestions.loader import get_data
from src.preprocessing.normalizer import normalize_jobs
from src.preprocessing.cleaner import  clean_jobs_text
from src.skills.extractor import extract_skills


from src.skills.index import build_inverted_index, search

from pathlib import Path


# Get project root
BASE_DIR = Path(__file__).resolve().parents[2]
output_dir = BASE_DIR / "data" / "processed"
df=get_data()

df=normalize_jobs(df)
df=clean_jobs_text(df)
output_path = output_dir / "jobs_clean.csv"
df["skills"] = df["text"].apply(extract_skills)


df.to_csv(output_path, index=False)




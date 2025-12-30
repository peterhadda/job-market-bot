import pandas as pd
from src.ingestions.schema import COLUMN_MAPPING
from src.ingestions.schema import KEEP_COLUMNS
from src.ingestions.schema import EMPLOYMENT_MAP
from src.ingestions.schema import EXPERIENCE_MAP

#RENAME JOBS
def rename_jobs(df: pd.DataFrame) -> pd.DataFrame:
    return df.rename(columns=COLUMN_MAPPING)


#KEEP COLUMNS WE CARE ABOUT
def keep_only_needed_columns(df: pd.DataFrame) -> pd.DataFrame:
    existing=[c for c in KEEP_COLUMNS if c in df.columns]
    return df[existing].copy()

def normalize_remote(df: pd.DataFrame) -> pd.DataFrame:
    # remote is 0/1 (or missing). Make it True/False always.
    if "remote" in df.columns:
        df["remote"] = df["remote"].fillna(0).astype(int).astype(bool)
    return df

def normalize_employment(df: pd.DataFrame) -> pd.DataFrame:
    if "employment_type" in df.columns:
        df["employment_type"] = df["employment_type"].map(EMPLOYMENT_MAP).fillna("other")
    if "experience_level" in df.columns:
        df["experience_level"] = df["experience_level"].map(EMPLOYMENT_MAP).fillna("undefined")
    if "education_level" in df.columns:
       df["education_level"] = df["education_level"].map(EMPLOYMENT_MAP).fillna("undefined")
    return df

def normalize_jobs(df: pd.DataFrame) -> pd.DataFrame:
    df=rename_jobs(df)
    df=keep_only_needed_columns(df)
    df=normalize_remote(df)
    df=normalize_employment(df)
    return df
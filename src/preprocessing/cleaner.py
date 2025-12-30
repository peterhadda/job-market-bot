
import pandas as pd

def clean_text(text):
    if pd.isna(text):
        return ""
    else:
        text = str(text).lower().strip()
        return " ".join(text.split())
def clean_text_columns(df,cols):
    for col in cols:
        df[col] = df[col].apply(clean_text)
    return df

def make_combined_text(df):
    df["text"] = ( df["title"].fillna("") +" " +df["description"].fillna("")).str.strip()
    return df

def clean_jobs_text(df):
    df=clean_text_columns(df,["title","description"])
    df=make_combined_text(df)
    return df




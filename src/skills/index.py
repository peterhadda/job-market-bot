import pandas as pd

index = {}
def build_inverted_index(df, job_id_col="job_id", skills_col="skills"):
    for job_id, skills in zip(df["job_id"], df["skills"]):
          return index

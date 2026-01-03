# src/pipelines/generate_report.py

import pandas as pd
from pathlib import Path
import ast
import re

from src.reporting.report_builder import (
    build_cluster_summary,
    top_skills_per_cluster
)
from src.reporting.charts import (
    plot_job_count_by_cluster,
    plot_top_skills_for_cluster
)

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_PATH = BASE_DIR / "data" / "processed" / "jobs_with_clusters.csv"
REPORTS_DIR = BASE_DIR / "reports"


def safe_filename(name: str) -> str:
    """
    Convert any string into a Windows-safe filename.
    Keeps only [a-z0-9_] and replaces everything else with "_".
    """
    name = name.lower().strip()
    name = re.sub(r"[^a-z0-9_]+", "_", name)
    name = re.sub(r"_+", "_", name)  # collapse multiple underscores
    return name.strip("_")


def run_report():
    # Create reports folder if not exists
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    # 1) Load clustered data
    df = pd.read_csv(DATA_PATH)

    # 2) Convert skills from string -> list safely (if needed)
    if "skills" in df.columns and len(df) > 0 and isinstance(df["skills"].iloc[0], str):
        df["skills"] = df["skills"].apply(
            lambda x: ast.literal_eval(x) if isinstance(x, str) else []
        )

    # 3) Build summary table
    summary = build_cluster_summary(df)

    # 4) Save summary table
    summary_path = REPORTS_DIR / "cluster_summary.csv"
    summary.to_csv(summary_path, index=False)
    print(f"✅ Saved: {summary_path}")

    # 5) Plot job count per cluster
    job_count_chart_path = REPORTS_DIR / "job_count_per_cluster.png"
    plot_job_count_by_cluster(summary, job_count_chart_path)
    print(f"✅ Saved: {job_count_chart_path}")

    # 6) Plot top skills per cluster
    skills_map = top_skills_per_cluster(df)

    for cluster_label, skills in skills_map.items():
        safe_label = safe_filename(cluster_label)
        filename = f"top_skills_{safe_label}.png"
        out_path = REPORTS_DIR / filename

        plot_top_skills_for_cluster(cluster_label, skills, out_path)
        print(f"✅ Saved: {out_path}")


if __name__ == "__main__":
    run_report()


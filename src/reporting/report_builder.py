# src/reporting/report_builder.py

from __future__ import annotations

from collections import Counter
from typing import Dict, List, Tuple, Optional

import pandas as pd


def top_skills_per_cluster(
    df: pd.DataFrame,
    cluster_col: str = "cluster_label",
    skills_col: str = "skills",
    top_n: int = 10
) -> Dict[str, List[Tuple[str, int]]]:
    """
    Compute top skills per cluster.

    Returns:
      { cluster_label: [("sql", 120), ("python", 95), ...] }
    """
    if cluster_col not in df.columns:
        raise ValueError(f"Missing column '{cluster_col}' in df")
    if skills_col not in df.columns:
        raise ValueError(f"Missing column '{skills_col}' in df")

    result: Dict[str, List[Tuple[str, int]]] = {}

    for cluster in df[cluster_col].dropna().unique():
        cluster_df = df[df[cluster_col] == cluster]

        all_skills: List[str] = []
        for skills in cluster_df[skills_col]:
            if skills:
                # skills should be a list like ["python", "sql"]
                all_skills.extend(skills)

        counts = Counter(all_skills)
        result[cluster] = counts.most_common(top_n)

    return result


def build_cluster_summary(
    df: pd.DataFrame,
    cluster_col: str = "cluster_label",
    skills_col: str = "skills",
    cluster_terms: Optional[Dict[int, List[Tuple[str, float]]]] = None,
    cluster_id_col: str = "cluster",
    top_n_skills: int = 10,
    top_n_terms: int = 10,
) -> pd.DataFrame:
    """
    A2) Build a summary table with:
      - cluster_label
      - job_count
      - top_skills (as a readable string)
      - top_terms  (as a readable string)  [optional if cluster_terms provided]

    cluster_terms format (from your Step 4):
      { cluster_id: [("sql", 0.33), ("python", 0.28), ...] }
    """
    if cluster_col not in df.columns:
        raise ValueError(f"Missing column '{cluster_col}' in df")
    if cluster_id_col not in df.columns:
        raise ValueError(f"Missing column '{cluster_id_col}' in df")

    # job counts per cluster label
    counts_df = (
        df.groupby(cluster_col, dropna=True)
          .size()
          .reset_index(name="job_count")
          .sort_values("job_count", ascending=False)
    )

    # top skills per cluster label
    top_skills_map = top_skills_per_cluster(
        df,
        cluster_col=cluster_col,
        skills_col=skills_col,
        top_n=top_n_skills
    )

    # helper: format list of (item,count) to "item (count), item (count)"
    def format_counts(pairs: List[Tuple[str, int]]) -> str:
        return ", ".join([f"{name} ({cnt})" for name, cnt in pairs])

    counts_df["top_skills"] = counts_df[cluster_col].map(
        lambda c: format_counts(top_skills_map.get(c, []))
    )

    # top terms per cluster (optional)
    if cluster_terms is not None:
        # Map cluster_label -> cluster_id (most common id for that label)
        # (usually 1-to-1, but this avoids edge cases)
        label_to_id = (
            df.groupby(cluster_col)[cluster_id_col]
              .agg(lambda s: s.value_counts().idxmax())
              .to_dict()
        )

        def format_terms(cluster_id: int) -> str:
            pairs = cluster_terms.get(cluster_id, [])[:top_n_terms]
            return ", ".join([t for (t, _) in pairs])

        counts_df["top_terms"] = counts_df[cluster_col].map(
            lambda label: format_terms(label_to_id.get(label, -1))
        )
    else:
        counts_df["top_terms"] = ""

    return counts_df
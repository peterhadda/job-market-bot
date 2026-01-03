import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter


def plot_job_count_by_cluster(summary_df, output_path):
    """
    Bar chart: number of jobs per cluster
    """
    plt.figure(figsize=(10, 6))
    plt.barh(summary_df["cluster_label"], summary_df["job_count"])
    plt.xlabel("Number of jobs")
    plt.ylabel("Cluster")
    plt.title("Job count per cluster")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def plot_top_skills_for_cluster(cluster_label, skill_counts, output_path, top_n=5):
    """
    Bar chart: top skills for ONE cluster
    skill_counts: list of (skill, count)
    """
    skills = [s for s, _ in skill_counts[:top_n]]
    counts = [c for _, c in skill_counts[:top_n]]

    plt.figure(figsize=(8, 5))
    plt.barh(skills, counts)
    plt.xlabel("Frequency")
    plt.title(f"Top skills — {cluster_label}")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

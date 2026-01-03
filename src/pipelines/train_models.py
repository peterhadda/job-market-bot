import pandas as pd
from pathlib import Path
import ast

from src.features.vectorizer import build_tfidf_matrix
from src.models.clustering import train_kmeans, add_clusters_to_df, top_terms_per_cluster
from src.models.clustering import auto_label_clusters, add_cluster_labels_to_df

BASE_DIR = Path(__file__).resolve().parents[2]

INPUT_PATH = BASE_DIR / "data" / "processed" / "jobs_clean.csv"
OUTPUT_PATH = BASE_DIR / "data" / "processed" / "jobs_with_clusters.csv"


def run_train_models():
    # 1) Load your processed data
    df = pd.read_csv(INPUT_PATH)

    # 2) Convert skills from string -> list (if needed)
    if "skills" in df.columns and isinstance(df["skills"].iloc[0], str):
        df["skills"] = df["skills"].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else [])

    # 3) TF-IDF
    X, vectorizer = build_tfidf_matrix(df, text_col="text")

    # 4) Clustering
    model = train_kmeans(X, k=8)
    df = add_clusters_to_df(df, model.labels_, cluster_col="cluster")

    # 5) Cluster terms + auto labels
    cluster_terms = top_terms_per_cluster(model, vectorizer, top_n=12)
    cluster_map = auto_label_clusters(cluster_terms)

    df = add_cluster_labels_to_df(df, cluster_col="cluster", label_col="cluster_label", cluster_id_to_label=cluster_map)

    # 6) Save df (THIS is the part you wanted)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f" Saved clustered jobs to {OUTPUT_PATH}")


if __name__ == "__main__":
    run_train_models()

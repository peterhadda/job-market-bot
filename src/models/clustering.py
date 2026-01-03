from re import X

from sklearn.cluster import KMeans
import numpy as np

LABEL_KEYWORDS = {
    "Data Analyst / BI": {
        "sql", "excel", "power bi", "tableau", "dashboard", "reporting", "kpi", "analysis", "visualization"
    },
    "ML / AI": {
        "pytorch", "tensorflow", "transformers", "deep learning", "machine learning", "nlp",
        "model", "training", "classification", "regression"
    },
    "Data Engineering": {
        "etl", "elt", "airflow", "spark", "kafka", "dbt", "warehouse", "pipeline", "bigquery",
        "snowflake", "redshift"
    },
    "Customer / Business": {
        "customer service", "sales", "client", "communication", "stakeholder", "support",
        "account", "crm", "marketing"
    },
}


def train_kmeans(X, k=8, random_state=42):
    kmeans = KMeans(n_clusters=k, random_state=random_state,n_init="auto")
    kmeans.fit(X)
    return kmeans

def add_clusters_to_df(df, labels, cluster_col="cluster"):
    df[cluster_col] = labels
    return df
def top_terms_per_cluster(model, vectorizer, top_n=10):
    """
    Returns a dict:
      cluster_id -> list of (term, weight)
    """
    terms = vectorizer.get_feature_names_out()
    centers = model.cluster_centers_

    cluster_terms = {}

    for cluster_id, center in enumerate(centers):
        # get indices of top weights
        top_idx = np.argsort(center)[-top_n:][::-1]

        # convert indices to (term, weight)
        cluster_terms[cluster_id] = [(terms[i], float(center[i])) for i in top_idx]

    return cluster_terms

def auto_label_clusters(cluster_terms, label_keywords=LABEL_KEYWORDS, fallback_prefix="Cluster"):
    """
    cluster_terms format:
      { cluster_id: [(term1, weight1), (term2, weight2), ...] }

    Returns:
      { cluster_id: "Label Name" }
    """
    cluster_labels = {}

    for cluster_id, term_weights in cluster_terms.items():
        # keep only terms, normalize to lowercase
        terms = [t.lower() for (t, _) in term_weights]

        best_label = None
        best_score = -1

        for label, keywords in label_keywords.items():
            # score = how many keywords appear in the cluster's top terms
            score = sum(1 for kw in keywords if kw in terms)

            if score > best_score:
                best_score = score
                best_label = label

        # if nothing matched, use fallback
        if best_score <= 0:
            cluster_labels[cluster_id] = f"{fallback_prefix} {cluster_id}"
        else:
            cluster_labels[cluster_id] = best_label

    return cluster_labels

def add_cluster_labels_to_df(df, cluster_col="cluster", label_col="cluster_label", cluster_id_to_label=None):
    if cluster_id_to_label is None:
        raise ValueError("cluster_id_to_label mapping is required")

    df[label_col] = df[cluster_col].map(cluster_id_to_label)
    return df




from sklearn.cluster import KMeans
import numpy as np

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


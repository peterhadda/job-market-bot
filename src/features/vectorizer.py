

from __future__ import annotations

from pathlib import Path
from typing import Tuple, Optional, List

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


def build_tfidf_matrix(
    df: pd.DataFrame,
    text_col: str = "text",
    *,
    max_features: int = 5000,
    ngram_range: Tuple[int, int] = (1, 2),
    stop_words: Optional[str] = "english",
    min_df: int = 2
):
    """
    Build a TF-IDF matrix from a dataframe text column.

    Returns:
      X: sparse TF-IDF matrix (n_jobs x n_features)
      vectorizer: fitted TfidfVectorizer (reusable for new texts)
    """

    # Step 3: validate input column exists
    if text_col not in df.columns:
        raise ValueError(f"Text column '{text_col}' not found in dataframe. Available: {list(df.columns)}")

    # Step 4: prepare texts
    texts = df[text_col].fillna("").astype(str)

    # Step 5: define vectorizer (rules)
    vectorizer = TfidfVectorizer(
        lowercase=True,
        stop_words=stop_words,
        max_features=max_features,
        ngram_range=ngram_range,
        min_df=min_df
    )

    # Step 6: fit + transform
    X = vectorizer.fit_transform(texts)

    # Step 7: return results
    return X, vectorizer


def top_terms_for_row(vectorizer: TfidfVectorizer, X_row, k: int = 10) -> List[Tuple[str, float]]:
    """
    Given a fitted vectorizer and a single row from X (e.g., X[i]),
    return top-k terms with their TF-IDF scores for that row.
    """
    feature_names = vectorizer.get_feature_names_out()

    # X_row is a 1 x n_features sparse row
    coo = X_row.tocoo()
    pairs = [(feature_names[j], float(v)) for j, v in zip(coo.col, coo.data)]
    pairs.sort(key=lambda x: x[1], reverse=True)
    return pairs[:k]





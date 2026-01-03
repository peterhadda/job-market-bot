# src/models/supervised.py

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Any, Tuple

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer


@dataclass
class SupervisedResult:
    model: Pipeline
    metrics: Dict[str, Any]


def train_text_classifier(
    df: pd.DataFrame,
    text_col: str = "text",
    label_col: str = "cluster",
    *,
    test_size: float = 0.2,
    random_state: int = 42,
    max_features: int = 5000,
    ngram_range: Tuple[int, int] = (1, 2),
    min_df: int = 2
) -> SupervisedResult:
    """
    Train a supervised classifier to predict labels from text.
    Default: predict the numeric cluster ID from the job text.

    Returns:
      - sklearn Pipeline (TF-IDF -> LogisticRegression)
      - metrics dict (accuracy + classification report)
    """

    # Validate columns
    if text_col not in df.columns:
        raise ValueError(f"Missing text column: {text_col}")
    if label_col not in df.columns:
        raise ValueError(f"Missing label column: {label_col}")

    # Prepare data
    X = df[text_col].fillna("").astype(str)
    y = df[label_col]

    # Train/test split (stratify keeps label proportions similar)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=test_size,
        random_state=random_state,
        stratify=y
    )

    # Build pipeline: TF-IDF -> classifier
    model = Pipeline(steps=[
        ("tfidf", TfidfVectorizer(
            lowercase=True,
            stop_words="english",
            max_features=max_features,
            ngram_range=ngram_range,
            min_df=min_df
        )),
        ("clf", LogisticRegression(
            max_iter=2000,
            n_jobs=None  # keep default; joblib handles parallelism elsewhere
        ))
    ])

    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    acc = float(accuracy_score(y_test, y_pred))
    report = classification_report(y_test, y_pred, output_dict=True)

    metrics = {
        "accuracy": acc,
        "report": report,
        "n_train": int(len(X_train)),
        "n_test": int(len(X_test)),
        "labels": sorted(list(pd.Series(y).unique()))
    }

    return SupervisedResult(model=model, metrics=metrics)

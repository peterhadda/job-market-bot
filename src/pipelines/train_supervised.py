# src/pipelines/train_supervised.py

import json
from pathlib import Path

import pandas as pd
import joblib

from src.models.supervised import train_text_classifier

BASE_DIR = Path(__file__).resolve().parents[2]

INPUT_PATH = BASE_DIR / "data" / "processed" / "jobs_with_clusters.csv"
MODELS_DIR = BASE_DIR / "data" / "processed" / "models"

MODEL_PATH = MODELS_DIR / "cluster_text_classifier.joblib"
METRICS_PATH = MODELS_DIR / "cluster_text_classifier_metrics.json"


def to_jsonable(obj):
    """
    Recursively convert numpy/pandas scalar types (e.g., int64, float64)
    into native Python types so json.dump() works.
    """
    # numpy/pandas scalars often have .item()
    if hasattr(obj, "item"):
        try:
            return obj.item()
        except Exception:
            pass

    # dict
    if isinstance(obj, dict):
        return {str(k): to_jsonable(v) for k, v in obj.items()}

    # list / tuple
    if isinstance(obj, (list, tuple)):
        return [to_jsonable(x) for x in obj]

    # anything else (str, int, float, None, etc.)
    return obj


def run_train_supervised():
    MODELS_DIR.mkdir(parents=True, exist_ok=True)

    # 1) Load data
    df = pd.read_csv(INPUT_PATH)

    # 2) Train classifier to predict cluster id from text
    result = train_text_classifier(
        df,
        text_col="text",
        label_col="cluster",
        test_size=0.2,
        random_state=42
    )

    # 3) Save model (includes TF-IDF + classifier because it's a Pipeline)
    joblib.dump(result.model, MODEL_PATH)

    # 4) Save metrics safely
    with open(METRICS_PATH, "w", encoding="utf-8") as f:
        json.dump(to_jsonable(result.metrics), f, indent=2)

    print(f"✅ Saved model to: {MODEL_PATH}")
    print(f"✅ Saved metrics to: {METRICS_PATH}")
    print(f"✅ Accuracy: {result.metrics['accuracy']:.4f}")


if __name__ == "__main__":
    run_train_supervised()


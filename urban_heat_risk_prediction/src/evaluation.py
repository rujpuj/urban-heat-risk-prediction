import json
from pathlib import Path

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from src.models import train_model


ROOT = Path(__file__).resolve().parents[1]
METRICS_PATH = ROOT / "results" / "model_metrics.json"


def evaluate_model(metrics_path: Path = METRICS_PATH) -> dict:
    model, x_test, y_test = train_model()
    predictions = model.predict(x_test)

    metrics = {
        "accuracy": round(float(accuracy_score(y_test, predictions)), 4),
        "labels": sorted(y_test.unique().tolist()),
        "confusion_matrix": confusion_matrix(y_test, predictions, labels=sorted(y_test.unique())).tolist(),
        "classification_report": classification_report(y_test, predictions, output_dict=True, zero_division=0),
    }

    metrics_path.parent.mkdir(parents=True, exist_ok=True)
    metrics_path.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    return metrics


if __name__ == "__main__":
    output = evaluate_model()
    print(json.dumps(output, indent=2))

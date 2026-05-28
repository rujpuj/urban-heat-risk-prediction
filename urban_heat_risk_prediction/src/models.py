from pathlib import Path

import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from src.preprocessing import load_dataset, split_features_target


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "raw" / "urban_heat_sample.csv"
MODEL_PATH = ROOT / "results" / "heat_risk_model.joblib"


def build_model(random_state: int = 42) -> Pipeline:
    return Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            (
                "classifier",
                RandomForestClassifier(
                    n_estimators=150,
                    max_depth=6,
                    random_state=random_state,
                    class_weight="balanced",
                ),
            ),
        ]
    )


def train_model(data_path: Path = DATA_PATH, model_path: Path = MODEL_PATH):
    data = load_dataset(data_path)
    features, target = split_features_target(data)
    x_train, x_test, y_train, y_test = train_test_split(
        features,
        target,
        test_size=0.25,
        random_state=42,
        stratify=target,
    )

    model = build_model()
    model.fit(x_train, y_train)
    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, model_path)
    return model, x_test, y_test


if __name__ == "__main__":
    train_model()
    print(f"Model saved to {MODEL_PATH}")

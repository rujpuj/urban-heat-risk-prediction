from pathlib import Path

import pandas as pd


FEATURE_COLUMNS = [
    "average_temperature",
    "max_temperature",
    "night_temperature",
    "population_density",
    "elderly_population_pct",
    "children_population_pct",
    "tree_cover_pct",
    "concrete_surface_pct",
    "distance_to_cooling_center_km",
    "median_income_usd",
    "hospital_distance_km",
    "historical_heat_cases",
]

TARGET_COLUMN = "heat_risk_level"


def load_dataset(path: str | Path) -> pd.DataFrame:
    """Load the heat-risk dataset and validate required columns."""
    data = pd.read_csv(path)
    missing = set(FEATURE_COLUMNS + [TARGET_COLUMN]) - set(data.columns)
    if missing:
        raise ValueError(f"Dataset is missing required columns: {sorted(missing)}")
    return data


def clean_dataset(data: pd.DataFrame) -> pd.DataFrame:
    """Return a cleaned dataframe with numeric features and no missing values."""
    cleaned = data.copy()
    for column in FEATURE_COLUMNS:
        cleaned[column] = pd.to_numeric(cleaned[column], errors="coerce")
        cleaned[column] = cleaned[column].fillna(cleaned[column].median())
    cleaned[TARGET_COLUMN] = cleaned[TARGET_COLUMN].astype(str)
    return cleaned


def split_features_target(data: pd.DataFrame):
    """Split dataframe into model features and target."""
    cleaned = clean_dataset(data)
    return cleaned[FEATURE_COLUMNS], cleaned[TARGET_COLUMN]

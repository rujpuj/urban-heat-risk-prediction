from pathlib import Path

from src.preprocessing import FEATURE_COLUMNS, TARGET_COLUMN, load_dataset, split_features_target


def test_load_dataset_has_required_columns():
    path = Path("data/raw/urban_heat_sample.csv")
    data = load_dataset(path)

    for column in FEATURE_COLUMNS + [TARGET_COLUMN]:
        assert column in data.columns


def test_split_features_target_shapes_match():
    path = Path("data/raw/urban_heat_sample.csv")
    data = load_dataset(path)
    features, target = split_features_target(data)

    assert len(features) == len(target)
    assert list(features.columns) == FEATURE_COLUMNS

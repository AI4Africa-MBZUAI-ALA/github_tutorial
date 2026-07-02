from __future__ import annotations

from typing import Any, Dict


def preprocess_event_data(raw_bundle: Dict[str, Any]) -> Dict[str, Any]:
    """
    Turn raw records into trainable data.

    Input contract:
    - raw_bundle["dataset_name"]: str
    - raw_bundle["source"]: str
    - raw_bundle["records"]: list[dict]

    Expected work:
    - clean missing values
    - normalize text fields
    - convert categories into model-friendly features
    - split the data into train and test rows

    Output contract:
    - dataset_name: str
    - feature_names: list[str]
    - target_name: str  # likely "water_need"
    - train_rows: list[dict]
    - test_rows: list[dict]
    - summary: dict
    """
    raise NotImplementedError(
        "preprocess_event_data is not implemented yet. "
        "This is the group task for the preprocessing team."
    )

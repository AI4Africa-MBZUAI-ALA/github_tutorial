from __future__ import annotations

from typing import Any, Dict


def train_model(processed_bundle: Dict[str, Any]) -> Dict[str, Any]:
    """
    Fit a model on the training rows.

    Input contract:
    - processed_bundle["dataset_name"]: str
    - processed_bundle["feature_names"]: list[str]
    - processed_bundle["target_name"]: str
    - processed_bundle["train_rows"]: list[dict]
    - processed_bundle["test_rows"]: list[dict]

    Expected work:
    - pick a simple model first
    - train it on the training rows
    - store anything needed for evaluation later

    Tip:
    - a small decision tree or logistic regression is enough for this workshop

    Output contract:
    - dataset_name: str
    - feature_names: list[str]
    - target_name: str
    - train_rows: list[dict]
    - test_rows: list[dict]
    - model: object
    - training_summary: dict
    """
    raise NotImplementedError(
        "train_model is not implemented yet. "
        "This is the group task for the training team."
    )

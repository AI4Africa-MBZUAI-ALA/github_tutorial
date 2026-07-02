from __future__ import annotations

from typing import Any, Dict


def evaluate_model(trained_bundle: Dict[str, Any]) -> Dict[str, Any]:
    """
    Measure how good the model is.

    Input contract:
    - trained_bundle["dataset_name"]: str
    - trained_bundle["feature_names"]: list[str]
    - trained_bundle["target_name"]: str
    - trained_bundle["train_rows"]: list[dict]
    - trained_bundle["test_rows"]: list[dict]
    - trained_bundle["model"]: object

    Expected work:
    - create predictions for the test set
    - compare predictions with the true labels
    - calculate at least one useful metric

    Tip:
    - accuracy plus a confusion matrix is enough for the first version

    Output contract:
    - dataset_name: str
    - feature_names: list[str]
    - target_name: str
    - train_rows: list[dict]
    - test_rows: list[dict]
    - model: object
    - metrics: dict
    - sample_predictions: list[dict]
    - confusion_matrix: list[list[int]]
    """
    raise NotImplementedError(
        "evaluate_model is not implemented yet. "
        "This is the group task for the evaluation team."
    )

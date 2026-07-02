from __future__ import annotations

from typing import Any, Dict


def create_visual_report(evaluation_bundle: Dict[str, Any]) -> Dict[str, Any]:
    """
    Turn model results into plots and visual summaries.

    Input contract:
    - evaluation_bundle["dataset_name"]: str
    - evaluation_bundle["metrics"]: dict
    - evaluation_bundle["sample_predictions"]: list[dict]
    - evaluation_bundle["confusion_matrix"]: list[list[int]]

    Expected work:
    - create at least one plot with matplotlib or seaborn
    - save the figure to disk
    - prepare chart notes for the dashboard step

    Tip:
    - confusion matrix plots work well for beginners

    Output contract:
    - dataset_name: str
    - metrics: dict
    - figure_paths: list[str]
    - chart_notes: list[str]
    - sample_predictions: list[dict]
    """
    raise NotImplementedError(
        "create_visual_report is not implemented yet. "
        "This is the group task for the visualization team."
    )

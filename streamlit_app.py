from __future__ import annotations

from typing import Any, Dict


def build_streamlit_dashboard(visual_bundle: Dict[str, Any]) -> Dict[str, Any]:
    """
    Prepare the data that a Streamlit app will render.

    Input contract:
    - visual_bundle["dataset_name"]: str
    - visual_bundle["metrics"]: dict
    - visual_bundle["figure_paths"]: list[str]
    - visual_bundle["chart_notes"]: list[str]
    - visual_bundle["sample_predictions"]: list[dict]

    Expected work:
    - build the layout for a Streamlit page
    - show the metrics
    - show the saved plots
    - show a small table of predictions

    Tip:
    - keep the page simple and visual first

    Output contract:
    - dataset_name: str
    - title: str
    - metrics: dict
    - figure_paths: list[str]
    - widgets: list[str]
    - sample_predictions: list[dict]
    """
    raise NotImplementedError(
        "build_streamlit_dashboard is not implemented yet. "
        "This is the group task for the Streamlit team."
    )

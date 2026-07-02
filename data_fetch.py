from __future__ import annotations

from typing import Any, Dict


def fetch_event_data(config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Create or load the controlled synthetic dataset for the workshop pipeline.

    Input contract:
    - config["dataset_name"]: human-friendly name for the dataset.
    - config["source"]: should be the string "synthetic" for this starter repo.
    - config["limit"]: optional maximum number of rows to keep.

    Output contract:
    - dataset_name: str
    - source: str
    - records: list[dict]
    - notes: list[str]

    Suggested beginner story:
    - use a fictional school garden / community farm story
    - keep one row per weather-and-soil observation
    - do not change the output keys
    """
    raise NotImplementedError(
        "fetch_event_data is not implemented yet. "
        "This is the group task for the data-fetching team."
    )

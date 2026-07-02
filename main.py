from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
from typing import Any, Callable, Dict, List


BASE_DIR = Path(__file__).resolve().parent


STEP_SPECS = [
    {
        "label": "Data fetching",
        "file_path": "to_complete/01_data_fetch.py",
        "function": "fetch_event_data",
        "sample_input": {
            "dataset_name": "school_garden_water_need",
            "source": "synthetic",
            "limit": 5,
        },
        "required_keys": ["dataset_name", "source", "records", "notes"],
    },
    {
        "label": "Preprocessing",
        "file_path": "to_complete/02_preprocess.py",
        "function": "preprocess_event_data",
        "sample_input": {
            "dataset_name": "school_garden_water_need",
            "source": "synthetic",
            "records": [
                {
                    "day_of_week": "Monday",
                    "weather": "sunny",
                    "temperature_c": 31,
                    "rainfall_mm": 0,
                    "soil_moisture": 18,
                    "crop_type": "maize",
                    "water_need": "high",
                },
                {
                    "day_of_week": "Wednesday",
                    "weather": "rainy",
                    "temperature_c": 24,
                    "rainfall_mm": 18,
                    "soil_moisture": 61,
                    "crop_type": "beans",
                    "water_need": "low",
                },
                {
                    "day_of_week": "Friday",
                    "weather": "cloudy",
                    "temperature_c": 27,
                    "rainfall_mm": 4,
                    "soil_moisture": 36,
                    "crop_type": "tomato",
                    "water_need": "medium",
                },
            ],
        },
        "required_keys": ["dataset_name", "train_rows", "test_rows", "feature_names", "target_name"],
    },
    {
        "label": "Training",
        "file_path": "to_complete/03_train.py",
        "function": "train_model",
        "sample_input": {
            "dataset_name": "school_garden_water_need",
            "feature_names": ["day_of_week", "weather", "temperature_c", "rainfall_mm", "soil_moisture", "crop_type"],
            "target_name": "water_need",
            "train_rows": [
                {
                    "day_of_week": "Monday",
                    "weather": "sunny",
                    "temperature_c": 31,
                    "rainfall_mm": 0,
                    "soil_moisture": 18,
                    "crop_type": "maize",
                    "water_need": "high",
                },
                {
                    "day_of_week": "Tuesday",
                    "weather": "rainy",
                    "temperature_c": 23,
                    "rainfall_mm": 15,
                    "soil_moisture": 58,
                    "crop_type": "beans",
                    "water_need": "low",
                },
            ],
            "test_rows": [
                {
                    "day_of_week": "Friday",
                    "weather": "cloudy",
                    "temperature_c": 27,
                    "rainfall_mm": 4,
                    "soil_moisture": 36,
                    "crop_type": "tomato",
                    "water_need": "medium",
                }
            ],
        },
        "required_keys": ["dataset_name", "model", "training_summary", "train_rows", "test_rows"],
    },
    {
        "label": "Evaluation",
        "file_path": "to_complete/04_evaluate.py",
        "function": "evaluate_model",
        "sample_input": {
            "dataset_name": "school_garden_water_need",
            "feature_names": ["day_of_week", "weather", "temperature_c", "rainfall_mm", "soil_moisture", "crop_type"],
            "target_name": "water_need",
            "model": {"kind": "placeholder"},
            "train_rows": [
                {
                    "day_of_week": "Monday",
                    "weather": "sunny",
                    "temperature_c": 31,
                    "rainfall_mm": 0,
                    "soil_moisture": 18,
                    "crop_type": "maize",
                    "water_need": "high",
                }
            ],
            "test_rows": [
                {
                    "day_of_week": "Friday",
                    "weather": "cloudy",
                    "temperature_c": 27,
                    "rainfall_mm": 4,
                    "soil_moisture": 36,
                    "crop_type": "tomato",
                    "water_need": "medium",
                }
            ],
        },
        "required_keys": ["dataset_name", "metrics", "sample_predictions", "confusion_matrix"],
    },
    {
        "label": "Visualization",
        "file_path": "to_complete/05_visualize.py",
        "function": "create_visual_report",
        "sample_input": {
            "dataset_name": "school_garden_water_need",
            "metrics": {"accuracy": 0.75, "precision": 0.70, "recall": 0.80},
            "confusion_matrix": [[8, 2], [1, 9]],
            "sample_predictions": [
                {"actual": "high", "predicted": "high"},
                {"actual": "low", "predicted": "low"},
            ],
        },
        "required_keys": ["dataset_name", "figure_paths", "chart_notes"],
    },
    {
        "label": "Streamlit dashboard",
        "file_path": "to_complete/06_streamlit_app.py",
        "function": "build_streamlit_dashboard",
        "sample_input": {
            "dataset_name": "school_garden_water_need",
            "title": "School Garden Water Need Dashboard",
            "metrics": {"accuracy": 0.75, "precision": 0.70, "recall": 0.80},
            "figure_paths": ["artifacts/plots/confusion_matrix.png"],
            "chart_notes": ["Show the confusion matrix", "Show a metric summary"],
            "sample_predictions": [
                {"actual": "high", "predicted": "high"},
                {"actual": "low", "predicted": "low"},
            ],
        },
        "required_keys": ["dataset_name", "title", "metrics", "figure_paths", "widgets"],
    },
]


def load_step(file_path: str, function_name: str) -> Callable[[Dict[str, Any]], Any]:
    full_path = BASE_DIR / file_path
    if not full_path.exists():
        raise ModuleNotFoundError(f"Could not load step file at {full_path}")

    module_name = f"step_{full_path.stem.replace('-', '_')}"
    spec = importlib.util.spec_from_file_location(module_name, full_path)
    if spec is None or spec.loader is None:
        raise ModuleNotFoundError(f"Could not load step file at {full_path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    function = getattr(module, function_name)
    return function


def validate_output(step_label: str, output: Any, required_keys: List[str]) -> List[str]:
    issues: List[str] = []
    if not isinstance(output, dict):
        return [f"{step_label}: expected a dict, got {type(output).__name__}"]

    missing = [key for key in required_keys if key not in output]
    if missing:
        issues.append(f"{step_label}: missing keys {missing}")

    return issues


def smoke_test_step(step_spec: Dict[str, Any]) -> Dict[str, Any]:
    result: Dict[str, Any] = {
        "label": step_spec["label"],
        "file_path": step_spec["file_path"],
        "function": step_spec["function"],
        "status": "not run",
        "details": "",
    }

    try:
        step_fn = load_step(step_spec["file_path"], step_spec["function"])
    except ModuleNotFoundError:
        result["status"] = "missing"
        result["details"] = f"file {step_spec['file_path']} could not be imported"
        return result
    except AttributeError:
        result["status"] = "missing"
        result["details"] = f"function {step_spec['function']} was not found in {step_spec['file_path']}"
        return result

    try:
        output = step_fn(step_spec["sample_input"])
    except NotImplementedError as exc:
        result["status"] = "stub"
        result["details"] = str(exc)
        return result
    except Exception as exc:
        result["status"] = "error"
        result["details"] = f"{type(exc).__name__}: {exc}"
        return result

    issues = validate_output(step_spec["label"], output, step_spec["required_keys"])
    if issues:
        result["status"] = "invalid"
        result["details"] = "; ".join(issues)
        return result

    result["status"] = "ok"
    result["details"] = "contract looks good"
    result["output"] = output
    return result


def print_report(results: List[Dict[str, Any]]) -> None:
    print("Workshop pipeline status")
    print("------------------------")
    for result in results:
        print(f"{result['label']}: {result['status']} - {result['details']}")


def run_pipeline() -> int:
    results = [smoke_test_step(step_spec) for step_spec in STEP_SPECS]
    print_report(results)

    hard_failures = [result for result in results if result["status"] in {"error", "invalid"}]
    stubs = [result for result in results if result["status"] in {"missing", "stub"}]

    if hard_failures:
        print()
        print("Some steps are implemented incorrectly. Fix the contract or the runtime error.")
        return 1

    if stubs:
        print()
        print("Some steps are still waiting for implementation. That is expected for the starter repo.")
        return 0

    print()
    print("All steps are implemented. The full pipeline contract is ready.")
    return 0


def main() -> int:
    return run_pipeline()


if __name__ == "__main__":
    sys.exit(main())

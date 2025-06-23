"""
write_status_yaml.py

Write a status.yaml file with timestamps or error messages for each fetch task.
Can be called with an optional JSON file as an argument to track actual results.
"""

import json
import sys
from pathlib import Path

import yaml
from civic_lib_core.date_utils import now_utc_str

STATUS_PATH = Path("docs/status.yaml")
TIMESTAMP = now_utc_str()


def main():
    # Default structure
    status = {"last_updated": TIMESTAMP, "fetch": {}}

    # Optional: load JSON summary of fetch results
    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1])
        if input_path.exists():
            with input_path.open("r", encoding="utf-8") as f:
                results = json.load(f)
                for task, outcome in results.items():
                    if isinstance(outcome, dict):
                        status["fetch"][task] = outcome
                    else:
                        status["fetch"][task] = {"error": str(outcome)}
        else:
            print(f"Warning: {input_path} not found. Writing default timestamps.")

    # Fallback if no input provided
    if not status["fetch"]:
        for task in ["boundaries", "congressional_districts", "roles", "states"]:
            status["fetch"][task] = {"timestamp": TIMESTAMP}

    STATUS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with STATUS_PATH.open("w", encoding="utf-8") as f:
        yaml.dump(status, f, sort_keys=False)

    print(f"Wrote status to {STATUS_PATH}")


if __name__ == "__main__":
    main()

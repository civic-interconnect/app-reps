"""
fetch_roles.py

Create placeholder roles and people data for Civic Interconnect.
"""

import json
from pathlib import Path

from civic_lib_core import log_utils
from civic_lib_core.date_utils import today_utc_str
from civic_lib_core.path_utils import ensure_dir

log_utils.init_logger()
logger = log_utils.logger

OUTPUT_PATH = Path("data/people/roles.json")


def fetch_roles_data():
    logger.info("Fetching roles and people...")

    try:
        ensure_dir(OUTPUT_PATH.parent)
        placeholder = {
            "generated": today_utc_str(),
            "roles": [
                {"name": "Governor", "state": "MN"},
                {"name": "Senator", "state": "MN"},
            ],
        }
        OUTPUT_PATH.write_text(json.dumps(placeholder, indent=2))
        logger.info(f"Placeholder roles written to {OUTPUT_PATH}")

    except Exception as e:
        logger.error(f"Error writing roles data: {e}")
        raise RuntimeError("Failed to create roles placeholder data.") from e


def main():
    try:
        fetch_roles_data()
    except Exception as e:
        logger.error(f"Fetch roles failed: {e}")
        raise SystemExit(1) from e


if __name__ == "__main__":
    main()

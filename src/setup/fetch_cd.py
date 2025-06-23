"""
fetch_cd.py

Fetch and store U.S. congressional district GeoJSON from the Civic Data Boundaries repo.
"""

from pathlib import Path

import requests
from civic_lib_core import log_utils
from civic_lib_core.path_utils import ensure_dir

log_utils.init_logger()
logger = log_utils.logger

URL = "https://raw.githubusercontent.com/civic-interconnect/civic-data-boundaries-us/main/data/congress/us-congressional-districts.geojson"
OUTPUT_PATH = Path("data/boundaries/congressional_districts.geojson")


def fetch_congressional_districts():
    logger.info("Fetching Congressional District boundaries...")
    try:
        ensure_dir(OUTPUT_PATH.parent)
        response = requests.get(URL, timeout=10)

        if response.status_code == 200:
            OUTPUT_PATH.write_text(response.text)
            logger.info(f"Fetched and saved to {OUTPUT_PATH}")
        else:
            logger.warning(f"Unexpected response code {response.status_code} from {URL}")
            raise RuntimeError(f"Failed to fetch data: HTTP {response.status_code}")

    except requests.exceptions.RequestException as e:
        logger.error(f"Network error fetching CD boundaries: {e}")
        raise RuntimeError("Unable to fetch congressional district boundaries.") from e

    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise RuntimeError("Unexpected error while fetching congressional districts.") from e


def main():
    try:
        fetch_congressional_districts()
    except Exception as e:
        logger.error(f"Fetch CD failed: {e}")
        raise SystemExit(1) from e


if __name__ == "__main__":
    main()

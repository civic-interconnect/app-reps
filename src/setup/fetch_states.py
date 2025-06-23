"""
fetch_states.py

Fetch and store metadata about U.S. states from the Civic Data Boundaries repo.
"""

from pathlib import Path

import requests
from civic_lib_core import log_utils
from civic_lib_core.path_utils import ensure_dir

log_utils.init_logger()
logger = log_utils.logger

# URL for national-level states GeoJSON metadata
URL = "https://github.com/civic-interconnect/civic-data-boundaries-us/raw/refs/heads/main/data/national/us-states.geojson"

OUTPUT_PATH = Path("data/states/us-states.json")


def fetch_us_states_metadata():
    logger.info("Fetching US states metadata...")
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
        logger.error(f"Network error fetching states metadata: {e}")
        raise RuntimeError("Unable to fetch US states metadata.") from e

    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise RuntimeError("Unexpected error while fetching states metadata.") from e


def main():
    try:
        fetch_us_states_metadata()
    except Exception as e:
        logger.error(f"Fetch states failed: {e}")
        raise SystemExit(1) from e


if __name__ == "__main__":
    main()

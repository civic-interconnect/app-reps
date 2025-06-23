"""
fetch_boundaries.py

Fetch and save US state boundary GeoJSON data.
"""

from pathlib import Path

import requests
from civic_lib_core import log_utils
from civic_lib_core.path_utils import ensure_dir

log_utils.init_logger()
logger = log_utils.logger

# URL to public raw file in civic-data-boundaries-us repo
URL = "https://raw.githubusercontent.com/civic-interconnect/civic-data-boundaries-us/main/data/national/us-states.geojson"
OUTPUT_PATH = Path("data/boundaries/us-states.geojson")


def fetch_us_state_boundaries():
    logger.info("Fetching US state boundary GeoJSON...")
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
        logger.error(f"Network error fetching boundaries: {e}")
        raise RuntimeError("Unable to fetch boundaries due to network error.") from e

    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise RuntimeError("Unexpected error while fetching boundaries.") from e


def main():
    try:
        fetch_us_state_boundaries()
    except Exception as e:
        logger.error(f"Fetch boundaries failed: {e}")
        raise SystemExit(1) from e


if __name__ == "__main__":
    main()

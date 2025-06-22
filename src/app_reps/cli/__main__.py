"""
app_reps.__main__

Entrypoint for running the CLI with:

py -m app_reps
python -m app_reps
python3 -m app_reps

Usage depends on your operating system and Python installation.
"""

from app_reps.cli.cli import app

if __name__ == "__main__":
    app()

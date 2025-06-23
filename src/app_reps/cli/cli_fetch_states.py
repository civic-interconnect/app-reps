"""
cli_fetch_states.py

Update application data files for Civic Interconnect agents.

This command runs update scripts or functions responsible for refreshing
data files (e.g., JSON, YAML) used by the application.

Intended for manual or scheduled use to ensure data freshness.
"""

import typer

from setup import fetch_states

app = typer.Typer(help="Update local JSON and structured data files.")


@app.command("fetch-states")
def main():
    """
    Run update tasks to refresh app data.
    """
    typer.echo("Fetching states data...")
    try:
        fetch_states.main()
        typer.echo("Fetch states complete.")
    except Exception as e:
        typer.echo(f"Error during fetch-states: {e}")
        raise typer.Exit(1) from e


if __name__ == "__main__":
    main()

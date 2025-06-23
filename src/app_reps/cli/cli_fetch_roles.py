"""
cli_fetch_roles.py

Update application data files for Civic Interconnect agents.

This command runs update scripts or functions responsible for refreshing
data files (e.g., JSON, YAML) used by the application.

Intended for manual or scheduled use to ensure data freshness.
"""

import typer

from setup import fetch_roles

app = typer.Typer(help="Update local JSON and structured data files.")


@app.command("fetch-roles")
def main():
    """
    Run update tasks to refresh app data.
    """
    typer.echo("Fetching roles data...")
    try:
        fetch_roles.main()
        typer.echo("Fetch roles complete.")
    except Exception as e:
        typer.echo(f"Error during fetch-roles: {e}")
        raise typer.Exit(1) from e


if __name__ == "__main__":
    main()

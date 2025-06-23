"""
cli.py

Command-line interface (CLI) for this repository.

Provides developer-facing commands to:
- Set up and verify the local development environment
- Format, lint, and test the codebase
- Bump version numbers for release
- Perform release steps including tagging and pushing
- Start the application locally
- Update data artifacts (e.g., JSON summaries)

Run `app-reps --help` for full usage details.
"""

import typer

from . import (
    bump_version,
    cli_fetch_boundaries,
    cli_fetch_cd,
    cli_fetch_roles,
    cli_fetch_states,
    prep_code,
    release,
    serve_app,
)

app = typer.Typer(help="App Reps CLI")


def wrap_fetch(cli_module, label: str):
    @app.command(label)
    def _command():
        cli_module.main()


wrap_fetch(cli_fetch_boundaries, "fetch-boundaries")
wrap_fetch(cli_fetch_cd, "fetch-cd")
wrap_fetch(cli_fetch_roles, "fetch-roles")
wrap_fetch(cli_fetch_states, "fetch-states")


@app.command("bump-version")
def bump_version_command(old_version: str, new_version: str):
    """
    Update version strings across the project.
    """
    bump_version.main(old_version, new_version)


@app.command("prep-code")
def prepare_code():
    """
    Format, lint, and test the codebase.
    """
    prep_code.main()


@app.command("release")
def release_command():
    """
    Tag and push the current version to GitHub.
    """
    release.main()


@app.command("serve-app")
def serve_local_app():
    """
    Start the application locally for development or preview.
    """
    serve_app.main()


def main():
    app()


if __name__ == "__main__":
    main()

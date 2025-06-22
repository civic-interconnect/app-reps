"""
tests/test_cli_cli.py

Basic tests for the app_reps CLI.
"""

from typer.testing import CliRunner

from app_reps.cli.cli import app

runner = CliRunner()


def test_cli_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "App Reps CLI" in result.output
    assert "bump-version" in result.output

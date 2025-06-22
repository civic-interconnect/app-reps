# DEVELOPER.md

## Setup

First, fork the repo. Git clone your repo to your machine. Open project repo in VS Code.
Open a terminal (commands are for PowerShell).

```powershell
git clone https://github.com/civic-interconnect/app-reps.git
cd app-reps
py -m venv .venv
.\.venv\Scripts\activate
py src\setup\init_venv.py
app-reps prep-code
app-reps serve-app
```

or serve with:

```powershell
cd docs
py -m http.server 8000
```

Visit: <http://localhost:8000>

## Releasing New Version

After verifying changes:

```powershell
app-reps bump-version 0.0.0 0.0.1
app-reps release
```

## Publishing to PyPI

Requires valid PyPI token:

```powershell
py -m build
py -m twine upload dist/*
```

## Test Web App Locally

```powershell
cd docs
py -m http.server 8000
```

Visit: <http://localhost:8000>

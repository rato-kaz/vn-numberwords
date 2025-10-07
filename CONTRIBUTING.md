# Contributing

Thanks for contributing to vn-numberwords!

## Development setup

```bash
python -m venv .venv
. .venv/Scripts/activate  # Windows PowerShell: .venv\\Scripts\\Activate.ps1
pip install -e .[dev]
pre-commit install
```

## Running checks

```bash
ruff check . && ruff format --check .
pytest -q
```

## Commit style

- Use conventional commits (feat, fix, docs, refactor, test, chore).

## Release

- Bump version in `vn_numberwords/__init__.py` and `pyproject.toml`.
- Update `CHANGELOG.md`.
- Tag: `git tag vX.Y.Z && git push --tags`.

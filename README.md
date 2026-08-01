# Advanced Hello World Backend Core

Reusable Django application providing the message model, REST API, validation,
migrations, and health endpoints for Advanced Hello World.

## Development

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -e '.[dev]'
ruff format --check .
ruff check .
pytest
python -m build
twine check dist/*
```

The package deliberately contains no Django project or deployment settings. It
must be installed into an assembler such as `advanced-hello-world-be`.


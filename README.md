# Advanced Hello World Backend Core

Reusable Django package containing shared module contracts and operational
health endpoints. Feature models and APIs live in independently versioned
modules. The package deliberately contains no Django project, deployment
settings, or web server; those belong to the
[backend assembler](https://github.com/YutakaX17/advanced-hello-world-be).

## What it provides

- `/api/v1/health/live` and `/api/v1/health/ready`
- a reusable Django app named `advanced_hello_world_core`
- a validated `BackendModule` contract for independently installed features
- inline type information for strict checking by downstream packages
- historical migrations that preserve databases created before feature
  extraction

Message persistence and `/api/v1/messages` are provided by
[the messages module](https://github.com/YutakaX17/advanced-hello-world-be-messages).

## Requirements

- Git
- Python 3.12 or newer
- PostgreSQL only when this package is used by the backend assembler
- Docker Engine with Compose only for the complete containerized application

## Native development

```bash
git clone https://github.com/YutakaX17/advanced-hello-world-be-core.git
cd advanced-hello-world-be-core
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
```

Run the same quality checks used by CI:

```bash
ruff format --check .
ruff check .
mypy src
pytest
python -m build
twine check dist/*
pip-audit
```

This `.venv` is an optional, disposable contributor environment for testing the
core package alone. It is not the assembled application's runtime. The test
suite supplies a minimal Django project and uses an in-memory SQLite database.
Application development and integration against PostgreSQL use the backend
assembler's `.venv`.

## Use from a sibling backend checkout

Clone both repositories into the same parent directory:

```text
workspace/
├── advanced-hello-world-be-core/
└── advanced-hello-world-be/
```

The backend manifest installer will manage this automatically. For direct
package development, install the core into the assembler's environment:

```bash
cd advanced-hello-world-be
. .venv/bin/activate
python -m pip install -e ../advanced-hello-world-be-core
```

## Docker setup

This library does not publish a standalone service image. The backend assembler
installs it when building the deployable image. For the complete Docker setup,
including PostgreSQL, migrations, backend, and frontend, use the
[distribution repository](https://github.com/YutakaX17/advanced-hello-world).

## Releases and security

Tags follow Semantic Versioning. Releases contain Python package archives, an
SPDX SBOM, and SHA-256 checksums. Pull requests run formatting, linting, strict
typing, tests with a 90% coverage threshold, package validation, dependency
audit, dependency review, CodeQL, secret scanning, and vulnerability scanning.

See [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md), and the
[release page](https://github.com/YutakaX17/advanced-hello-world-be-core/releases).

## Repository family

- [Backend assembler](https://github.com/YutakaX17/advanced-hello-world-be)
- [Backend messages module](https://github.com/YutakaX17/advanced-hello-world-be-messages)
- [Frontend core](https://github.com/YutakaX17/advanced-hello-world-fe-core)
- [Frontend assembler](https://github.com/YutakaX17/advanced-hello-world-fe)
- [All-in-one distribution](https://github.com/YutakaX17/advanced-hello-world)

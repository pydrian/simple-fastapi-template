# FastAPI Versioned API Template

This is a template project demonstrating how to structure a versioned REST API using FastAPI.

## Features

- Multiple API versions (v1, v2, v3) with separate documentation
- Poetry for dependency management
- Type checking with mypy
- Testing with pytest

## Getting Started

1. Install dependencies:
```bash
make install  ## or poetry install
```

2. Run the application:
```bash
make run  ## or poetry run uvicorn api.main:app --reload
```

3. Run tests:
```bash
make test  ## or poetry run pytest
```

4. Run type checking:
```bash
make mypy .  ## or poetry run mypy .
```

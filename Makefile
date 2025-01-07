run:  ## Run the FastAPI application with hot reload
	poetry run uvicorn api.main:app --reload

test:  ## Run pytest tests
	poetry run pytest

lint:  ## Run mypy type checking
	poetry run mypy .

install:  ## Install poetry dependencies
	poetry install

help:  ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

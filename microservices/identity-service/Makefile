.DEFAULT_GOAL := check

.PHONY: docker-build lint format test check check-ci

docker-build:
	docker build --tag identity-service:local .

lint:
	ruff check .
	ruff format --check .

format:
	ruff format .
	ruff check --fix .

test:
	pytest

check: lint test

check-ci:
	ruff check .
	ruff format --check .
	pytest

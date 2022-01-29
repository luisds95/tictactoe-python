install:
	poetry install

lint:
	poetry run black tictactoe tests
	poetry run isort tictactoe tests
	poetry run python -m flake8 tictactoe tests
	poetry run mypy tictactoe tests

test:
	poetry run pytest tests

precommit: lint test

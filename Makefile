install:
	poetry install

lint:
	black tictactoe tests
	isort tictactoe tests
	python -m flake8 tictactoe tests
	mypy tictactoe

test:
	pytest tests

precommit: lint test
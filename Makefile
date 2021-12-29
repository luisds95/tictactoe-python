install:
	poetry install

lint:
	black tictactoe
	isort tictactoe
	python -m flake8 tictactoe
	mypy tictactoe

test:
	pytest tests

precommit: lint test
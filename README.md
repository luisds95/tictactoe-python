# tictactoe-python
Tic-Tac-Toe solved with Reinforcement Learning in Python!

## Pre-requisites
To play TicTacToe, you must have installed:

- [Python ^3.9](https://www.python.org/)
- [Poetry](https://python-poetry.org/docs/master/)

## Installation
To install, simply run `make install`. 

Alternatively, run `poetry install`. 

You can verify your installation with `make test`.

That's it 🐱‍👤.

## Usage
When activating the environment (by running `poetry shell`, or alternatively, prefixing every command with `poetry run`) the `tictactoe` CLI will be available. The CLI expects you to provide the name of the two agents that will be playing, valid names are: human, random and searcher. 

See `tictactoe --help` to get more details.

### Quick start examples
Train the [ExhaustiveSearch](tictactoe/agent/searcher.py) agent:

`tictactoe searcher --train`

Play against the searcher (you first):

`tictactoe human searcher`

Play against the searcher (searcher first):

`tictactoe searcher human`

Play against a [random agent](tictactoe/agent/random.py):

`tictactoe human random`

Watch the searcher playing against itself:

`tictactoe searcher searcher --loud`

Get the output of 10 games of the random agent against the searcher:

`tictactoe random searcher --n-games 10`
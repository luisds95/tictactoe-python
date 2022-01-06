import pytest

from tictactoe.agent.random import RandomAgent
from tictactoe.game.board import Board


@pytest.fixture
def agent():
    return RandomAgent()


@pytest.mark.parametrize("state", ["121212000", "121201212"])
def test_agent_returns_possible_actions(state: str, agent: RandomAgent):
    board = Board(state)
    action = agent.get_action(board)
    assert board.is_valid_move(action)

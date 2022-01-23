import pytest

from tictactoe.agent.random import RandomAgent
from tictactoe.environment.board import Board


@pytest.fixture
def agent():
    return RandomAgent()


@pytest.mark.parametrize("state", ["000000000", "121212000", "121201212"])
def test_agent_returns_possible_actions(state: str, agent: RandomAgent):
    board = Board(state)
    for _ in range(10):
        action = agent.get_action(board)
        assert board.is_valid_move(action)

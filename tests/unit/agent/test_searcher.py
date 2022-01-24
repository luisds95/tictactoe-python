from typing import Dict
import pytest

from tictactoe.agent.searcher import ExhaustiveSearchAgent
from tictactoe.environment import Board


@pytest.mark.parametrize(
    "state,expected",
    [
        ["112002000", {3: -1, 4: -1, 6: -1, 7: -1, 8: 1}]
    ]
)
def test_searcher_evaluates_moves_correctly(state: str, expected: Dict[int, int]):
    agent = ExhaustiveSearchAgent("1")
    board = Board(state)

    values = agent.evaluate_moves(board, max_depth=1)

    assert values == expected
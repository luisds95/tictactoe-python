from typing import Dict

import pytest

from tictactoe.agent.searcher import ExhaustiveSearchAgent
from tictactoe.environment import Board


@pytest.mark.parametrize(
    "state,expected",
    [
        ["112122000", {6: 1, 7: -1, 8: -1}],
        ["010221120", {0: 0, 2: 1, 8: 0}],
        ["010221100", {0: -1, 2: 0, 7: -1, 8: 0}],
        ["010221000", {0: 0, 2: 1, 6: 0, 7: -1, 8: 0}],
    ],
)
def test_exhaustive_search_agent_evaluates_moves_correctly(
    state: str, expected: Dict[int, int]
):
    board = Board(state)
    agent = ExhaustiveSearchAgent(board.next_player)

    values = agent.evaluate_moves(board)

    assert values == expected


@pytest.mark.parametrize(
    "state,expected",
    [
        ["112122000", 6],
        ["010221120", 2],
        ["010221000", 2],
    ],
)
def test_ehaustive_search_agent_gets_best_action(state: str, expected: int):
    board = Board(state)
    agent = ExhaustiveSearchAgent(board.next_player)

    action = agent.get_action(board)

    assert action == expected

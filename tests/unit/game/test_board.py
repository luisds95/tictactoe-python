import pytest
from tictactoe.game.board import Board


@pytest.fixture
def board():
    return Board()


def test_initial_state_of_board(board: Board):
    assert str(board) == '000000000'


@pytest.mark.parametrize(
    "int_state,str_state",
    [[511, '111111111'], [256, '100000000'], [32, '000100000']]
)
def test_load_state(int_state: int, str_state: str, board: Board):
    board.load_state(int_state)
    assert board.to_str() == str_state

    board.load_state(0)
    assert board.state == 0

    board.load_state(str_state)
    assert board.state == int_state
    

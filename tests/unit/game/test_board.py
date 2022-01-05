import pytest

from tictactoe.game import Board, InvalidBoardError


@pytest.fixture
def board():
    return Board()


def test_initial_state_of_board(board: Board):
    assert str(board) == "000000000"


@pytest.mark.parametrize(
    "state,success",
    [
        ["111111111", False],
        ["10000000", False],
        ["000000o00", False],
        ["000000000", True],
        ["001002001", True],
        ["001210120", True],
    ],
)
def test_load_state(state: str, success: bool, board: Board):
    if success:
        board.load_state(state)
        assert str(board) == state
    else:
        with pytest.raises(InvalidBoardError):
            board.load_state(state)

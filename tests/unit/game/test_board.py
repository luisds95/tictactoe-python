import pytest

from tictactoe.game import Board, InvalidBoardError


def test_initial_state_of_board():
    board = Board()
    assert str(board) == "000000000"
    assert board.next_player == 1


@pytest.mark.parametrize(
    "state",
    [
        "000000000",
        "001002001",
        "001210120",
    ],
)
def test_board_loads_correct_states(state: str):
    board = Board(state)
    assert str(board) == state


@pytest.mark.parametrize(
    "state",
    [
        "111111111",
        "10000000",
        "000000o00",
    ],
)
def test_board_fails_loading_wrong_states(state: str):
    with pytest.raises(InvalidBoardError):
        Board(state)


@pytest.mark.parametrize("state,next_player", [["100000000", 2], ["100000020", 1]])
def test_next_player_updates_when_loading_state(state: str, next_player: int):
    board = Board(state)
    assert board.next_player == next_player

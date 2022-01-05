import pytest

from tictactoe.game import Board, InvalidBoardError, InvalidMoveError


def test_initial_state_of_board():
    board = Board()
    assert str(board) == "000000000"
    assert board.next_player == "1"


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


@pytest.mark.parametrize("state,next_player", [["100000000", "2"], ["100000020", "1"]])
def test_next_player_updates_when_loading_state(state: str, next_player: str):
    board = Board(state)
    assert board.next_player == next_player


@pytest.mark.parametrize(
    "move,should_succeed,original_state,new_state",
    [
        [0, True, "000000000", "100000000"],
        [1, True, "100000000", "120000000"],
        [5, True, "120000000", "120001000"],
        [0, False, "100000000", "100000000"],
        [9, False, "100000000", "100000000"],
    ],
)
def test_move(move: int, should_succeed: bool, original_state: str, new_state: str):
    board = Board(original_state)
    if should_succeed:
        board.make_move(move)
        assert str(board) == new_state
    else:
        with pytest.raises(InvalidMoveError):
            board.make_move(move)

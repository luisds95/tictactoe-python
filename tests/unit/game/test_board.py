import pytest

from tictactoe.game import Board, GameOutcome, InvalidBoardError, InvalidMoveError


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
        [5, False, "102100102", "102100102"],
    ],
)
def test_make_move(
    move: int, should_succeed: bool, original_state: str, new_state: str
):
    board = Board(original_state)
    if should_succeed:
        board.make_move(move)
        assert str(board) == new_state
    else:
        with pytest.raises(InvalidMoveError):
            board.make_move(move)


@pytest.mark.parametrize(
    "state,expected_winner",
    [
        ["000000000", GameOutcome.NA],
        ["121120000", GameOutcome.NA],
        ["121121212", GameOutcome.DRAW],
        ["122120100", GameOutcome.P1],
        ["021021120", GameOutcome.P2],
        ["111202000", GameOutcome.P1],
        ["101222100", GameOutcome.P2],
        ["122012101", GameOutcome.P1],
        ["112120200", GameOutcome.P2],
    ],
)
def test_outcome(state: str, expected_winner: GameOutcome):
    board = Board(state)
    assert board.outcome == expected_winner


def test_print_can_execute():
    board = Board("112120200")
    board.print()

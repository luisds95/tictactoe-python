from collections import Counter
from typing import Union

from tictactoe.game.exceptions import InvalidBoardError, InvalidMoveError


class Board:
    def __init__(self, state: Union[list, str] = None) -> None:
        self.state = list("000000000") if state is None else list(state)
        self.moves = self.get_moves()
        self.validate_state()
        self.next_player = self.get_next_player()

    def __str__(self) -> str:
        return "".join(self.state)

    def get_moves(self) -> dict:
        return Counter(self.state)

    def validate_state(self) -> None:
        if len(self.state) != 9:
            raise InvalidBoardError("Invalid length of board")

        chars_in_state = set(self.moves.keys())
        valid_chars = set("012")
        if chars_in_state.difference(valid_chars):
            raise InvalidBoardError("Invalid character in board")

        if not (
            self.moves["1"] == self.moves["2"]
            or self.moves["1"] == (self.moves["2"] + 1)
        ):
            raise InvalidBoardError("Unreachable position")

    def get_next_player(self) -> str:
        return str(int(self.moves["1"] != self.moves["2"]) + 1)

    def make_move(self, move: int) -> None:
        if not self.is_valid_move(move):
            raise InvalidMoveError(f"Move {move} is invalid")

        self.state[move] = self.next_player
        self.moves[self.next_player] += 1
        self.next_player = self.get_next_player()

    def is_valid_move(self, move: int) -> bool:
        return 0 <= move < len(self.state) and self.state[move] == "0"

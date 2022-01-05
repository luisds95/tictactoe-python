from collections import Counter

from tictactoe.game.exceptions import InvalidBoardError


class Board:
    def __init__(self, state: str = None) -> None:
        self.state = "000000000" if state is None else state
        self.moves = self.get_moves()
        self.validate_state()
        self.next_player = self.get_next_player()

    def __str__(self) -> str:
        return self.state

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

    def get_moves(self) -> dict:
        return Counter(self.state)

    def get_next_player(self) -> int:
        return int(self.moves["1"] != self.moves["2"]) + 1

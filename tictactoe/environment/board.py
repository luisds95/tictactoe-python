import logging
from collections import Counter
from typing import Union, List

from tictactoe.environment.enums import GameOutcome
from tictactoe.environment.exceptions import InvalidBoardError, InvalidMoveError, NoWinnerError

N_ROWS = 3


class Board:
    def __init__(self, state: Union[list, str] = None) -> None:
        self.state = list("000000000") if state is None else list(state)
        self.moves = self.get_moves()
        self.validate_state()
        self.next_player = self.get_next_player()
        self.outcome = self._get_outcome()

    def __str__(self) -> str:
        state_map = {"1": "X", "2": "O", "0": " "}
        mapped_state = [state_map[char] for char in self.state]
        printable = "\n"
        for row in range(N_ROWS):
            idx = row * N_ROWS
            row_values = " | ".join(mapped_state[idx : idx + N_ROWS])
            printable += row_values
            if row != N_ROWS - 1:
                printable += "\n" + "-" * len(row_values) + "\n"
        return printable

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

    def make_move_on_copy(self, move: int) -> "Board":
        copy = self.copy()
        copy.make_move(move)
        return copy

    def copy(self) -> "Board":
        return Board(self.state)

    def make_move(self, move: int) -> None:
        if not self.is_valid_move(move):
            raise InvalidMoveError(f"Move {move} is invalid")

        self.state[move] = self.next_player
        self.moves[self.next_player] += 1
        self.moves["0"] -= 1
        self.next_player = self.get_next_player()
        self.outcome = self._get_outcome()

    def is_valid_move(self, move: int) -> bool:
        return (
            0 <= move < len(self.state)
            and not self.is_finished()
            and self.state[move] == "0"
        )

    def is_full(self) -> bool:
        return self.moves.get("0", 0) == 0

    def is_finished(self) -> bool:
        return self.outcome != GameOutcome.NA

    def _get_outcome(self) -> GameOutcome:
        if not self.could_have_a_winner():
            return GameOutcome.NA

        try:
            return self.get_winner()
        except NoWinnerError:
            return GameOutcome.DRAW if self.is_full() else GameOutcome.NA

    def could_have_a_winner(self) -> bool:
        return self.moves["1"] >= N_ROWS

    def get_winner(self) -> GameOutcome:
        funcs = [
            self.search_for_winner_in_columns,
            self.search_for_winner_in_rows,
            self.search_for_winner_in_diagonals,
        ]
        for func in funcs:
            winner = func()
            if winner != GameOutcome.NA:
                return winner

        if self.is_full():
            return GameOutcome.DRAW

        raise NoWinnerError

    def search_for_winner_in_columns(self) -> GameOutcome:
        for column in range(N_ROWS):
            if (
                self.state[column]
                == self.state[column + N_ROWS]
                == self.state[column + N_ROWS * 2]
            ):
                return GameOutcome(self.state[column])
        return GameOutcome.NA

    def search_for_winner_in_rows(self) -> GameOutcome:
        for row in range(0, N_ROWS ** 2, N_ROWS):
            if self.state[row] == self.state[row + 1] == self.state[row + 2]:
                return GameOutcome(self.state[row])
        return GameOutcome.NA

    def search_for_winner_in_diagonals(self) -> GameOutcome:
        if (
            self.state[0] == self.state[4] == self.state[8]
            or self.state[2] == self.state[4] == self.state[6]
        ):
            return GameOutcome(self.state[4])
        return GameOutcome.NA

    def log(self, level: int = logging.DEBUG) -> None:
        logging.log(level, str(self))

    def get_valid_moves(self) -> List[int]:
        return [idx for idx, value in enumerate(self.state) if value == "0"]
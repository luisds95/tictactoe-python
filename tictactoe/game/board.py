from tictactoe.game.exceptions import InvalidBoardError


class Board:
    def __init__(self) -> None:
        self.state = "000000000"

    def __str__(self) -> str:
        return self.state

    def load_state(self, state: str) -> None:
        self.validate_state(state)
        self.state = state

    @staticmethod
    def validate_state(state: str) -> None:
        if len(state) != 9:
            raise InvalidBoardError("Invalid length of board")

        ones = 0
        twos = 0
        for char in state:
            if char == "1":
                ones += 1
            elif char == "2":
                twos += 1
            elif char != "0":
                raise InvalidBoardError(f"Invalid character in board: {char}")

        if not (ones == twos or ones == (twos + 1)):
            raise InvalidBoardError("Unreachable position")

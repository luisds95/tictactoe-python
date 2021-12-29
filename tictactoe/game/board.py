from typing import Union


class Board:
    def __init__(self) -> None:
        self.state = 0

    def __str__(self) -> str:
        return self.to_str()

    def to_str(self) -> str:
        return f"{self.state:09b}"

    def load_state(self, state: Union[str, int]) -> None:
        if isinstance(state, int):
            self.load_int_state(state)
        else:
            self.load_str_state(state)

    def load_int_state(self, state: int) -> None:
        self.state = state

    def load_str_state(self, state: str) -> None:
        self.state = eval(f"0b{state}")

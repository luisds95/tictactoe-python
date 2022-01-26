from typing import Any, Dict

from tictactoe.database.base import Database
from tictactoe.environment import Board


class InMemoryDatabase(Database):
    def __init__(self) -> None:
        super().__init__()
        self.data: Dict[str, dict] = {}

    def connect(self) -> None:
        self.data = {}

    def commit(self) -> None:
        pass

    def exists(self, key: Board) -> bool:
        return key.get_str_state() in self.data

    def get(self, board: Board, default: Any = None) -> Dict[int, int]:
        return self.data.get(board.get_str_state(), default)  # type: ignore

    def size(self) -> int:
        return len(self.data)

    def update(self, board: Board, values: Dict[int, int]) -> None:
        self.data[board.get_str_state()] = values

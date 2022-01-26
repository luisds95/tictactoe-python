from abc import ABC, abstractmethod
from typing import Any, Dict

from tictactoe.environment import Board


class Database(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def get(self, board: Board, default: Any = None) -> Dict[int, int]:
        pass

    @abstractmethod
    def update(self, board: Board, values: Dict[int, int]) -> None:
        pass

    @abstractmethod
    def commit(self) -> None:
        pass

    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def exists(self, key: Board) -> bool:
        pass

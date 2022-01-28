import json
from pathlib import Path

from tictactoe.database.memory import InMemoryDatabase


class DictDatabase(InMemoryDatabase):
    def __init__(self, data_path: Path) -> None:
        super().__init__()
        self.data_path = data_path

    def connect(self) -> None:
        if self.data_path.exists():
            with open(self.data_path) as stream:
                self._data = json.load(stream)
            self._data = {
                board: {int(action): value for action, value in values.items()}
                for board, values in self.data.items()
            }
        else:
            self.commit()

    def commit(self) -> None:
        self._data = {
            state: {str(move): float(values) for move, values in moves.items()}
            for state, moves in self._data.items()
        }
        with open(self.data_path, "w") as file:
            json.dump(self._data, file)

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
                self.data = json.load(stream)
            self.data = {
                board: {int(action): value for action, value in values.items()}
                for board, values in self.data.items()
            }
        else:
            self.commit()

    def commit(self) -> None:
        with open(self.data_path, "w") as file:
            json.dump(self.data, file)

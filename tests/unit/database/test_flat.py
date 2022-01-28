import json
import os
from pathlib import Path
from typing import Union

import pytest

from tictactoe.database import DictDatabase
from tictactoe.environment.board import Board


@pytest.fixture
def data():
    return {"010221100": {0: 0, 2: 0, 7: 0, 8: 0}, "211221120": {8: 0}}


def read_json(path: Union[str, Path]) -> dict:
    with open(path) as stream:
        values = json.load(stream)
    return values


def test_dict_database_loads_some_data(data: dict):
    file_path = Path("test_file.json")

    with open(file_path, "w") as file:
        json.dump(data, file)

    db = DictDatabase(file_path)
    db.connect()

    for k, v in data.items():
        assert db.get(Board(k)) == v

    os.remove(file_path)


def test_dict_database_element_exists(data: dict):
    db = DictDatabase(Path())
    db._data = data

    assert db.exists(Board(list(data)[0]))
    assert not db.exists(Board())


def test_dict_database_updates_data(data: dict):
    db = DictDatabase(Path())
    db._data = data

    board = Board("010221100")
    new_data = {0: 0, 2: 0, 7: 1, 8: 0}
    db.update(board, new_data)

    assert db.get(board) == new_data


def test_dict_database_returns_correct_number_of_elements(data: dict):
    db = DictDatabase(Path())
    db._data = data

    assert db.size() == 2


def test_dict_database_only_writes_json_when_commiting(data: dict):
    file_path = Path("test_file2.json")
    if file_path.exists():
        os.remove(file_path)

    db = DictDatabase(file_path)
    db.connect()
    assert file_path.exists()

    for board_str, values in data.items():
        db.update(Board(board_str), values)
        assert len(read_json(file_path)) == 0

    db.commit()
    assert len(read_json(file_path)) == 2

    os.remove(file_path)

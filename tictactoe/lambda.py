import json
from typing import Any, Dict

from tictactoe.database import DictDatabase
from tictactoe.environment import DICT_DATABASE_FILE, Board, InvalidBoardError
from tictactoe.game import get_move_response
from pathlib import Path


def move_handler(event: Dict[str, Any], context: Dict[str, Any]) -> str:
    board_str = event.get("board", "0")

    try:
        board = Board(board_str)
    except InvalidBoardError as e:
        return json.dumps({"error": str(e)})

    database = DictDatabase(data_path=DICT_DATABASE_FILE)
    database.connect()

    response = get_move_response(board, database)
    return json.dumps(response)

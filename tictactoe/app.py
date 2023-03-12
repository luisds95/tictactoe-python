import json

from flask import Flask, request

from tictactoe.database import DictDatabase
from tictactoe.environment import DICT_DATABASE_FILE, Board, InvalidBoardError
from tictactoe.game import get_move_response

app = Flask(__name__)
database = DictDatabase(DICT_DATABASE_FILE)


@app.route("/")
def home() -> str:
    return json.dumps({"health": "OK"})


@app.route("/get-action")
def get_action() -> str:
    """
    Returns an action based on the board provided.

    Example call:
        http://127.0.0.1:5000/get-action?board=010221000

    Response:
        {"action": 2, "result": "NA"}
    """
    args = request.args.to_dict()
    board_str = args.get("board", "0")

    try:
        board = Board(board_str)
    except InvalidBoardError as e:
        return json.dumps({"error": str(e)})

    response = get_move_response(board, database)
    return json.dumps(response)

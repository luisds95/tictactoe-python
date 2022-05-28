import json

from flask import Flask, request

from tictactoe.agent import ExhaustiveSearchAgent
from tictactoe.database import DictDatabase
from tictactoe.environment import (
    DICT_DATABASE_FILE,
    Board,
    GameOutcome,
    InvalidBoardError,
)

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

    try:
        board = Board(args.get("board", "0"))
    except InvalidBoardError as e:
        return json.dumps({"error": str(e)})

    if board.outcome == GameOutcome.NA:
        agent = ExhaustiveSearchAgent(db=database, player_number=board.next_player)
        action = agent.get_action(board)
        board.make_move(action)
        response = {"action": action, "result": board.outcome.name}
    else:
        response = {"result": board.outcome.name}

    return json.dumps(response)

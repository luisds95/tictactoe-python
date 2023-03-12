from typing import Any, Dict

from tictactoe.agent import ExhaustiveSearchAgent
from tictactoe.database import Database
from tictactoe.environment import Board, GameOutcome


def get_move_response(board: Board, database: Database) -> Dict[str, Any]:
    if board.outcome == GameOutcome.NA:
        agent = ExhaustiveSearchAgent(db=database, player_number=board.next_player)
        action = agent.get_action(board)
        board.make_move(action)
        response = {"action": action, "result": board.outcome.name}
    else:
        response = {"result": board.outcome.name}
    return response

from ctypes import Union
from typing import Dict
from tictactoe.agent.base import Agent
from tictactoe.agent.enums import AgentTypes
from tictactoe.environment import Board, NoWinnerError


class ExhaustiveSearchAgent(Agent):
    def __init__(self, player_number: Union[int, str]) -> None:
        super().__init__()
        self.set_player_number(player_number)

    def agent_type(self) -> AgentTypes:
        return AgentTypes.searcher

    def _get_action(self, board: Board) -> int:
        return 0

    def evaluate_moves(self, board: Board, max_depth: int = None) -> Dict[int, int]:
        moves = board.get_valid_moves()
        for move in moves:
            new_board = board.make_move_on_copy(move)
            value = new_board.get_winner()
        return {}

    def get_board_value(self, board: Board) -> int:
        try:
            winner = board.get_winner()
        except NoWinnerError:
            value = 0
        else:
            pass
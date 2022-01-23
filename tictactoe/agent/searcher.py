from tictactoe.agent.base import Agent
from tictactoe.environment import Board


class SearchAgent(Agent):
    def _get_action(self, board: Board) -> int:
        return super()._get_action(board)
import random

from tictactoe.agent.base import Agent
from tictactoe.agent.enums import AgentTypes
from tictactoe.environment import Board


class RandomAgent(Agent):
    def _get_action(self, board: Board) -> int:
        indices = board.get_valid_moves()
        return indices[random.randint(0, len(indices) - 1)]

    @property
    def agent_type(self) -> AgentTypes:
        return AgentTypes.random

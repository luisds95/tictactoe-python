import random

from tictactoe.agent.base import Agent
from tictactoe.agent.enums import AgentTypes
from tictactoe.game import Board


class RandomAgent(Agent):
    def _get_action(self, board: Board) -> int:
        indices = [idx for idx, value in enumerate(board.state) if value == "0"]
        return indices[random.randint(0, len(indices) - 1)]

    def get_agent_type(self) -> AgentTypes:
        return AgentTypes.random

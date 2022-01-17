from abc import ABC, abstractmethod
from typing import Optional, Union

from tictactoe.agent.enums import AgentTypes
from tictactoe.agent.exceptions import NoValidMovesError
from tictactoe.game import Board


class Agent(ABC):
    def __init__(self) -> None:
        super().__init__()

        self.player_number: Optional[str] = None

    def set_player_number(self, player_number: Union[str, int]) -> None:
        self.player_number = str(player_number)

    def get_action(self, board: Board) -> int:
        if board.is_finished():
            raise NoValidMovesError
        return self._get_action(board)

    @abstractmethod
    def _get_action(self, board: Board) -> int:
        pass

    @abstractmethod
    def get_agent_type(self) -> AgentTypes:
        pass

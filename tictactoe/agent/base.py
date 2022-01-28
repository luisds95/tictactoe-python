from abc import ABC, abstractmethod, abstractproperty
from typing import Optional, Union

from tictactoe.agent.enums import AgentTypes
from tictactoe.agent.exceptions import NoValidMovesError, PlayerNumberNotSetError
from tictactoe.database import Database
from tictactoe.environment import Board, GameOutcome
from tictactoe.log import TrainingLogger


class Agent(ABC):
    def __init__(self) -> None:
        super().__init__()
        self._player_number: Optional[GameOutcome] = None

    @property
    def player_number(self) -> GameOutcome:
        if self._player_number is None:
            raise PlayerNumberNotSetError
        return self._player_number

    def set_player_number(self, player_number: Union[str, int]) -> None:
        self._player_number = GameOutcome(str(player_number))

    def get_action(self, board: Board) -> int:
        if board.is_finished():
            raise NoValidMovesError
        return self._get_action(board)

    @abstractmethod
    def _get_action(self, board: Board) -> int:
        pass

    @abstractproperty
    def agent_type(self) -> AgentTypes:
        pass

    def is_trainable(self) -> bool:
        return False


class TrainableAgent(Agent):
    def __init__(self, db: Database, logger: TrainingLogger = None) -> None:
        super().__init__()
        self.db = db
        self.is_training = False
        self.logger = TrainingLogger(frequency=0) if logger is None else logger

    def train(self, board: Board = None) -> int:
        self.is_training = True
        self.logger.start_training()

        action = self._train(board)

        self.is_training = False

        return action

    @abstractmethod
    def _train(self, board: Board = None) -> int:
        pass

    def is_trainable(self) -> bool:
        return True

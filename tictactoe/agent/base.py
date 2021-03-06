from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime
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
    def agent_type(self) -> AgentTypes:  # type: ignore
        pass


class TrainableAgent(Agent):
    def __init__(self, db: Database, logger: Optional[TrainingLogger] = None) -> None:
        super().__init__()
        self.db = db
        self.is_training = False
        self.logger = TrainingLogger(frequency=0) if logger is None else logger

    def train(self, board: Optional[Board] = None) -> int:
        start = datetime.now()
        self.is_training = True
        self.logger.start_training()

        action = self._train(board)

        self.is_training = False
        print("Finished training in", datetime.now() - start)

        return action

    @abstractmethod
    def _train(self, board: Optional[Board] = None) -> int:
        pass

from pathlib import Path
from typing import Optional, Tuple

from tictactoe.agent import (
    Agent,
    AgentTypes,
    ExhaustiveSearchAgent,
    HumanAgent,
    RandomAgent,
)
from tictactoe.database import DictDatabase, InMemoryDatabase
from tictactoe.environment import Board, GameOutcome
from tictactoe.log import TrainingLogger


class Game:
    def __init__(
        self,
        p1_name: str,
        p2_name: str,
        database_str: Optional[str] = None,
        logger: Optional[TrainingLogger] = None,
    ) -> None:
        self.p1_name = p1_name.lower()
        self.p2_name = p2_name.lower()
        self.database = (
            InMemoryDatabase()
            if database_str is None
            else DictDatabase(Path(database_str))
        )
        self.logger = TrainingLogger() if logger is None else logger

        self.p1 = self.get_agent(1)
        self.p2 = self.get_agent(2)
        self.board = Board()

    def play(self, n: int = 1) -> None:
        for _ in range(n):
            self._play_one()
            self.print_result()

    def get_agent(self, number: int) -> Agent:
        name = self.p1_name if number == 1 else self.p2_name
        if name == AgentTypes.human.value:
            agent: Agent = HumanAgent()
        elif name == AgentTypes.random.value:
            agent = RandomAgent()
        elif name == AgentTypes.searcher.value:
            agent = ExhaustiveSearchAgent(
                self.database, player_number=number, logger=self.logger
            )
        else:
            raise ValueError(f"No agent {name}")
        return agent

    def _play_one(self):
        self.reset()
        p1_turn = True

        while not self.board.is_finished():
            self.board.log()
            player = self.p1 if p1_turn else self.p2
            p1_turn = not p1_turn
            action = player.get_action(self.board)
            self.board.make_move(action)

    def reset(self) -> None:
        self.board = Board()

    def print_result(self) -> None:
        winner = self.board.outcome
        self.board.log()
        if winner == GameOutcome.DRAW:
            self.logger.log("Draw!", force=True)
        else:
            self.logger.log(f"{winner.value} wins!", force=True)

    @property
    def agents(self) -> Tuple[Agent, Agent]:
        return self.p1, self.p2

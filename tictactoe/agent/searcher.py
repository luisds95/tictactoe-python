from typing import Dict, Optional, Union

import numpy as np

from tictactoe.agent.base import TrainableAgent
from tictactoe.agent.enums import AgentTypes
from tictactoe.database import Database
from tictactoe.environment import Board, GameOutcome
from tictactoe.log import TrainingLogger


class ExhaustiveSearchAgent(TrainableAgent):
    WIN_REWARD = 1
    DRAW_REWARD = 0
    LOSE_REWARD = -1

    def __init__(
        self,
        db: Database,
        player_number: Union[int, str],
        logger: Optional[TrainingLogger] = None,
        max_depth: int = -1,
        commit_freq: int = 1000,
    ) -> None:
        super().__init__(db, logger=logger)
        self.max_depth = max_depth
        self.commit_freq = commit_freq

        self.set_player_number(player_number)

    def agent_type(self) -> AgentTypes:
        return AgentTypes.searcher

    def _train(self, board: Optional[Board] = None) -> int:
        board = Board() if board is None else board
        action = self.get_action(board)
        self.db.commit()
        return action

    def _get_action(self, board: Board) -> int:
        values = self.db.get(board)
        if values is None:
            values = self.evaluate_moves(board)

        return max(values, key=lambda move: values[move])

    def evaluate_moves(self, board: Board) -> Dict[int, int]:
        return self._evaluate_moves(board, current_depth=0)

    def _evaluate_moves(self, board: Board, current_depth: int) -> Dict[int, int]:
        values = {}

        moves = board.get_valid_moves()

        for move in moves:
            new_board = board.make_move_on_copy(move)

            if new_board.outcome == GameOutcome.NA:
                if current_depth == self.max_depth:
                    values[move] = self.DRAW_REWARD
                else:
                    future_values = [
                        v
                        for v in self._evaluate_moves(
                            new_board, current_depth=current_depth + 1
                        ).values()
                    ]
                    values[move] = (
                        np.max(future_values)
                        if new_board.next_player == self.player_number.value
                        else np.min(future_values)
                    )
            elif new_board.outcome == GameOutcome.DRAW:
                values[move] = self.DRAW_REWARD
            elif new_board.outcome == self.player_number:
                values[move] = self.WIN_REWARD
            else:
                values[move] = self.LOSE_REWARD

        if self.is_training:
            self._update_database(board, values)

        return values

    def _update_database(self, board: Board, values: Dict[int, int]) -> None:
        if self.db.get(board, None) == values:
            return

        self.db.update(board, values)
        if self.db.size() % self.commit_freq == 0:
            self.db.commit()
        self.logger.log_state()

    def print_sequence(self, board: Board) -> None:
        board = board.copy()

        while not board.is_finished():
            board.log()
            action = self._get_action(board)
            board.make_move(action)
        board.log()

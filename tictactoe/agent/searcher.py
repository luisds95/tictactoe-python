from pathlib import Path
from typing import Dict, Union

import numpy as np
import json

from tictactoe.agent.base import TrainableAgent
from tictactoe.agent.enums import AgentTypes
from tictactoe.environment import Board, GameOutcome
from tictactoe.database import Database


class ExhaustiveSearchAgent(TrainableAgent):
    WIN_REWARD = 1
    DRAW_REWARD = 0
    LOSE_REWARD = -1

    def __init__(self, player_number: Union[int, str], db: Database,  max_depth: int = -1) -> None:
        super().__init__()
        self.max_depth = max_depth
        self.db = db

        self.set_player_number(player_number)

    def agent_type(self) -> AgentTypes:
        return AgentTypes.searcher

    def load_data(self) -> None:
        with open(self.data_path) as stream:
            self.data = json.load(stream)

    def save_data(self) -> None:
        with open(self.data_path, "w") as stream:
            json.dump(self.data, stream)

    def train(self) -> None:
        return super().train()

    def _get_action(self, board: Board) -> int:
        board_str_state = board.get_str_state()
        if board_str_state in self.data:
            return self.data[board_str_state]

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

        return values

    def _save_values(self, board: Board, values: Dict[int, int]):
        # This will be called by _evaluate_moves
        pass

    def print_sequence(self, board: Board) -> None:
        board = board.copy()

        while not board.is_finished():
            board.log()
            action = self._get_action(board)
            board.make_move(action)
        board.log()

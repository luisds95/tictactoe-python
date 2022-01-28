from typing import List
from unittest.mock import MagicMock, patch

import pytest

from tictactoe.log import Logger, TrainingLogger


@pytest.mark.parametrize(
    "should_force,frequency,should_log",
    [
        [[False], 1, [True]],
        [[False, False], 1, [True, True]],
        [[False, False], 2, [False, True]],
        [[False, False], 3, [False, False]],
        [[True, False], 3, [True, False]],
        [[False, False], 0, [False, False]],
    ],
    ids=["one_message", "two_messages", "skip_one", "skip_two", "force", "never"],
)
def test_logger_logs(
    should_force: List[bool],
    frequency: int,
    should_log: List[bool],
):
    messages = list("abcdefgh")
    logger = Logger(frequency=frequency)
    logger.logger = MagicMock()
    for message, force, result in zip(messages, should_force, should_log):
        logger.log(message, force=force)
        if result:
            logger.logger.log.assert_called_once()
        else:
            logger.logger.log.assert_not_called()
        logger.logger.reset_mock()


def test_training_logger_logs_state():
    logger = TrainingLogger()

    logger.start_training()
    logger.log_state()
    logger.log("test")

    assert logger.state_count == 1

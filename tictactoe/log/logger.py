import logging
from datetime import datetime
from typing import Callable, Optional


class Logger:
    def __init__(self, frequency: int = 1, handler: Callable = print) -> None:
        self.frequency = frequency
        self.handler = handler

        self.enabled = frequency > 0
        self.count = 0

    def log(self, message: str, force: bool = False) -> None:
        self.count += 1
        if self._should_log(force):
            self.handler(message)

    def _should_log(self, force: bool) -> bool:
        return force or (self.enabled and self.count % self.frequency == 0)


class TrainingLogger(Logger):
    def __init__(self, frequency: int = -1, handler: Callable = logging.log) -> None:
        super().__init__(frequency, handler)
        self.state_count = 0
        self._start_time: Optional[datetime] = None

    def log_state(self, force: bool = False) -> None:
        self.state_count += 1
        elapsed = datetime.now() - self.start_time
        self.log(
            f"{self.state_count} states logged in {str(elapsed)}",
            force=force,
        )

    def start_training(self) -> None:
        self.log("Starting training")
        self._start_time = datetime.now()

    @property
    def start_time(self) -> datetime:
        if self._start_time is None:
            raise ValueError("Logger has not been started. Call logger.start() first.")
        return self._start_time

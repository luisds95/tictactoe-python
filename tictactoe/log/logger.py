import logging
from datetime import datetime
from typing import Optional


class Logger:
    def __init__(self, frequency: int = 1) -> None:
        self.logger = logging.getLogger()
        self.frequency = frequency
        self.enabled = frequency > 0
        self.count = 0

    def log(
        self, message: str, *args, force: bool = False, level: int = logging.INFO
    ) -> None:
        self.count += 1
        if self._should_log(force):
            self.logger.log(level, message, *args)

    def _should_log(self, force: bool) -> bool:
        return force or (self.enabled and self.count % self.frequency == 0)

    def set_level(self, level: int) -> None:
        self.logger.setLevel(level)


class TrainingLogger(Logger):
    def __init__(self, frequency: int = -1) -> None:
        super().__init__(frequency)
        self.state_count = 0
        self._start_time: Optional[datetime] = None

    def log_state(self, force: bool = False, level: int = logging.INFO) -> None:
        self.state_count += 1
        elapsed = datetime.now() - self.start_time
        self.log(
            "%s states logged in %s",
            self.state_count,
            str(elapsed),
            force=force,
            level=level,
        )

    def start_training(self) -> None:
        self.log("Starting training")
        self._start_time = datetime.now()

    @property
    def start_time(self) -> datetime:
        if self._start_time is None:
            raise ValueError("Logger has not been started. Call logger.start() first.")
        return self._start_time

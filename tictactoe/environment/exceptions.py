class GameError(Exception):
    pass


class BoardError(GameError):
    pass


class InvalidBoardError(BoardError):
    pass


class InvalidMoveError(BoardError):
    pass


class NoWinnerError(GameError):
    pass

class GameError(Exception):
    pass


class BoardError(GameError):
    pass


class InvalidBoardError(BoardError):
    pass

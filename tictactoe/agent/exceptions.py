class AgentError(Exception):
    pass


class NoValidMovesError(AgentError):
    pass


class PlayerNumberNotSetError(AgentError):
    pass


class AgentIsNotTrainableError(AgentError):
    pass

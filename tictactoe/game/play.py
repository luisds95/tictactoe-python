import logging

from tictactoe.agent import Agent, AgentTypes, HumanAgent, RandomAgent, ExhaustiveSearchAgent
from tictactoe.environment import Board, GameOutcome
from tictactoe.log import TrainingLogger


def play_games(p1: str, p2: str, n: int = 1, train: bool = False, database: str = None) -> None:
    p1_agent = get_agent(p1, number=1)
    p2_agent = get_agent(p2, number=2)

    for _ in range(n):
        play_and_print_result(p1_agent, p2_agent)


def get_agent(name: str, number: int, database: str = None) -> Agent:
    name = name.lower()
    if name == AgentTypes.human.value:
        agent: Agent = HumanAgent()
    elif name == AgentTypes.random.value:
        agent = RandomAgent()
    elif name == AgentTypes.searcher.value:
        agent = ExhaustiveSearchAgent(database, number)
    else:
        raise ValueError(f"No agent {name}")
    return agent


def play_and_print_result(p1_agent: Agent, p2_agent: Agent):
    board = play_game(p1_agent, p2_agent)
    print_game_result(board)


def play_game(p1: Agent, p2: Agent) -> Board:
    board = Board()
    p1_turn = True

    while not board.is_finished():
        board.log()
        player = p1 if p1_turn else p2
        p1_turn = not p1_turn
        action = player.get_action(board)
        board.make_move(action)

    return board


def print_game_result(board: Board):
    winner = board.get_winner()
    board.log()
    if winner == GameOutcome.DRAW:
        logging.info("Draw!")
    else:
        logging.info("%s wins!", winner.value)

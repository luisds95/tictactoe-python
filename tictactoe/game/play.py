from tictactoe.agent import Agent, AgentTypes, HumanAgent, RandomAgent
from tictactoe.game.board import Board
from tictactoe.game.enums import GameOutcome


def new_game(p1: str, p2: str):
    p1_agent = get_agent(p1)
    p2_agent = get_agent(p2)
    board = play_game(p1_agent, p2_agent)
    print_game_result(board)


def get_agent(name: str) -> Agent:
    name = name.lower()
    if name == AgentTypes.human.value:
        agent: Agent = HumanAgent()
    elif name == AgentTypes.random.value:
        agent = RandomAgent()
    else:
        raise ValueError(f"No agent {name}")
    return agent


def play_game(p1: Agent, p2: Agent) -> Board:
    board = Board()
    p1_turn = True

    while not board.is_finished():
        board.print()
        player = p1 if p1_turn else p2
        p1_turn = not p1_turn
        action = player.get_action(board)
        board.make_move(action)

    return board


def print_game_result(board: Board):
    winner = board.get_winner()
    board.print()
    if winner == GameOutcome.DRAW:
        print("Draw!")
    else:
        print(f"{winner.value} wins!")

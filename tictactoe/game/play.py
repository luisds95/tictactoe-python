from tictactoe.agent import HumanAgent, RandomAgent
from tictactoe.game.board import Board
from tictactoe.game.enums import GameOutcome


def new_game():
    p1 = HumanAgent()
    p2 = RandomAgent()
    board = Board()
    p1_turn = True

    while not board.is_finished():
        board.print()
        player = p1 if p1_turn else p2
        p1_turn = not p1_turn
        action = player.get_action(board)
        board.make_move(action)

    winner = board.get_winner()
    board.print()
    if winner == GameOutcome.DRAW:
        print("Draw!")
    else:
        print(f"{winner.value} wins!")

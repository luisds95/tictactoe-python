import click

from tictactoe.game.play import new_game


@click.command()
@click.argument("P1", default="human")
@click.argument("P2", default="random")
def main(p1: str, p2: str) -> None:
    """
    Play a tic tac toe game. Possible players: human, random
    """
    new_game(p1, p2)

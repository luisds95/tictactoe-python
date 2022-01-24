import logging

import click

from tictactoe.game.play import play_games


@click.command()
@click.argument("P1", default="human")
@click.argument("P2", default="random")
@click.option("-n", default=1, help="Number of games to play", type=int)
@click.option("--loud/--quiet", default=None, help="Level of verbosity")
def main(p1: str, p2: str, n: int, loud: bool) -> None:
    """
    Play a tic tac toe game. Possible players: human, random
    """
    if loud or "human" in (p1, p2):
        logging.getLogger().setLevel(logging.DEBUG)
    else:
        logging.getLogger().setLevel(logging.INFO)
    play_games(p1, p2, n=n)

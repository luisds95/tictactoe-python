import logging

import click

from tictactoe.agent import AgentIsNotTrainableError, TrainableAgent
from tictactoe.game.play import Game
from tictactoe.log.logger import TrainingLogger


@click.command()
@click.argument("P1", default="human")
@click.argument("P2", default="random")
@click.option("--n-games", default=1, help="Number of games to play", type=int)
@click.option("--loud/--quiet", default=None, help="Level of verbosity")
@click.option("--train/--no-train", help="Should train non-human players")
@click.option("--database", default="states.json", type=str)
def main(
    p1: str, p2: str, n_games: int, loud: bool, train: bool, database: str
) -> None:
    """
    Play a tic tac toe game. Possible players: human, random, searcher
    """
    frequency = 1 if loud else 10000
    logger = TrainingLogger(frequency=frequency, handler=click.echo)

    if loud or "human" in (p1, p2):
        logging.getLogger().setLevel(logging.DEBUG)
    else:
        logging.getLogger().setLevel(logging.INFO)

    game = Game(p1, p2, database_str=database, logger=logger)
    if train:
        p1_agent, _ = game.agents
        if isinstance(p1_agent, TrainableAgent):
            logger.log("Starting training", force=True)
            p1_agent.train()
        else:
            raise AgentIsNotTrainableError
    else:
        game.play(n=n_games)

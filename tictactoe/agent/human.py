from tictactoe.agent.base import Agent
from tictactoe.agent.enums import AgentTypes
from tictactoe.game import Board


class HumanAgent(Agent):
    def _get_action(self, board: Board) -> int:
        indices = [str(idx) for idx, value in enumerate(board.state) if value == "0"]
        answer = None
        while answer is None:
            answer = input("Insert next move: ")
            if answer not in indices:
                print("Invalid index. Try again...")
                answer = None
        return int(answer)

    def get_agent_type(self) -> AgentTypes:
        return AgentTypes.human

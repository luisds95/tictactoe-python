import os

root_path = os.path.abspath("~")
activate_this = root_path + "/tictactoe-python/.venv/Scripts/activate_this.py"
with open(activate_this):
    exec(file_.read(), dict(__file__=activate_this))

from tictactoe.app import app as application
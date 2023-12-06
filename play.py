import os
from gameEngine import GameEngine

engine = GameEngine()
# this line ensures that the terminal forces the game to appear at the "top"
os.system("cls" if os.name == "nt" else "clear")
engine.play()  # start the game

import os
from gameEngine import GameEngine

engine = GameEngine()
os.system("cls" if os.name == "nt" else "clear")
engine.play()  # start the game

import view, stateModifier


class GameEngine:
    def __init__(self) -> None:
        self.playerStatus = True
        self.turnCounter = 0
        self.dataNeeded = [None]
        self.dataToBeChanged: [None]
        # self.stateModifier = stateModifier.StateModifier()
        self.inputHandler = view.InputHandler()
        self.outputHandler = view.OutputHandler()

    def executeCommand(self):
        pass

    def checkDonditions(self):
        pass

    def handleCombat(self):
        pass

    def handleDetection(self):
        pass

    def handlePuzzle(self):
        pass

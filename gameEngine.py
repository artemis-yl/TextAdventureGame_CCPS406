import view #, stateModifier


class GameEngine:
    def __init__(self) -> None:
        self.playerStatus = True
        self.turnCounter = 0
        self.dataNeeded = [None]
        self.dataToBeChanged: [None]
        # self.stateModifier = stateModifier.StateModifier()
        self.inHandler = view.InputHandler()
        self.outHandler = view.OutputHandler()

    def executeCommand(self):
        self.inHandler.parseInput()
        verb = self.inHandler.getVerb()

        # check dictionary of verbs to see which correct action to take
        # execute the verb
        # where the heck are we storing the verbs rn...

    def checkConditions(self):
        pass

    def handleCombat(self):
        pass

    def handleDetection(self):
        pass

    def handlePuzzle(self):
        pass

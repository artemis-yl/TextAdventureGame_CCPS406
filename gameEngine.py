import view, gameLoader


class GameEngine:
    def __init__(self) -> None:
        self.playerStatus = True
        self.turnCounter = 0
        self.dataNeeded = [None]
        self.dataToBeChanged: [None]

        self.model = gameLoader( "npc.json", "room.json", "items.json", "puzzles.json", "gameMsg.json", "commands.json" ) 
        self.npcDict, self.roomDict, self.itemDict, self.puzzleDict, self.msgDict, self.commandDict = self.model.loadGame()

        self.inHandler = view.InputHandler(self.commandDict)
        self.outHandler = view.OutputHandler(self.commandDict)

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

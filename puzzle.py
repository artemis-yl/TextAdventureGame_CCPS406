from container import ContainterModel

class Puzzle(ContainterModel):
    def __init__(self, puzzle):
        super().__init__(
            puzzle["name"],
            puzzle["stateDescriptions"],
            puzzle["subPuzzles"]
        )

        self.current_state = puzzle["currentState"]
        self.key = puzzle["key"]
        self.keyVerb = puzzle["keyVerb"]

    def tryToSolve(self, keyItem):
        #print(self.key, keyItem)
        if self.key == keyItem:
            self.current_state = "solved"
            return True
        else:
            return False

    def getSubPuzzles(self):
        return self.getInv()

    def getCurrentState(self):
        return self.current_state

    def setCurrentState(self, currentState):
        self.current_state = currentState

    def getKey(self):
        return self.key
    
    def setKey(self, keyObj):
        self.key = keyObj

    def getKeyVerb(self):
        return self.keyVerb
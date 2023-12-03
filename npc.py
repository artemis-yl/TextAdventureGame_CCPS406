from container import ContainterModel

class NPC(ContainterModel):
    def __init__(self, npc):
        super().__init__(
            npc["name"],
            npc["stateDescriptions"],
            npc["initialInventory"]
        )

        self.dialogue = npc["dialogue"]
        self.current_state = npc["initialState"]
        self.is_active = npc["isActive"]
        self.is_roaming = npc["isRoaming"]

    def getPuzzleState(self):
        pass

    # check if the given key and command are correct
    # TO BE CHANGED
    def tryPuzzle(self, command):
        key = self.puzzle.getKey()
        key_cmd = self.puzzle.getKeyVerb()
        if key in self.inventory and key_cmd == command:
            self.puzzle.solve()

    def getState(self):
        return self.current_state

    def setState(self, new_state):
        if new_state in self.possible_states:
            self.current_state = new_state
            print(f"{self.npc_id} is now in state: {new_state}")
        else:
            print(f"Error: {new_state} is not a valid state for {self.npc_id}")

    def getDialogue(self):
        return self.dialogue

    def checkIfActive(self):
        return self.is_active

    def setActivity(self, is_active):
        self.is_active = is_active
        activity = "active" if is_active else "inactive"
        print(f"{self.npc_id} is now {activity}")

    def checkIfRoaming(self):
        return self.is_roaming

    def setRoaming(self, is_roaming):
        self.is_roaming = is_roaming
        roaming_status = "roaming" if is_roaming else "not roaming"
        print(f"{self.npc_id} is now {roaming_status}")
class NPC:
    def __init__(self, npc_id, initial_state, possible_states):
        self.npc_id = npc_id
        self.current_state = initial_state
        self.possible_states = possible_states
        self.is_active = False
        self.is_roaming = False

    def getState(self):
        return self.current_state

    def setState(self, new_state):
        if new_state in self.possible_states:
            self.current_state = new_state
            print(f"{self.npc_id} is now in state: {new_state}")
        else:
            print(f"Error: {new_state} is not a valid state for {self.npc_id}")

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

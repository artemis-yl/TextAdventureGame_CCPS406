import json

class NPC:
    def __init__(self, npc_id, initial_state, possible_states, is_active, is_roaming, initial_inventory, puzzle_list):
        self.npc_id = npc_id
        self.current_state = initial_state
        self.possible_states = possible_states
        self.is_active = is_active
        self.is_roaming = is_roaming
        self.initial_inventory = initial_inventory
        self.puzzle_list = puzzle_list

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

# Load NPC data from file
with open("npcs.json", 'r') as npc_file:
    npc_data = json.load(npc_file)
    npc_instances = []

    for npc_info in npc_data["npcs"]:
        npc_instances.append(
            NPC(
                npc_info["name"],
                npc_info.get("initialState", ""),  # Handling possible keys in the JSON
                npc_info.get("stateDescriptions", {}),
                npc_info.get("isActive", False),
                npc_info.get("isRoaming", False),
                npc_info.get("initialInventory", []),
                npc_info.get("puzzleList", [])
            )
        )

# Example usage...
# Access and manipulate the NPC instances
for npc in npc_instances:
    print(f"NPC Name: {npc.npc_id}")
    print(f"Current State: {npc.current_state}")
    print(f"Active: {npc.is_active}")
    print(f"Roaming: {npc.is_roaming}")
    print(f"Initial Inventory: {npc.initial_inventory}")
    print(f"Puzzle List: {npc.puzzle_list}")
    print("\n")

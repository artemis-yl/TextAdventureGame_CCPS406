from gameLoader import GameLoader

FILE_NAME_LIST = [
    "npcs.json",
    "room.json",
    "items.json",
    "puzzles.json",
    "gameMsg.json",
    "commands.json",
]


class GameState:
    def __init__(self):
        # load the json objects into dictionaries of each object type
        self.models = GameLoader(FILE_NAME_LIST)
        (
            self.npc_dict,
            self.room_dict,
            self.item_dict,
            self.puzzle_dict,
            self.msg_dict,
            self.command_dict,
        ) = self.models.loadGame()

    def keyToObject(self, dict):
        pass


    def populateWorld(self):
        # 1) fill NPC inventories with items + puzzles
        for npc in self.npc_dict.values():
            tmpList = []

            for thing in npc.inventory:
                if thing.startswith("item"):
                    obj = self.item_dict[thing]
                else:
                    obj = self.puzzle_dict[thing]
                tmpList.append(obj)

            npc.inventory = tmpList

        # 2) fill room inventories with NPCs, items, + puzzles (doors + others)
        for room in self.room_dict.values():
            pass

        # return updated room dictionary
        return self.room_dict

    def save(self):
        pass
        # call gameSaver to save data

    def signalChange(self):
        # Method to signal a change in the game state
        print("Game state changed!")

    # Example Usage:
    # Instantiate GameState and use its attributes and methods
    # game_state = GameState()
    # game_state.currentRoom = Room("Start Room", "A room where the adventure begins", [], "Open", None, [])
    # game_state.rooms = [Room("Room 1", "Description 1", [], "Open", None, []),
    #                     Room("Room 2", "Description 2", [], "Open", None, [])]
    # game_state.npcs = [NPC("John Doe", "Friendly", "Alive", ["Key"], ["solve_puzzle"]),
    #                    NPC("Jane Doe", "Mysterious", "Alive", ["Map"], ["unlock_door"])]
    # game_state.puzzles = [Puzzle("solve_puzzle", "Solve the puzzle to unlock the door", "Locked", "Key", "use")]
    # game_state.items = [Item("Key", "A shiny key", "Inactive")]
    # game_state.player = Player("Player 1", 100, [])

    # Call the signalChange method to indicate a change in the game state
    # game_state.signalChange()


test = GameState()
test.populateWorld()

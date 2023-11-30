from gameLoader import GameLoader
from room import Room

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

        # print(self.npc_dict["npc_player"].inventory)

    def keyToObject(self, beingFilled, pool):
        # print("-" * 20)
        # get individual npc/room/etc whose inv needs to be filled
        for model in beingFilled.values():
            # print(model.name)
            tmpList = []

            for thing_name in model.inventory:
                if thing_name is None:
                    break

                true_obj = pool[thing_name]
                # print(true_obj.name)
                tmpList.append(true_obj)

            model.inventory.clear()
            model.inventory.extend(tmpList)
            # print(model.inventory)

    def fillRooms(self, room_dict, pool):
        for room in room_dict.values():
            # print(">>>> ", room.name)
            for direction in room.connected_to:
                # fill out connected to
                connected_room_name = room.connected_to[direction]
                if connected_room_name is not None:
                    true_room = room_dict[connected_room_name]
                else:
                    true_room = None
                room.connected_to[direction] = true_room

                # fill out doors
                door_name = room.associated_door[direction]
                if door_name is not None:
                    true_door = pool[door_name]
                else:
                    true_door = None
                room.associated_door[direction] = true_door

            # print(room.connected_to)
            # print(room.associated_door)

    def populateWorld(self):
        pool = {**self.item_dict, **self.puzzle_dict}  # merge the dictionaries
        # print(pool)

        # 1) fill NPC inventories with items + puzzles
        self.keyToObject(self.npc_dict, pool)
        # print(self.npc_dict["npc_lia"].inventory)
        # print(">>> npc filled")

        # 2) fill room inventories with NPCs, items, + puzzles (doors + others)
        pool.update(self.npc_dict)
        self.keyToObject(self.room_dict, pool)
        self.fillRooms(self.room_dict, pool)

        # return updated room dictionary
        return self.room_dict

    def getPlayer(self):
        return self.npc_dict["npc_player"]

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


#test = GameState()
#rooms = test.populateWorld()
#print(rooms["room_armory"].describeRoom())
# print(rooms.get("room_Hangar").associated_door)

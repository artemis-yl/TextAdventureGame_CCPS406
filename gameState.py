from gameLoader import GameLoader
from modelClasses import Room

FILE_NAME_LIST = [
    "JSON/npcs.json",
    "JSON/room.json",
    "JSON/items.json",
    "JSON/puzzles.json",
    "JSON/gameMsg.json",
    "JSON/commands.json",
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

    # ========================== COMMAND/VERB RELATED METHODS ============================

    # moves an NPC from one room to another.
    # this method assumes the rooms are connected, the NPC is in the room, and the NPC can move there
    # target_room is the actual room object
    def move(self, npc_name, target_room):
        # get the NPC object and its current room object
        npc = self.npc_dict[npc_name]
        current_room = self.room_dict[npc.getLocation()]

        current_room.removeNPC()

        pass

    # =====================================================================================

    # This method converts the inventories of all NPCs + Rooms into dictionaries
    # that points to the actual item/puzzle/npc object
    # Also converts puzzle's key into the actual object
    def populateWorld(self):
        # fill puzzle keys
        self.keyToObject()

        pool = {**self.item_dict, **self.puzzle_dict}  # merge the dictionaries
        # print(pool)

        # 1) fill NPC inventories with items + puzzles
        self.fillInv(self.npc_dict, pool)
        # print(self.npc_dict["npc_lia"].inventory)
        # print(">>> npc filled")

        # 2) fill room inventories with NPCs, items, + puzzles (doors + others)
        pool.update(self.npc_dict)
        self.fillInv(self.room_dict, pool)
        self.fillRooms(self.room_dict, pool)

        # return updated room dictionary
        return self.room_dict

    # converts the inventory from a list of strings(keys) to dictionary of objects
    def fillInv(self, beingFilled, pool):
        # print("-" * 20)
        # get individual npc/room/etc whose inv needs to be filled
        for model in beingFilled.values():
            # print(model.name)
            tmp = {}

            for thing_name in model.inventory:
                if thing_name is None:
                    break

                true_obj = pool[thing_name]
                # print(true_obj.name)
                tmp[true_obj.getName()] = true_obj

            model.inventory = tmp
            # print(model.inventory)

    # specifically handles the room's doors and connecting rooms
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

    # specifically handles converting a puzzle's key from a string to an object
    def keyToObject(self):
        for puzzle in self.puzzle_dict.values():
            item = self.item_dict[puzzle.getKey()]
            puzzle.setKey(item)
            # print(puzzle.getKey())

    def getPlayer(self, npc_name):
        return self.npc_dict[npc_name]

    def getCommands(self):
        return self.command_dict

    def getMsgs(self):
        return self.msg_dict

    def save(self):
        pass
        # call gameSaver to save data


#test = GameState()
#rooms = test.populateWorld()
# print(rooms.get("room_Hangar").associated_door['S'])
#print(rooms["room_security"].inventory)
# print(rooms["room_armory"].describeRoom())
# print(rooms.get("room_Hangar").associated_door)

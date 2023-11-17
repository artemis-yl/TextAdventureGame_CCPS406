import json
from npc import NPC
from room import Room
from item import Item
from puzzle import Puzzle

class GameLoader:
    def __init__(self, npc_filename, room_filename, items_filename, puzzles_filename):
        # Constructor to initialize the file names
        self.npc_filename = npc_filename
        self.room_filename = room_filename
        self.items_filename = items_filename
        self.puzzles_filename = puzzles_filename

    def loadGame(self):
        # Method to load the game data
        npc_list = self.import_npc()
        room_list = self.import_rooms()
        item_list = self.import_items()
        puzzle_list = self.import_puzzles()

        return npc_list, room_list, item_list, puzzle_list

    def import_npc(self):
        # Method to import NPC data from JSON
        with open(self.npc_filename, 'r') as npc_json:
            data = json.load(npc_json)

        npc_list = []

        for npc_data in data['npcs']:
            npc_list.append(
            NPC
            (
                    npc_data["name"],
                    npc_data.get("initialState"),
                    npc_data.get("stateDescriptions"),  
                    npc_data.get("isActive"),
                    npc_data.get("isRoaming"),
                    npc_data.get("initialInventory"),
                    npc_data.get("puzzleList")
            )
            )

        return npc_list

    def import_rooms(self):
        # Method to import room data from JSON
        with open(self.room_filename, 'r') as room_json:
            data = json.load(room_json)

        room_list = []

        for room_data in data['rooms']:
            room_list.append(
            Room
            (
                room_data["name"],
                room_data["description"],
                room_data["connectedTo"],
                room_data["associatedDoor"],
                room_data["initialInventory"],
                room_data["npc"]
            )
            )

        return room_list

    def import_items(self):
        # Method to import item data from JSON
        with open(self.items_filename, 'r') as item_json:
            data = json.load(item_json)

        item_list = []

        for item_data in data['items']:
            item_list.append(
            Item
            (
                item_data["name"],
                item_data["stateDescriptions"],
                item_data["currentState"],
                [
                item_data["isWeapon"],
                item_data["isShield"],
                item_data["isTeleporter"],
                item_data["isRevive"]
                ]
            )
            )

        return item_list

    def import_puzzles(self):
        # Method to import puzzle data from JSON
        with open(self.puzzles_filename, 'r', encoding='utf-8') as puzzle_json:
            data = json.load(puzzle_json)

        puzzle_list = []

        for puzzle_data in data['puzzles']:
            puzzle_list.append(
            Puzzle
            (
                puzzle_data["name"], 
                puzzle_data["stateDescriptions"], 
                puzzle_data["currentState"], 
                puzzle_data["key"], 
                puzzle_data["keyVerb"], 
                puzzle_data["hints"], 
                puzzle_data["subPuzzles"]
            
            )
            )
        
        return puzzle_list
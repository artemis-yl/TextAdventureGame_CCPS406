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
        npc = self.import_npc()
        room_list = self.import_rooms()
        item_list = self.import_items()
        puzzle_list = self.import_puzzles()

        # Initialize game using the loaded data
        # For example, might create instances of game objects and set up the game state.

    def import_npc(self):
        # Method to import NPC data from JSON
        with open(self.npc_filename, 'r') as npc_json:
            data = json.load(npc_json)

        return NPC(data['name'], data['state_descriptions'], data['initial_state'],
                   data['initial_inventory'], data['puzzle_list'])

    def import_rooms(self):
        # Method to import room data from JSON
        with open(self.room_filename, 'r') as room_json:
            data = json.load(room_json)

        room_list = []

        for room_data in data['rooms']:
            room = Room(room_data['name'], room_data['description'], room_data['connected_to'],
                        room_data['initial_door_state'], room_data['associated_door'], room_data['initial_inventory'])

            room_list.append(room)

        return room_list

    def import_items(self):
        # Method to import item data from JSON
        with open(self.items_filename, 'r') as item_json:
            data = json.load(item_json)

        item_list = []

        for item_data in data['items']:
            item = Item(item_data['name'], item_data['state_descriptions'], item_data['initial_state'])

            item_list.append(item)

        return item_list

    def import_puzzles(self):
        # Method to import puzzle data from JSON
        with open(self.puzzles_filename, 'r') as puzzle_json:
            data = json.load(puzzle_json)

        puzzle_list = []

        for puzzle_data in data['puzzles']:
            puzzle = Puzzle(puzzle_data['name'], puzzle_data['state_descriptions'], puzzle_data['initial_state'],
                            puzzle_data['key'], puzzle_data['key_verb'])

            puzzle_list.append(puzzle)

        return puzzle_list

    # Example Usage:
    # loader = GameLoader('npc_data.json', 'room_data.json', 'item_data.json', 'puzzle_data.json')
    # loader.loadGame()

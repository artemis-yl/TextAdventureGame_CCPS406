import json
from npc import NPC
from room import Room
from item import Item
from puzzle import Puzzle


class GameLoader:
    def __init__(self, file_name_list):
        # Constructor to initialize the file names
        self.npc_filename = file_name_list[0]
        self.room_filename = file_name_list[1]
        self.items_filename = file_name_list[2]
        self.puzzles_filename = file_name_list[3]
        self.messages_filename = file_name_list[4]
        self.commands_filename = file_name_list[5]

    def loadGame(self):
        # Method to load the game data
        npc_dict = self.import_npcs()
        room_dict = self.import_rooms()
        item_dict = self.import_items()
        puzzle_dict = self.import_puzzles()
        message_dict = self.import_messages()
        cmd_dict = self.import_commands()

        return [npc_dict, room_dict, item_dict, puzzle_dict, message_dict, cmd_dict]

    def import_commands(self):
        pass

    def import_npcs(self):
        # Method to import npcs
        with open(self.npc_filename, "r") as file:
            npc_data = json.load(file)

        npc_dict = {}

        for npc_key, npc_d in npc_data.items():
            npc_instance = NPC(npc_d)
            npc_dict[npc_key] = npc_instance

        return npc_dict

    def import_rooms(self):
        # Method to import rooms
        with open(self.room_filename, "r") as file:
            room_data = json.load(file)

        room_dict = {}

        for room_key, room_d in room_data.items():
            room_instance = Room(room_d)
            room_dict[room_key] = room_instance

        return room_dict

    def import_items(self):
        # Method to import items
        with open(self.items_filename, "r") as item_json:
            data = json.load(item_json)

        item_dict = {}

        for item_key, item_data in data.items():
            item_instance = Item(item_data)
            item_dict[item_key] = item_instance

        return item_dict

    def import_puzzles(self):
        # Method to import puzzles
        with open(self.puzzles_filename, "r", encoding="utf-8") as puzzle_json:
            data = json.load(puzzle_json)

        puzzle_dict = {}

        for puzzle_key, puzzle_data in data.items():
            puzzle_instance = Puzzle(puzzle_data)
            puzzle_dict[puzzle_key] = puzzle_instance

        return puzzle_dict

    def import_messages(self):
        # Method to import messages
        with open(self.messages_filename, "r") as message_json:
            data = json.load(message_json)

        messages_dict = {}

        for message_key, message_data in data.items():
            messages_dict[message_key] = message_data

        return messages_dict

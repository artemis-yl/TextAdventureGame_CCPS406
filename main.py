import math
import json
from mechanics import *


def import_npcs(npc_filename):
    with open(npc_filename, 'r') as npc_json:
        data = json.load(npc_json)

    npc_list = []

    for npc_data in data['npcs']:
        npc = Character(npc_data['name'], npc_data['state_descriptions'], npc_data['initial_state'],
                        npc_data['initial_inventory'], npc_data['puzzle_list'])

        npc_list.append(npc)

    return npc_list


def import_rooms(room_filename):
    with open(room_filename, 'r') as room_json:
        data = json.load(room_json)

    room_list = []

    for room_data in data['rooms']:
        room = Room(room_data['name'], room_data['description'], room_data['connected_to'],
                    room_data['initial_door_state'], room_data['associated_door'], room_data['initial_inventory'])

        room_list.append(room)

    return room_list


def import_items(items_filename):
    with open(items_filename, 'r') as item_json:
        data = json.load(item_json)

    item_list = []

    for item_data in data['items']:
        item = Item(item_data['name'], item_data['state_descriptions'], item_data['initial_state'])

        item_list.append(item)

    return item_list


def import_puzzles(puzzles_filename):
    with open(puzzles_filename, 'r') as puzzle_json:
        data = json.load(puzzle_json)

    puzzle_list = []

    for puzzle_data in data['puzzles']:
        puzzle = Puzzle(puzzle_data['name'], puzzle_data['state_descriptions'], puzzle_data['initial_state'],
                        puzzle_data['key'], puzzle_data['key_verb'])

        puzzle_list.append(puzzle)

    return puzzle_list


npc_dir = 'npc_data.json'
npc_list = import_npcs(npc_dir)

for i in npc_list:
    print(i.name)

room_dir = 'room_data.json'
room_list = import_rooms(room_dir)

for i in room_list:
    print(i.name)

item_dir = 'item_data.json'
item_list = import_items(item_dir)

for i in item_list:
    print(i.name)

puzzle_dir = 'puzzle_data.json'
puzzle_list = import_puzzles(puzzle_dir)

for i in puzzle_list:
    print(i.name)

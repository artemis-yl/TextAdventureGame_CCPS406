import json
from modelClasses import NPC, Room, Item, Puzzle

class GameSaver:
    def __init__(self, npc_filename, room_filename, items_filename, puzzles_filename):
        # Constructor to initialize the file names
        self.npc_filename = npc_filename
        self.room_filename = room_filename
        self.items_filename = items_filename
        self.puzzles_filename = puzzles_filename

    def saveData(self, npc, rooms, items, puzzles):
        # Save NPC data
        npc_data = {
            'name': npc.name,
            'state_descriptions': npc.state_descriptions,
            'initial_state': npc.initial_state,
            'initial_inventory': npc.initial_inventory,
            'puzzle_list': npc.puzzle_list
        }
        self._save_to_file(self.npc_filename, {'npc': npc_data})

        # Save Room data
        room_data = [{'name': room.name,
                      'description': room.description,
                      'connected_to': room.connected_to,
                      'initial_door_state': room.initial_door_state,
                      'associated_door': room.associated_door,
                      'initial_inventory': room.initial_inventory} for room in rooms]
        self._save_to_file(self.room_filename, {'rooms': room_data})

        # Save Item data
        item_data = [{'name': item.name,
                      'state_descriptions': item.state_descriptions,
                      'initial_state': item.initial_state} for item in items]
        self._save_to_file(self.items_filename, {'items': item_data})

        # Save Puzzle data
        puzzle_data = [{'name': puzzle.name,
                        'state_descriptions': puzzle.state_descriptions,
                        'initial_state': puzzle.initial_state,
                        'key': puzzle.key,
                        'key_verb': puzzle.key_verb} for puzzle in puzzles]
        self._save_to_file(self.puzzles_filename, {'puzzles': puzzle_data})

        print("Game data saved successfully.")

    def loadData(self):
        # Load NPC data
        npc_data = self._load_from_file(self.npc_filename)['npc']
        npc = NPC(npc_data['name'],
                  npc_data['state_descriptions'],
                  npc_data['initial_state'],
                  npc_data['initial_inventory'],
                  npc_data['puzzle_list'])

        # Load room data
        room_data = self._load_from_file(self.room_filename)['rooms']
        rooms = [Room(data['name'], data['description'], data['connected_to'],
                      data['initial_door_state'], data['associated_door'], data['initial_inventory']) for data in room_data]

        # Load item data
        item_data = self._load_from_file(self.items_filename)['items']
        items = [Item(data['name'], data['state_descriptions'], data['initial_state']) for data in item_data]

        # Load puzzle data
        puzzle_data = self._load_from_file(self.puzzles_filename)['puzzles']
        puzzles = [Puzzle(data['name'], data['state_descriptions'], data['initial_state'],
                          data['key'], data['key_verb']) for data in puzzle_data]

        print("Game data loaded successfully.")

        return npc, rooms, items, puzzles

    def _save_to_file(self, filename, data):
        # Utility method to save data to a JSON file
        with open(filename, 'w') as file:
            json.dump(data, file, indent=2)

    def _load_from_file(self, filename):
        # Utility method to load data from a JSON file
        with open(filename, 'r') as file:
            return json.load(file)
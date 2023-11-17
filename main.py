import gameLoader
import gameSaver

loader = gameLoader.GameLoader('npcs.json', 'room.json', 'items.json', 'puzzles.json')
npc_list, room_list, item_list, puzzle_list = loader.loadGame()



print("-" * 50)
print("NPCS")
print("-" * 50)
for npc in npc_list:
    print(f"NPC Name: {npc.npc_id}")
    print(f"Current State: {npc.current_state}")
    print(f"Active: {npc.is_active}")
    print(f"Roaming: {npc.is_roaming}")
    print(f"Initial Inventory: {npc.initial_inventory}")
    print(f"Puzzle List: {npc.puzzle_list}")
    print(f"\n")


print("-" * 50)
print("ITEMS")
print("-" * 50)
for item in item_list:
    print(f"Item Name: {item.getName()}")
    print(f"Description: {item.getDescription()}")
    print(f"Is Weapon: {item.isWeapon()}")
    print(f"Is Shield: {item.isShield()}")
    print(f"Is Teleport: {item.isTeleport()}")
    print(f"Is Revive: {item.isRevive()}")
    print("\n")



print("-" * 50)
print("ROOMS")
print("-" * 50)
for room in room_list:
    print(f"Room Name: {room.room_name}")
    print(f"Description: {room.description}")
    print(f"Connected To: {room.connected_to}")
    print(f"Associated Door: {room.associated_door}")
    print(f"Initial Inventory: {room.initial_inventory}")
    print("\n")


print("-" * 50)
print("PUZZLES")
print("-" * 50)
for puzzle in puzzle_list:
    print(f"Puzzle Name: {puzzle.name}")
    print(f"Descriptions: {puzzle.stateDescriptions}")
    print(f"Current State: {puzzle.currentState}")
    print(f"Key: {puzzle.key}")
    print(f"Verb: {puzzle.keyVerb}")
    print(f"Hints: {puzzle.hints}")
    print(f"SubPuzzles: {puzzle.subPuzzles}")
    print("\n")
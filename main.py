import gameLoader
import gameSaver

loader = gameLoader.GameLoader('npcs.json', 'room.json', 'items.json', 'puzzles.json', 'gameMsg.json')
npc_dict, room_dict, item_dict, puzzle_dict, message_dict = loader.loadGame()


print("-" * 50)
print("NPCS")
print("-" * 50)
for npc_key, npc_instance in npc_dict.items():
    print(f"NPC Name: {npc_instance.name}")
    print(f"Current State: {npc_instance.current_state}")
    print(f"Descriptions: {npc_instance.state_descriptions}")
    print(f"Active: {npc_instance.is_active}")
    print(f"Roaming: {npc_instance.is_roaming}")
    print(f"Initial Inventory: {npc_instance.inventory}")
    #print(f"Puzzle List: {npc_instance.puzzle_list}")  
    print(f"\n")

print("-" * 50)
print("ITEMS")
print("-" * 50)
for item_key, item_instance in item_dict.items():
    print(f"Item Name: {item_instance.name}")
    print(f"Current State: {item_instance.current_state}")
    print(f"Descriptions: {item_instance.state_descriptions}")
    print(f"Is Weapon: {item_instance.isWeapon()}")
    print(f"Is Shield: {item_instance.isShield()}")
    print(f"Is Teleport: {item_instance.isTeleport()}")
    print(f"Is Revive: {item_instance.isRevive()}")
    print("\n")


print("-" * 50)
print("ROOMS")
print("-" * 50)
for room_key, room_instance in room_dict.items():
    print(f"Room Name: {room_instance.name}")
    print(f"Description: {room_instance.state_descriptions}")
    print(f"Connected To: {room_instance.connected_to}")
    print(f"Associated Door: {room_instance.associated_door}")
    print(f"Inventory: {room_instance.inventory}")
    print("\n")


print("-" * 50)
print("PUZZLES")
print("-" * 50)
for puzzle_key, puzzle_instance in puzzle_dict.items():
    print(f"Puzzle Name: {puzzle_instance.name}")
    print(f"Descriptions: {puzzle_instance.state_descriptions}")
    print(f"Current State: {puzzle_instance.current_state}")
    print(f"Key: {puzzle_instance.key}")
    print(f"Verb: {puzzle_instance.keyVerb}")
    print("\n")

print("-" * 50)
print("MESSAGES")
print("-" * 50)
for message_name, message_data in message_dict.items():
    print(f"{message_name}: {message_data}")
    print("\n")

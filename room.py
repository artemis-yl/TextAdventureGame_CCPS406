from container import ContainterModel


class Room(ContainterModel):
    def __init__(self, room):
        super().__init__(
            self,
            room["name"],
            room["description"],
            room["initialInventory"],
        )

        self.connected_to = room["connectedTo"]
        self.associated_door = room["associatedDoor"]
        self.inventory = room["initialInventory"]

    def getConnectedRooms(self):
        return self.connected_to

    def getAssociatedDoor(self):
        return self.associated_door

    def addNPC(self, npc):
        self.inventory.append(npc)

    def removeNPC(self, npc):
        if npc in self.inventory:
            self.inventory.remove(npc)
        else:
            print(f"{npc.name} is not inside {self.name}")

    def __str__(self):
        return f"Room Name: {self.name}"

    def __repr__(self):
        return f"Room Name: {self.name}"


"""
# Load room data from file
with open("room.json", 'r') as room_file:
    room_data = json.load(room_file)
    room_instances = {}

    for room_id, room_info in room_data.items():
        room_instances[room_id] = Room(
            room_info["name"],
            room_info["description"],
            room_info["connectedTo"],
            room_info["associatedDoor"],
            room_info["initialInventory"]
            room_info["npc"]
        )
# Example usage...
# Access and manipulate the Room instances
for room_id, room in room_instances.items():
    print(f"Room ID: {room_id}")
    print(f"Room Name: {room.room_name}")
    print(f"Description: {room.description}")
    print(f"Connected To: {room.connected_to}")
    print(f"Associated Door: {room.associated_door}")
    print(f"Initial Inventory: {room.initial_inventory}")
    print("\n")
"""

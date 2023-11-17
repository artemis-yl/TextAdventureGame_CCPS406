class Room:
    def __init__(self, room_name, description, connected_to,associated_door,initial_inventory,npc):
        self.room_name = room_name
        self.description = description
        self.connected_to = connected_to
        self.associated_door = associated_door
        self.initial_inventory=initial_inventory
        self.npcs_inside=[]
        self.state = None

    def getRoomName(self):
        return self.room_name

    def getConnectedRooms(self):
        return self.connected_to

    def getState(self):
        return self.state

    def setState(self, new_state):
        self.state = new_state

    def getAssociatedDoor(self):
        return self.associated_door

    def getInitialInventory(self):
        return self.initial_inventory

    def addNPC(self, npc):
        self.npcs_inside.append(npc)

    def removeNPC(self, npc):
        if npc in self.npcs_inside:
            self.npcs_inside.remove(npc)
        else:
            print(f"{npc.npc_id} is not inside {self.room_name}")

    def __str__(self):
        return f"Room Name: {self.room_name}"
    
    def __repr__(self):
        return f"Room Name: {self.room_name}"
    
'''
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
'''
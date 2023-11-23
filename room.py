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
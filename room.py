from container import ContainterModel


class Room(ContainterModel):
    def __init__(self, room):
        super().__init__(room["name"], room["description"], room["initialInventory"])

        self.connected_to = room["connectedTo"]
        self.associated_door = room["associatedDoor"]
        self.inventory = room["initialInventory"]
        self.entered_before = False

    def hasEntered(self):
        self.entered_before = True

    def scan(self):
        return self.listInventory()

    # might remove
    def describeRoom(self):
        if self.entered_before is False:
            room_description = self.getStateDescription("firstEntry")
            self.entered_before = True
        else:
            room_description = self.getStateDescription("rentry")

        door_description = self.describeDoors()
        item_description = self.describeItems()

        return room_description + "\n\n" + door_description + "\n"  # + item_description

    def describeItems(self):
        itemNum = len(self.inventory)
        if itemNum == 0:
            description = "This room is empty of any people or thing."
        elif itemNum == 1:
            description = "There is something in the room: " + self.inventory[0].name
        else:
            description = (
                "There are "
                + str(itemNum)
                + " things in the room: "
                + self.listInventory()
            )

        return description

    def describeDoors(self):
        connection_count = 0

        # get number of connected rooms an dlist their directions
        connections = []
        for direction in self.connected_to:
            room = self.connected_to[direction]

            if room is not None:
                connection_count += 1
                connections.append(direction.upper())

        if len(connections) > 1:
            semiString = ", ".join(connections[:-1]) + ", and " + connections[-1]
            # print("SEMI STRING : " + semiString)
            description = (
                "There are "
                + str(connection_count)
                + " doors in the room. They are to the "
                + semiString
                + "."
            )
        else:
            description = (
                "There is 1 door in the room. It is to the " + connections[0] + "."
            )

        return description

    def getConnectedRooms(self):
        return self.connected_to

    def getAssociatedDoor(self, key):
        return self.associated_door[key]

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

from container import ContainterModel
from puzzle import Puzzle


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

    # will look for the puzzle in the room's inv, and try to solve it
    # will return false is the puzzle DNE or key doesn't match it
    def tryPuzzle(self, keyItem):
        check = False # will become true IF a puzzle has been found and solved

        for thing in self.inventory.values():
            if isinstance(thing, Puzzle):
                check = check or thing.tryToSolve(keyItem)

        return check

    # returns false is no puzzle door exists, OR all doors already unlocked
    def tryOpeningDoors(self, keyItem):
        check = False  # will stay false unless a door was unlocked

        for door in self.associated_door.values():
            if door is not None:  # a door exists
                if door.getCurrentState() == "solved":  # if already open move on
                    continue
                check = check or door.tryToSolve(keyItem)

        return check

    # creates a formatted string of the room description and of the doors
    def describeRoom(self):
        if self.entered_before is False:
            room_description = self.getStateDescription("firstEntry")
            self.entered_before = True
        else:
            room_description = self.getStateDescription("rentry")

        return room_description + "\n\n" + self.describeDoors() + "\n"

    # created a formatted string that described the items in the room
    # CURRENTLY UNUSED
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

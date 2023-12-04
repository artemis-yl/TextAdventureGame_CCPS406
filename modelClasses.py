class ContainterModel:
    def __init__(self, name, states, inventory) -> None:
        # self.id = id #string
        self.name = name  # string
        # this is a list of strings, if only one it will be a list of 1 element
        # the subclasses will describe which index holds what kind of description
        self.state_descriptions = states  # dictionary
        self.inventory = inventory  # list

    # pythonically, no true data encapsulation, therefore no real need for setter/getters
    # shall include anyway, for now

    # both, name and ID will never change so no need to have setters
    def getName(self):
        return self.name

    def getID(self):
        return self.id

    # will give you the object
    def getObject(self, obj_name):
        # print(obj_name)
        # print(self.inventory)
        if obj_name in self.inventory:
            return self.inventory[obj_name]
        return None

    # unlike above, need the actual object ref and not a string of its name
    def removeObject(self, object):
        # print("before : ", self.inventory)
        if object in self.inventory.values():
            self.inventory.pop(object.getName())
            # print(self.inventory)
            return True
        return False

    def addToInv(self, obj):
        self.inventory[obj.getName()] = obj

    def getInv(self):
        return self.inventory

    def setInv(self, invList):
        self.inventory = invList

    def getStateDescription(self, state_key):
        return self.state_descriptions[state_key]

    # utility method that's really useful
    def listToGrammarString(self, list):
        if len(list) > 1:
            formatted = ", ".join(list[:-1]) + ", and " + list[-1]
        elif len(list):
            formatted = list[0]
        else:
            formatted = "empty"

        return formatted

    # useful for all  command method
    def listInventory(self):
        str_list = []
        for item in self.inventory.values():
            str_list.append(item.name)

        if str_list == []:
            return None
        return self.listToGrammarString(str_list)


# =================================================================================================


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

    # will check if the txt string has a substring with the object's name in it
    def isItThere(self, txt, dict):
        for obj in dict.values():
            if obj.getName() in txt:
                return True

        return False

    # will look for the puzzle in the room's inv, and try to solve it
    # will return false is the puzzle DNE or key doesn't match it
    def tryPuzzle(self, keyItem):
        check = False  # will become true IF a puzzle has been found and solved

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

    def addNPC(self, npc_obj):
        self.addToInv(npc_obj)

    def removeNPC(self, npc_obj):
        return self.removeObject(npc_obj)

    def __str__(self):
        return f"Room Name: {self.getName()}"

    def __repr__(self):
        return f"Room Name: {self.getName()}"


# =================================================================================================
class Puzzle(ContainterModel):
    def __init__(self, puzzle):
        super().__init__(
            puzzle["name"], puzzle["stateDescriptions"], puzzle["subPuzzles"]
        )

        self.current_state = puzzle["currentState"]
        self.key = puzzle["key"]
        self.keyVerb = puzzle["keyVerb"]

    def tryToSolve(self, keyItem):
        # print(self.key, keyItem)
        if self.key == keyItem:
            self.current_state = "solved"
            return True
        else:
            return False

    def getSubPuzzles(self):
        return self.getInv()

    def getCurrentState(self):
        return self.current_state

    def setCurrentState(self, currentState):
        self.current_state = currentState

    def getKey(self):
        return self.key

    def setKey(self, keyObj):
        self.key = keyObj

    def getKeyVerb(self):
        return self.keyVerb


# =================================================================================================


class NPC(ContainterModel):
    def __init__(self, npc):
        super().__init__(npc["name"], npc["stateDescriptions"], npc["initialInventory"])

        self.dialogue = npc["dialogue"]
        self.current_state = npc["initialState"]
        self.is_active = npc["isActive"]
        self.is_roaming = npc["isRoaming"]
        self.location = npc["location"]

    def getLocation(self):
        return self.location

    # location name is the STRING key
    def setLocation(self, location_name):
        self.location = location_name

    def getPuzzleState(self):
        pass

    # check if the given key and command are correct
    # TO BE CHANGED
    def tryPuzzle(self, command):
        key = self.puzzle.getKey()
        key_cmd = self.puzzle.getKeyVerb()
        if key in self.inventory and key_cmd == command:
            self.puzzle.solve()

    def getState(self):
        return self.current_state

    def setState(self, new_state):
        if new_state in self.possible_states:
            self.current_state = new_state
            print(f"{self.npc_id} is now in state: {new_state}")
        else:
            print(f"Error: {new_state} is not a valid state for {self.npc_id}")

    def getDialogue(self):
        return self.dialogue

    def checkIfActive(self):
        return self.is_active

    def setActivity(self, is_active):
        self.is_active = is_active
        activity = "active" if is_active else "inactive"
        print(f"{self.npc_id} is now {activity}")

    def checkIfRoaming(self):
        return self.is_roaming

    def setRoaming(self, is_roaming):
        self.is_roaming = is_roaming
        roaming_status = "roaming" if is_roaming else "not roaming"
        print(f"{self.npc_id} is now {roaming_status}")


# =================================================================================================


class Item(ContainterModel):
    def __init__(self, item):
        super().__init__(item["name"], item["stateDescriptions"], [None])

        self.current_state = item["currentState"]
        self.is_purpose = item["is_purpose"]  # [Weapon, Shield, Teleporter, Revive]

    # needs to be overriden in a subclass for weapon, revive, teleporter, etc
    # will currently return True to indicate item is only a puzzle's key
    def use(self):
        return True

    def isWeapon(self):
        return self.is_purpose[0]  # Override if the item is a weapon

    def isShield(self):
        return self.is_purpose[1]  # Override if the item is a shield

    def isRevive(self):
        return self.is_purpose[2]  # Override if the item is for revival

    def isTeleport(self):
        return self.is_purpose[3]  # Override if the item is for teleportation

    def setState(self, new_state):
        self.current_state = new_state

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"

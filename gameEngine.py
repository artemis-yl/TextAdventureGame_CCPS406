import view, gameState


class GameEngine:
    def __init__(self) -> None:
        self.turn_counter = 0
        self.data_needed = [None]
        self.data_TBChanged: [None]

        self.gameState = gameState.GameState()

        self.filled_rooms = self.gameState.populateWorld()
        self.current_room = self.filled_rooms["room_Hangar"]
        self.player = self.gameState.getPlayer()
        self.player_status = True
        cmd_list = [ cmds for cmds in self.gameState.command_dict ]
        #print(cmd_list)
        self.commands = self.player.listToGrammarString(cmd_list )  # list of command strings

        self.inHandler = view.InputHandler()
        self.outHandler = view.OutputHandler(
            self.gameState.command_dict, self.gameState.msg_dict
        )

    def executeCommand(self):
        # to use method,type COMMANDS[key]( parameter )
        COMMANDS = {
            """
            "N": self.N,
            "S": self.S,
            "E": self.E,
            "W": self.W,
            """
            "SAY": self.say,
            "MOVE": self.move,  # done
            "EXIT": self.exit,
            "ATTACK": self.attack,
            "SCAN": self.scan,  # done
            "INVENTORY": self.listInventory,  # done
            "USE": self.use,
            "TAKE": self.take,  # (item_to_take)
            "TALK": self.talk,
            "LOCATION": self.location,  # done
            "DISCARD": self.discard,
            "SAVE": self.gameState.save,
            "HELP": self.listCommands,
        }
        # some of these will call the method from the appropriate object (container, room, etc)
        # but then get additional paramters when sent to outputHandler

        # get the input from user/player
        self.inHandler.parseInput()
        verb = self.inHandler.getVerb()
        keyword1 = self.inHandler.getFirstKeyword()
        keyword2 = self.inHandler.getSecondKeyword()

        objectList = []

        # check dictionary of commands to see which correct action to take
        if verb.upper() in COMMANDS:
            if keyword1 == "":
                # need to handle parameters somehow but do that later....
                COMMANDS[verb.upper()]()
            elif keyword2 == "":
                COMMANDS[verb.upper()](keyword1)
                objectList.append(keyword1)
            else:  # unlikely to occure since game atm is very simple
                COMMANDS[verb.upper()](keyword1, keyword2)
                objectList.append(keyword1)
                objectList.append(keyword2)
        else:
            self.outHandler.appendToBuffer("Invalid input, please try again.")

        self.outHandler.displayOutput()

    def startGame(self):
        pass
        # print introduction

    # all command methods below - limited to 2 parameters AKA keyword
    # returns the new current room

    def basicOutputCall(self, toBeInserted, verb):
        if toBeInserted is None:
            self.outHandler.formatOutput(verb, "failure", [])
        else:
            self.outHandler.formatOutput(verb, "success", [toBeInserted])

    def move(self, direction="x"):
        direction = direction.upper()  # to match keys

        # print(self.current_room.name, direction)

        # get rid of invalid input
        if direction.upper() not in ["N", "E", "W", "S"]:
            return " That's not a valid direction. "

        # get the door + room to move to
        door = self.current_room.getAssociatedDoor(direction)
        new_room = self.current_room.getConnectedRooms().get(direction)

        if door is not None:  # aka there is a room there but a puzzle exists
            if door.current_state == "solved":
                self.current_room = new_room
                self.moveSuccess()
            elif door.current_state == "unsolved":
                self.moveFailure(new_room.getName())
        elif new_room is not None:  # no puzzle door, but room exists
            self.current_room = new_room
            self.moveSuccess()
        elif new_room is None:
            self.moveFailure("a room that doesn't exist")

    def moveFailure(self, targeted_room_name):
        # if you cannot move to that room
        # "failure": "You can't move to <>"
        self.outHandler.formatOutput("MOVE", "failure", [targeted_room_name])

    def moveSuccess(self):
        # if you successfuly move to a new room, you saythe success move msg + describe new room
        # "success": "You moved to <>",
        self.outHandler.formatOutput("MOVE", "success", [self.current_room.getName()])
        self.outHandler.appendToBuffer(self.current_room.describeRoom())

    def scan(self):
        objects = self.current_room.scan()  # aka the room's inventory
        self.basicOutputCall(objects, "SCAN")

    def listInventory(self):
        invString = self.player.listInventory()
        self.basicOutputCall(invString, "INVENTORY")

    def say(self):
        pass

    def attack(self):
        pass

    def use(self):
        pass

    def take(self):
        pass

    def talk(self):
        pass

    def location(self):
        self.basicOutputCall(self.current_room.getName(), "LOCATION")

    def discard(self):
        pass

    def save(self):
        pass

    def listCommands(self):
        self.outHandler.formatOutput("HELP", "success", [self.commands])

    def exit(self):
        pass

    def itemUseFail():
        print("Nothing happens.")

    def findThing(self, key, dict):
        if key in dict:
            return dict[key]
        return None

    def findItem(self, item_name, items_dict):
        return self.findThing(item_name, items_dict)

    def findRoom(self, room_name, room_dict):
        return self.findThing(room_name, room_dict)

    def findPuzzle(self, puzzle_name, puzzle_dict):
        return self.findThing(puzzle_name, puzzle_dict)

    def unlockAllDoors(room_dict):
        for room in room_dict.values():
            connections = room.associated_door

            for door in connections:
                if door is None:
                    continue
                else:
                    door.current_state = "solved"


test = GameEngine()
test.executeCommand()

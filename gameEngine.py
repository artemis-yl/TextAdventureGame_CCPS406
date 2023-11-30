import view, gameState


class GameEngine:
    def __init__(self) -> None:
        self.player_status = True
        self.turn_counter = 0
        self.data_needed = [None]
        self.data_TBChanged: [None]

        self.gameState = gameState.GameState()

        self.filled_rooms = self.gameState.populateWorld()
        self.current_room = self.filled_rooms["room_Hangar"]
        self.player = self.gameState.getPlayer()

        self.inHandler = view.InputHandler()
        self.outHandler = view.OutputHandler(
            self.gameState.command_dict, self.gameState.msg_dict
        )

    def executeCommand(self):
        # notes on where these methods should be....

        # N,S,E,W needs to move the player from the current room inventory to the desired room's inventory
        #  will call on currentRoom to check if a room exist and the puzzle/door
        #  => needs to stored HERE in gameEngine
        # ATTACK needs the attacking NPC and target NPC => here in GameEngine
        # LOCATION tells you current room => her ein GameEngine
        # TALK only work on NPC, but the NPC needs to be in the same room as player => here in gameEngine
        # USE requires that the player has the item, and that the target is in the room => here in game engine
        # TAKE can only work on items, but need to place into NPC inv => gameEngine.py
        # HELP list commands which are stored in this class

        # SCAN lists out everything inside the current room's inventory => should be in room.py

        # INVENTORY lists out player inventory => in NPC.py
        # DISCARD is for player to remove an item => in NPC.py

        # maybe change the obj calling the method depending where we actually store the damn methods
        # to use method,type COMMANDS[key]( parameter )
        COMMANDS = {
            """
            "N": self.N,
            "S": self.S,
            "E": self.E,
            "W": self.W,
            """
            "SAY": self.say,
            "MOVE": self.move,
            "EXIT": self.exit,
            "ATTACK": self.attack,
            "SCAN": self.scan,
            "INVENTORY": self.listInventory,
            "USE": self.use,
            "TAKE": self.take,  # (item_to_take)
            "TALK": self.talk,
            "LOCATION": self.location,
            "DISCARD": self.discard,
            "SAVE": self.gameState.save,
            "HELP": self.listCommands,
        }

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
            self.outHandler.formatOutput(verb, "failure", objectList)

    def startGame(self):
        pass
        # print introduction

    # all command methods below - limited to 2 parameters AKA keyword
    # returns the new current room
    def move(self, direction="x"):
        direction = direction.upper()  # to match keys

        print(self.current_room.name, direction)

        # get rid of invalid input
        if direction.upper() not in ["N", "E", "W", "S"]:
            #
            print(" >> invalid direction: cant move there")

        # get the door
        door = self.current_room.getAssociatedDoor(direction)
        print(door.name)
        if door is None:
            pass
        else:
            if door.current_state == "solved":
                self.current_room = self.current_room.getConnectedRooms().get(direction)
            elif door.current_state == "unsolved":
                print(" >> door is locked")

    def say(self):
        pass

    def attack(self):
        pass

    def scan(self):
        pass

    def listInventory(self):
        pass

    def use(self):
        pass

    def take(self):
        pass

    def talk(self):
        pass

    def location(self):
        pass

    def discard(self):
        pass

    def save(self):
        pass

    def listCommands(self):
        pass

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

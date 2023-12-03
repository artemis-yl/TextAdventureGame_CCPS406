import view, gameState
from modelClasses import Item, Puzzle

START_ROOM = "room_Hangar"


class GameEngine:
    def __init__(self) -> None:
        self.turn_counter = 0  # boomb sabotage for example
        self.playing_now = True

        self.gameState = gameState.GameState()

        self.filled_rooms = self.gameState.populateWorld()
        self.current_room = self.filled_rooms[START_ROOM]
        self.player = self.gameState.getPlayer()
        self.player_status = True
        cmd_list = [cmds for cmds in self.gameState.command_dict]
        # print(cmd_list)
        # list of command strings
        self.commands = self.player.listToGrammarString(cmd_list)

        self.inHandler = view.InputHandler()
        self.outHandler = view.OutputHandler(
            self.gameState.getCommands(), self.gameState.getMsgs()
        )

    # will check every possible flag that means the game needs to end
    def checkPlayStatus(self):
        if self.player_status is False or self.playing_now is False:
            return False
        else:
            return True

    # MAIN LOOP
    def play(self):
        # create method that will print the intro

        while self.checkPlayStatus():
            self.outHandler.appendToBuffer("\n")
            self.executeCommand()
            self.outHandler.appendToBuffer("\n" + "-=-" * 15)
            self.outHandler.displayOutput()

        # create method(s) that will print the end, depending on good or bad

    def executeCommand(self):
        # MOVE THESE 2 DICTS UPWARD AS GLOBAL CONSTANTS LATER

        # to use method,type COMMANDS_NO_ARGS[key]( parameter )
        COMMANDS_NO_ARGS = {
            "EXIT": self.exit,  # done
            "INVENTORY": self.listInventory,  # done
            "SAVE": self.gameState.save,
            "HELP": self.listCommands,  # done
            "LOCATION": self.location,  # done
            "SCAN": self.scan,  # done
            # "HINT" : self.hint
        }
        # ALL METHODS HERE NEED TO HANDLE WHEN USER DONT GIVE ADDITIONAL ENOUGH EX) MOVE + ""
        COMMANDS_WITH_ARGS = {
            "SAY": self.say,  # done
            "MOVE": self.move,  # done
            "ATTACK": self.attack,
            "USE": self.use,
            "GIVE": self.give,
            "TAKE": self.take,  # done
            "DISCARD": self.discard,  # done
        }
        # some of these will call the method from the appropriate object (container, room, etc)
        # but then get additional paramters when sent to outputHandler

        # get the input from user/player
        self.inHandler.parseInput()
        verb = self.inHandler.getVerb()
        keyword1 = self.inHandler.getFirstKeyword()
        keyword2 = self.inHandler.getSecondKeyword()  # attack GRUNT with BLASTER

        # print(" >>>> : ", verb, keyword1)

        # check dictionary of commands, seperated on whether it has parameters or not
        if verb.upper() in COMMANDS_NO_ARGS:
            COMMANDS_NO_ARGS[verb.upper()]()

        elif verb.upper() in COMMANDS_WITH_ARGS:
            if keyword2 == "":  # aka only 1 parameter
                COMMANDS_WITH_ARGS[verb.upper()](keyword1)
            else:  # unlikely to occure since game atm is very simple
                COMMANDS_WITH_ARGS[verb.upper()](keyword1, keyword2)

        else:
            self.outHandler.appendToBuffer("Invalid input, please try again.")

        self.outHandler.displayOutput()

    def move(self, direction="x"):
        direction = direction.upper()  # to match keys

        # print(self.current_room.name, direction)

        # add the actually north, south, etc if time permits

        # get rid of invalid input
        if direction.upper() not in ["N", "E", "W", "S"]:
            self.outHandler.appendToBuffer("That's not a valid direction.")
            return

        # get the door + room to move to
        door = self.current_room.getAssociatedDoor(direction)
        new_room = self.current_room.getConnectedRooms().get(direction)

        if door is not None:  # there is a room that direction but door locked
            if door.getCurrentState() == "solved":
                self.moveSuccess(new_room)
            elif door.getCurrentState() == "unsolved":
                self.moveFailure("there, " + door.getName() + " is locked")
        elif new_room is not None:  # room that direction, unblocked
            self.moveSuccess(new_room)
        else:
            self.moveFailure("a room that doesn't exist")

    # === the following 2 methods are helper methods for move() ===
    def moveFailure(self, targeted_room_name):
        # if you cannot move to that room # "failure": "You can't move to <>"
        self.outHandler.formatOutput("MOVE", "failure", [targeted_room_name])

    def moveSuccess(self, new_room):
        self.current_room = new_room
        # you saythe success move msg + describe new room # "success": "You moved to <>",
        self.outHandler.formatOutput("MOVE", "success", [self.current_room.getName()])
        self.outHandler.appendToBuffer("\n" + self.current_room.describeRoom())

        new_room.hasEntered()

    # HELPER for commands/verbs as some are very simple and use same structure
    # so far used in scan(), listInventory(), location(), listCommands()
    def basicOutputCall(self, toBeInserted, verb):
        if toBeInserted is None:
            self.outHandler.formatOutput(verb, "failure", [])
        else:
            self.outHandler.formatOutput(verb, "success", [toBeInserted])

    def scan(self):
        objects = self.current_room.scan()  # aka the room's inventory
        self.basicOutputCall(objects, "SCAN")

    def listInventory(self):
        invString = self.player.listInventory()
        self.basicOutputCall(invString, "INVENTORY")

    def location(self):
        self.basicOutputCall(self.current_room.getName(), "LOCATION")

    def listCommands(self):
        self.outHandler.formatOutput("HELP", "success", [self.commands])

    def say(self, speech):
        if speech != "":
            self.outHandler.formatOutput("SAY", "success", [speech])
        else:
            self.outHandler.formatOutput("SAY", "failure", [])

    def attack(self):
        pass

    # helper for use()
    # will look for a door puzzle and see if the item is its key, but already opened doors fail
    def tryOpeningDoors(self, item_obj):
        if self.current_room.tryOpeningDoors(item_obj):
            self.outHandler.formatOutput("USE", "success", [item_obj.getName()])
            self.outHandler.appendToBuffer("\nYou unlocked a door.\n")
            return True
        else:
            self.outHandler.formatOutput("USE", "failure", [item_obj.getName()])
            return False

    # helper for use()
    # will look in room for a puzzle and try to solve it
    def tryPuzzle(self, keyItem):
        if self.current_room.tryPuzzle(keyItem):
            self.outHandler.formatOutput("USE", "success", [keyItem.getName()])
        else:
            self.outHandler.formatOutput("USE", "failure", [keyItem.getName()])

    # use can be used on door keys, puzzle keyItems
    # NOT CODED IN: teleporter, revive, other special items -> will need to be sibclassed
    def use(self, item_name):
        used = False
        # retrieve the item, but None if not in inv
        item_obj = self.player.getObject(item_name)

        if item_obj is None:
            item_name += " because you don't have it."
            self.outHandler.formatOutput("USE", "failure", [item_name])
        # means the item can only be a puzzle's key
        elif item_obj.use():
            # RIGHT NOW THIS ORDER IS WACK
            # MIGHT NEED TO IMPLEMENT USE WITHIN CLASSES SOMEHOW
            # OR
            # MAKE USE REQUIRE 2 KEYWORDS
            if not self.tryOpeningDoors(item_obj):  # check the doors
                self.tryPuzzle(item_obj)  # check the room for a standalone puzzle

    # due to our current naming in JSON and thus how inputHandler gets the keywords
    # the item_name is case sensitive
    def take(self, item_name):
        # get the item, remove from room if there BUT returns None if not
        item_obj = self.current_room.getObject(item_name)

        if item_name == "" or item_obj is None:
            if item_name == "":
                item_name = "nothing"
            self.outHandler.formatOutput("TAKE", "failure", [item_name])
        else:
            # print item description
            self.outHandler.appendToBuffer(
                item_obj.getStateDescription(item_obj.current_state) + "\n"
            )
            # remove item and add item to player inv
            self.current_room.removeObject(item_obj)
            self.player.addToInv(item_obj)

            # print take msg
            self.outHandler.formatOutput("TAKE", "success", [item_name])

    # like take, item_name is case Sensitive
    def discard(self, item_name):
        # check the player has the item, will also remove from inv if it is there
        item_obj = self.player.getObject(item_name)

        if item_name == "":
            item_name = "nothing"
            self.outHandler.formatOutput("DISCARD", "failure", [item_name])
        elif item_obj is None:
            item_name += " since you don't have it"
            self.outHandler.formatOutput("DISCARD", "failure", [item_name])
        else:  # player has the object
            # remove from player + put item into room inventory
            self.player.removeObject(item_obj)
            self.current_room.addToInv(item_obj)
            self.outHandler.formatOutput("DISCARD", "success", [item_name])

    def save(self):
        pass

    def give(self):
        pass

    def exit(self):
        self.player_status = False
        self.outHandler.formatOutput("EXIT", "success", [])

    # from old demo code.... may not need
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
test.play()

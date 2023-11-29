import view, gameState


class GameEngine:
    def __init__(self) -> None:
        self.player_status = True
        self.turn_counter = 0
        self.data_needed = [None]
        self.data_TBChanged: [None]

        self.gameState = gameState.GameState()

        self.filled_rooms = self.gameState.populateWorld()

        self.inHandler = view.InputHandler(self.gameState.command_dict)
        self.outHandler = view.OutputHandler(
            self.gameState.command_dict, self.gameState.msg_dict
        )

    def executeCommand(self):
        # maybe change the obj calling the method depending where we actually store the damn methods
        # to use method,type COMMANDS[key]( parameter )
        COMMANDS = {
            """
            "N": self.N,
            "S": self.S,
            "E": self.E,
            "W": self.W,
            """
            "SAY" : self.say,
            "MOVE" : self.move,
            "ATTACK": self.attack,
            "SCAN": self.current_room.scan,
            "INVENTORY": self.player.listInventory,
            "USE": self.player.use,
            "TAKE": self.player.take,  # (item_to_take)
            "TALK": self.talk,
            "LOCATION": self.location,
            "DISCARD": self.player.discard,
            "SAVE": self.gameState.save,
            "HELP": self.listCommands,
        }

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

        self.inHandler.parseInput()
        verb = self.inHandler.getVerb()
        keyword1 = self.inHandler.getFirstKeyword()
        keyword2 = self.inHandler.getSecondKeyword()

        objectList = []

        # check dictionary of commands to see which correct action to take
        if verb.upper() in COMMANDS:
            # need to handle parameters somehow but do that later....
            COMMANDS[verb.upper()]()
        else:
            self.outHandler.formatOutput(verb, "failure", objectList)

    # transfering xixek's methods - reminder that method names are camelcase but variables are underscored
    def say(self):
        pass
    
    def move(self, current_room, direction="x"):
        # get rid of invalid input
        if direction.upper() not in ["N", "E", "W", "S"]:
            return current_room

        # get the door
        door = current_room.getAssociatedDoor().get(direction)

        if door is None:
            pass
        else:
            door_state = door.state

            if door_state == "solved":
                return current_room.getConnectedRooms().get(direction)
            elif door_state == "unsolved":
                pass  # need to tell view to send failure door msg

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

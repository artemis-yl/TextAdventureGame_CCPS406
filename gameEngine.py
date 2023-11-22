import view, gameLoader


class GameEngine:
    # maybe change the obj calling the method depending where we actually store the damn methods
    # to use method,type COMMANDS[key]( parameter )
    COMMANDS = {
        "N": current_room.N,
        "S": current_room.S,
        "E": current_room.E,
        "W": current_room.W,
        "ATTACK": target_NPC.attack,
        "SCAN": current_room.scan,
        "INVENTORY": player_NPC.listInventory,
        "USE": player_NPC.use,
        "TAKE": player_NPC.take,
        "TALK": target_NPC.talk,
        "LOCATION": blank.location,
        "DISCARD": blank.discard,
    }

    # notes on where these methods should be....

    # N,S,E,W needs to move the player from the current room inventory to the desired room's inventory
    #  will call on currentRoom to check if a room exist and the puzzle/door
    #  => needs to stored HERE in gameEngine
    # ATTACK needs the attacking NPC and target NPC => here in GameEngine
    # LOCATION tells you current room => her ein GameEngine

    # SCAN lists out everything inside the current room's inventory => should be in room.py

    # INVENTORY lists out player inventory => in NPC.py
    # TALk only work on NPC => NPC.py
    # DISCARD is for player to remove an item => in NPC.py

    # TAKE can only work on items => item.py

    def __init__(self) -> None:
        self.player_status = True
        self.turn_counter = 0
        self.data_needed = [None]
        self.data_TBChanged: [None]

        self.model = gameLoader(
            "npc.json",
            "room.json",
            "items.json",
            "puzzles.json",
            "gameMsg.json",
            "commands.json",
        )
        (
            self.npc_dict,
            self.room_dict,
            self.item_dict,
            self.puzzle_dict,
            self.msg_dict,
            self.command_dict,
        ) = self.model.loadGame()

        self.inHandler = view.InputHandler(self.command_dict)
        self.outHandler = view.OutputHandler(self.command_dict, self.msg_dict)

    def executeCommand(self):
        self.inHandler.parseInput()
        verb = self.inHandler.getVerb()
        keyword1 = self.inHandler.getFirstKeyword()
        keyword2 = self.inHandler.getSecondKeyword()

        # check dictionary of commands to see which correct action to take
        if verb.upper() in self.COMMANDS:
            self.COMMANDS[verb.upper()]()
        else:
            self.outHandler.formatOutput(verb, "failure", objectList)

    def checkConditions(self):
        pass

    def handleCombat(self):
        pass

    def handleDetection(self):
        pass

    def handlePuzzle(self):
        pass

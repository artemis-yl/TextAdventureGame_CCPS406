import view, gameLoader


class GameEngine:
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

        self.player = self.npc_dict["npc_player"]

        self.inHandler = view.InputHandler(self.command_dict)
        self.outHandler = view.OutputHandler(self.command_dict, self.msg_dict)

    def executeCommand(self):
        # maybe change the obj calling the method depending where we actually store the damn methods
        # to use method,type COMMANDS[key]( parameter )
        COMMANDS = {
            "N" : self.N,
            "S" : self.S,
            "E" : self.E,
            "W" : self.W,
            "ATTACK" : self.attack,
            "SCAN" : self.current_room.scan,
            "INVENTORY" : self.player.listInventory,
            "USE" : self.player.use,
            "TAKE" : self.player.take,  # (item_to_take)
            "TALK" : self.talk,
            "LOCATION" : self.location,
            "DISCARD" : self.player.discard,
        }

        # notes on where these methods should be....

        # N,S,E,W needs to move the player from the current room inventory to the desired room's inventory
        #  will call on currentRoom to check if a room exist and the puzzle/door
        #  => needs to stored HERE in gameEngine
        # ATTACK needs the attacking NPC and target NPC => here in GameEngine
        # LOCATION tells you current room => her ein GameEngine
        # TALK only work on NPC, but the NPC needs to be in the same room as player => here in gameEngine
        # USE requires that the player has the item, and that the target is in the room => here in game engine

        # SCAN lists out everything inside the current room's inventory => should be in room.py

        # INVENTORY lists out player inventory => in NPC.py
        # DISCARD is for player to remove an item => in NPC.py
        # TAKE can only work on items, but need to place into NPC inv => NPC.py

        self.inHandler.parseInput()
        verb = self.inHandler.getVerb()
        keyword1 = self.inHandler.getFirstKeyword()
        keyword2 = self.inHandler.getSecondKeyword()

        objectList = []

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

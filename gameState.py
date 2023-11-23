class GameState:
    def __init__(self):
        # Initialize the attributes
        self.currentRoom = None
        self.rooms = []
        self.npcs = []
        self.puzzles = []
        self.items = []
        self.player = None

    def signalChange(self):
        # Method to signal a change in the game state
        print("Game state changed!")

    # Example Usage:
    # Instantiate GameState and use its attributes and methods
    # game_state = GameState()
    # game_state.currentRoom = Room("Start Room", "A room where the adventure begins", [], "Open", None, [])
    # game_state.rooms = [Room("Room 1", "Description 1", [], "Open", None, []),    
    #                     Room("Room 2", "Description 2", [], "Open", None, [])]
    # game_state.npcs = [NPC("John Doe", "Friendly", "Alive", ["Key"], ["solve_puzzle"]),
    #                    NPC("Jane Doe", "Mysterious", "Alive", ["Map"], ["unlock_door"])]
    # game_state.puzzles = [Puzzle("solve_puzzle", "Solve the puzzle to unlock the door", "Locked", "Key", "use")]
    # game_state.items = [Item("Key", "A shiny key", "Inactive")]
    # game_state.player = Player("Player 1", 100, [])

    # Call the signalChange method to indicate a change in the game state
    # game_state.signalChange()
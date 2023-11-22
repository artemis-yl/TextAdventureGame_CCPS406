from container import ContainterModel

class Puzzle(ContainterModel):
    def __init__(self, id, name, stateDescriptions, currentState, key, keyVerb, subPuzzles):
        super().__init__(self, id, name, stateDescriptions, subPuzzles)

        self.currentState = currentState
        self.key = key
        self.keyVerb = keyVerb

    def solve(self):
        self.currentState = "solved"

    """ 
    #these are in superclass
    def getName(self):
        return self.name

    def getStateDescriptions(self):
        return self.stateDescriptions

    def getSubPuzzles(self):
        return self.subPuzzles
    """

    def getCurrentState(self):
        return self.currentState

    def setCurrentState(self, currentState):
        self.currentState = currentState

    def getKey(self):
        return self.key

    def getKeyVerb(self):
        return self.keyVerb


"""        
# Example usage in a text-based game
if __name__ == "__main__":
    # Initialize the game state
    current_room = "Starting Room"

    # Main game loop
    while True:
        print(f"You are in the {current_room}.")

        # Check if there is a puzzle associated with the current room
        if current_room in puzzles_data:
            puzzle = puzzle_instances[current_room]
            print(f"Puzzle Name: {puzzles_data[current_room]['name']}")
            print(f"Puzzle Description: {puzzles_data[current_room]['stateDescriptions'][puzzle.getState().lower()]}")
            print(f"Key Item: {puzzle.getKeyItem()}")

            user_action = input("What do you want to do? ").strip().upper()

            # Logic to interact with the puzzle
            if user_action == puzzle.getKeyVerb():
                if not puzzle.getState():
                    # Handle solving the puzzle
                    user_answer = input(f"What is the answer to the {puzzles_data[current_room]['subPuzzles'][0]['name']}? ").strip().lower()
                    if user_answer == puzzles_data[current_room]['subPuzzles'][0]['answer']:
                        puzzle.setState(True)
                        print("You've solved the puzzle!")
                    else:
                        print("That's not the correct answer.")
                else:
                    print("The puzzle is already solved.")
            elif user_action == "LOOK AT":
                # Describe the room or puzzle
                print(puzzles_data[current_room]['stateDescriptions'][puzzle.getState().lower()])
            elif user_action == "MOVE":
                destination = input("Where do you want to go? ").strip()
                if destination in rooms_data.get(current_room, []):
                    current_room = destination
                else:
                    print("You can't go there from here.")
            elif user_action == "QUIT":
                print("Thanks for playing!")
                break
            else:
                print("You can't do that here.")

        # Game progression logic (e.g., moving to other rooms) goes here
        else:
            print("There's nothing to do here.")
"""

"""   
    # Access and manipulate the puzzle instances
    puzzle1 = puzzle_instances["compoundPuzzle1"]
    puzzle2 = puzzle_instances["compoundPuzzle2"]
    puzzle3 = puzzle_instances["compoundPuzzle3"]
    puzzle4 = puzzle_instances["compoundPuzzle4"]

    print("Puzzle 1 Name:", puzzles_data["compoundPuzzle1"]["name"])
    print("Puzzle 1 Key Item:", puzzle1.getKeyItem())
    print("Puzzle 1 Key Verb:", puzzle1.getKeyVerb())
    print("Puzzle 1 Solved State:", puzzle1.getState())

    print("\nPuzzle 2 Name:", puzzles_data["compoundPuzzle2"]["name"])
        # Access and print attributes for puzzle 2, 3, and 4 similarly.
    print("\nPuzzle 2 Name:", puzzles_data["compoundPuzzle2"]["name"])
    print("Puzzle 2 Key Item:", puzzle2.getKeyItem())
    print("Puzzle 2 Key Verb:", puzzle2.getKeyVerb())
    print("Puzzle 2 Solved State:", puzzle2.getState())

    print("\nPuzzle 3 Name:", puzzles_data["compoundPuzzle3"]["name"])
    print("Puzzle 3 Key Item:", puzzle3.getKeyItem())
    print("Puzzle 3 Key Verb:", puzzle3.getKeyVerb())
    print("Puzzle 3 Solved State:", puzzle3.getState())

    print("\nPuzzle 4 Name:", puzzles_data["compoundPuzzle4"]["name"])
    print("Puzzle 4 Key Item:", puzzle4.getKeyItem())
    print("Puzzle 4 Key Verb:", puzzle4.getKeyVerb())
    print("Puzzle 4 Solved State:", puzzle4.getState())
"""

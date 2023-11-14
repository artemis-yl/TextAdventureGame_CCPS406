class InputHandler:
    def __init__(self) -> None:
        # format is Verb Target with Item - ex) attack grunt with blaster
        self.reset()
        # default prompt
        self.prompt = "What will you do? >"

    # this methods will extract the key words from the given user Input
    def parseInput(self):
        self.reset()  # ensures prev parsed input does not linger

        rawInput = input(self.prompt).lower().split(" ")

        self.verb = rawInput[0]
        self.target = rawInput[1]
        if len(rawInput) > 2:
            self.item = rawInput[-1]

    def getVerb(self):
        return self.verb

    def getTarget(self):
        return self.target

    def getItem(self):
        return self.item

    # can change the prompt per situation
    def setPrompt(self, givenPrompt):
        self.prompt = givenPrompt

    def reset(self):
        self.verb, self.target, self.item = ""


class OutputHandler:
    def __init__(self) -> None:
        self.buffer = ""

    def displayOutput(self):
        print(self.buffer)
        self.clearBuffer()

    # even is there is only 1 object to print, must be in a list for paras
    def formatOutput(self, msg, paras):
        if len(paras) > 1:
            # will give index of spot to insert paras
            position = msg.find("{}")
            front = msg[:position]
            back = msg[position:]

            formattedParas = ""
            for i in range(0, len(paras) - 2):
                formattedParas += ", " + paras[i]
            formattedParas += ", and " + paras[-1]

            msg = front + formattedParas + back  # may need to add a space???

        # 1 or more parameters, 1st will always be at default
        else:
            msg.format(paras[0])

        self.appendToBuffer(msg)

    def appendToBuffer(self, formatted):
        self.buffer += formatted

    def clearBuffer(self):
        self.buffer = ""

    # entering a room, you get described:
    # room, all items in room, all NPCs in room

    # room description prints: You enter... you see...
    # ally msgs print i.e. With you are your allies/ally <> ... . They seem <>
    # items print i.e. You see <>, <>, <> ... and <> in the room.
    # enemy print i.e. You can see grunt(s) over there. They haven't noticed you yet

    # use loops to print all objects in a list.
    # use if to determine plural/singular forms of certain wrods

    # if user did an action, you will see in response:
    # success or failure msg corrosponding to the Verb + item(s)
    # each action has a success/failure msg attached, only need to attack target + item

    # if the enemy is present and takes action, it will be printed
    # ex) grunt attacked you will a blaster! fortunately you know the force and
    # have a beamsword so you blocked it. You're not sure if you can do it again

    # Game over messages, or other game-mechanic msgs, like warning of the overal timer


# this class is kinda... not useful
# might be better to only have the handlers OR have it all in this View class
class View:
    # initialize handlers
    def __init__(self) -> None:
        self.inHandler = InputHandler()
        self.outHandler = OutputHandler()

        # default prompt
        self.prompt = "What will you do? >"

    # can change the prompt per situation
    def setPrompt(self, givenPrompt):
        self.prompt = givenPrompt

    # retrives the input from the user after printing the Prompt
    # caller will receive a list of strings containing the [verb, target, item]
    def getInput(self):
        ih = self.inHandler
        ih.parseInput(self.prompt)
        return [ih.getVerb(), ih.getTarget(), ih.getItem()]

    def display(self, string):
        # prints the output to the user
        print(string)

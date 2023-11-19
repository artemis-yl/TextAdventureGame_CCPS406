import re


class InputHandler:
    def __init__(
        self, prompt="What will you do? >", invalidResponse="Invalid input."
    ) -> None:
        """
        Verb Target Item ex) attack grunt with blaster
        Verb Item Target ex) use ITEM on SOMETHING
        => caller needs to know how to parse which is target and which is item based on Verb
        """

        # code repeat with reset() but better readibility
        self.verb = ""
        self.keyword2 = ""
        self.keyword1 = ""
        self.prompt = prompt
        self.invalidResponse = invalidResponse

    # this method will extract the verb/command, and keywords from the user Input
    def parseInput(self):
        self.reset()  # ensures prev parsed input does not linger

        # imitation do-while loop to ensure valid input from user
        while True:
            # recall that: - strip() trims whitespace at front and end of string
            #            : - split() list-ifys a string based on a given seperator
            rawInput = input(self.prompt).strip().lower().split(" ")

            # basic error check : may create a new function for this later
            if rawInput[0] == "" or len(rawInput) > 4:
                print(self.invalidResponse)
            else:
                break

        # min valid input is a verb. target and item are not always there
        self.verb = rawInput[0]
        if len(rawInput) > 1:
            self.keyword1 = rawInput[1]
        if len(rawInput) > 2:
            self.keyword2 = rawInput[-1]

    def getVerb(self):
        return self.verb

    def getFirstKeyword(self):
        return self.keyword1

    def getSecondKeyword(self):
        return self.keyword2

    # can change the prompt per situation
    def setPrompt(self, givenPrompt):
        self.prompt = givenPrompt

    def reset(self):
        self.verb = ""
        self.keyword2 = ""
        self.keyword1 = ""


class OutputHandler:
    def __init__(self) -> None:
        self.buffer = ""

    def displayOutput(self):
        print(self.buffer)
        self.clearBuffer()

    # method assumes list is a homogeneous list of Strings
    def listToGrammarString(self, list):
        if len(list) > 1:
            formatted = ", ".join(list[:-1]) + ", and " + list[-1]
        else:
            formatted = list[0]

        return formatted

    """
    two types of msgs that needs to be formatted: 
        1) "You blah <> with/on <>" 
        2) "blah blah <> blah"

    1st will only have 1 THING per <>
        => can use normal python formatter and nothing else

    2nd can have many objects per <>
    """

    # even is there is only 1 object to print, must be in a list for para(meter)s
    def formatOutput(self, msg, paras):
        splited = re.split("<>", msg)  # string to list, split at seperator "<>"

        # this is very... hardcoded. good for now but may need to be redone
        if len(splited) == 2:  # AKA only 1 "<>" AKA 1 split AKA 2 substrings
            msg = splited[0] + self.listToGrammarString(paras) + splited[1]
        else:
            msg = splited[0] + paras[0] + splited[1] + paras[1] + splited[2]

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


""" testing InputHandler
inH = InputHandler()

inH.parseInput()
print("verb: " + inH.getVerb())
print("1st: " + inH.getFirstKeyword())
print("2nd: " + inH.getSecondKeyword())
"""

"""testing output Handler


inO = OutputHandler()
inO.formatOutput("You attacked <>", ["grunt"])
inO.displayOutput()

inO.formatOutput("You attacked <> with <>!", ["grunt", "sword"])
inO.displayOutput()
"""

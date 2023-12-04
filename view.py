import re

# output msg keys
SUCCESS = "success"
FAILED = "failure"


# purpose of this class is to:
# 1) prompt the player to enter their next move
# 2) parse the VERB and any keywords
# 3) Basic invalid inputs are also handled
class InputHandler:
    def __init__(self, cmd_list, invalidResponse, prompt) -> None:
        """
        Verb Target Item ex) attack grunt with blaster
        Verb Item Target ex) use ITEM on SOMETHING
        => caller needs to know how to parse which is target and which is item based on Verb
        """

        # code repeat with reset() but better readibility
        self.verb = ""
        self.keyword1 = ""
        self.keyword2 = ""
        self.notVerbText = ""
        self.cmd_list = cmd_list

        self.prompt = prompt
        self.invalidResponse = invalidResponse

    # checks if the raw input is valid
    #  i.e.) not blank, didn't type more than 4 words,
    def checkRawInput(self, rawInput):
        if rawInput[0] == "" or len(rawInput) > 4:
            return False
        return True

    # check if the verb extracted is valid
    def checkVerb(self):
        if self.verb.upper() in self.cmd_list:
            return True
        else:
            self.reset()
            return False

    # returns False if the rawInput was invalid
    def extractInput(self):
        # prompt user and get raw string
        rawInput = input(self.prompt)
        splited = rawInput.strip().split(" ")

        # extract verb + keywords if raw input is ok
        rawCheck = self.checkRawInput(splited)
        if rawCheck:
            self.notVerbText = splited
            # min valid input is a verb. target and item are not always there
            self.verb = splited[0].lower()
            if len(splited) > 1:
                self.keyword1 = splited[1]
            if len(splited) > 2:
                self.keyword2 = splited[-1]
            return True
        else:
            print(self.invalidResponse)
            return False

    # this method will extract the verb/command, and keywords from the user Input
    def parseInput(self):
        self.reset()  # ensures prev parsed input does not linger

        # imitation do-while loop to ensure valid input from user
        # if the rawInput is invalid OR the verb not on list, keep looping
        # else, break out of while loop
        while True:
            if self.extractInput() is False:
                continue
            if self.checkVerb() is True:
                break

    def getVerb(self):
        return self.verb

    def getNotVerb(self):
        return self.notVerbText

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
        self.notVerbText = ""


# the purpose of this class is to handle printing everything to the user/player
# 1) it primarily formats the success and failure responses to each VERB
# 2) it also allows one to add anyother string to the buffer before displaying
# in case the method caller has other text
class OutputHandler:
    def __init__(self, command_msgs, game_msgs) -> None:
        self.buffer = ""
        self.command_msgs = command_msgs  # this and below are dictionarys
        self.game_msgs = game_msgs

    # the following 3 methods are as they say.
    def appendToBuffer(self, string):
        self.buffer += string

    def clearBuffer(self):
        self.buffer = ""

    def displayOutput(self):
        print(self.buffer)
        self.clearBuffer()

    def printGameMessage(self, key):
        self.appendToBuffer(self.game_msgs[key])
        # self.displayOutput()

    def getCMDOutput(self, key, result):
        # result keys can be "sucess" or "failure"
        return self.command_msgs[key][result]

    """
    two types of msgs that needs to be formatted: 
        1) "You blah <> with/on <>" 
        2) "blah blah <> blah"

    1st will only have 1 THING per <>
        => can use normal python formatter and nothing else

    2nd can have many objects per <>
    """

    # these 2 methods exist purely for ease of calling
    def successMsg(self, verb, given):
        self.formatVerbMsg(verb, SUCCESS, given)

    def failMsg(self, verb, given):
        self.formatVerbMsg(verb, FAILED, given)

    # even is there is only 1 object to print, must be in a list for para(meter)s
    def formatVerbMsg(self, verb, result, given):
        msg = self.getCMDOutput(verb, result)  # get success or failure ver of msg
        splited = re.split("<>", msg)  # string to list, split at seperator "<>"
        # print(">>> ", given)

        # this is very... hardcoded. good for now but may need to be redone
        if len(splited) == 2:  # AKA only 1 "<>" AKA 1 split AKA 2 substrings
            msg = splited[0] + given[0] + splited[1]
        elif len(splited) > 2:
            msg = splited[0] + given[0] + splited[1] + given[1] + splited[2]

        self.appendToBuffer(msg)

    # method assumes parameter list is a homogeneous list of Strings
    def listToGrammarString(list):
        if len(list) > 1:
            formatted = ", ".join(list[:-1]) + ", and " + list[-1]
        else:
            formatted = list[0]

        return formatted

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

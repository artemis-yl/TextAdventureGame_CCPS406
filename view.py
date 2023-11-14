class View:

  private prompt = ''
  private input = ''
  
  def getInput(self):
    #retrives the input from the user
    self.input = input(prompt)

  def display(self, string):
    #prints the output to the user
    print(string)

  def setPrompt(self, givenPrompt):
    self.prompt = givenPrompt

class inputHandler:
  # format is Verb Target with Item
  # ex) attack grunt with blaster
  verb, target, item = ''
  
  def parseInput(self):
    
    input = input.lower().split(' ')
    
    self.verb = input[0]
    self.target = input[1]
    if len(input) > 2: 
      self.item = input[-1]

class outputHandler:
  """appendToBuffer(message: string): void

+ clearBuffer(): void             

+ displayOutput(): void

+ formatOutput()"""
  # entering a room, you get described:
  # room, all items in room, all NPCs in room
  def printEnteringRoom(self, roomMsg, itemMsgs[], enemyMsgs[], allyMsgs):
    # room description prints: You enter... you see...
    # ally msgs print i.e. With you are your allies/ally <> ... . They seem <>
    # items print i.e. You see <>, <>, <> ... and <> in the room. 
    # enemy print i.e. You can see grunt(s) over there. They haven't noticed you yet

    # use loops to print all objects in a list.
    # use if to determine plural/singular forms of certain wrods
    
    pass

  # if user did an action, you will see in response:
  # success or failure msg corrosponding to the Verb + item(s)
  # each action has a success/failure msg attached, only need to attack target + item
  def printActionResult(self, strings[]):
    # Success/Failure! You <verb>ed the <target> with <item>
    pass


  # if the enemy is present and takes action, it will be printed
  # ex) grunt attacked you will a blaster! fortunately you know the force and 
  # have a beamsword so you blocked it. You're not sure if you can do it again
  def printExternalAction(self):
    pass

  # Game over messages, or other game-mechanic msgs, like warning of the overal timer

  def printWorldMessage(self, strings[]):
    pass
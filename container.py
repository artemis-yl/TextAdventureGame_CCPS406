class ContainterModel:
    def __init__(self, name, states, inventory) -> None:
        # self.id = id #string
        self.name = name  # string
        # this is a list of strings, if only one it will be a list of 1 element
        # the subclasses will describe which index holds what kind of description
        self.state_descriptions = states  # dictionary
        self.inventory = inventory  # list

    # pythonically, no true data encapsulation, therefore no real need for setter/getters
    # shall include anyway, for now

    # both, name and ID will never change so no need to have setters
    def getName(self):
        return self.name

    def getID(self):
        return self.id

    # will give you the object + remove it from inv
    def getObject(self, obj_name):
        if obj_name in self.inventory:
            return self.inventory[obj_name]
        return None

    # unlike above, need the actual object ref and not a string of its name
    def removeObject(self, object):
        if object in self.inventory:
            self.inventory.pop(object)
            return True
        return False

    def addToInv(self, obj):
        self.inventory[obj.getName()] = obj

    def getInv(self):
        return self.inventory

    def setInv(self, invList):
        self.inventory = invList


    def getStateDescription(self, state_key):
        return self.state_descriptions[state_key]

    # utility method that's really useful
    def listToGrammarString(self, list):
        if len(list) > 1:
            formatted = ", ".join(list[:-1]) + ", and " + list[-1]
        elif len(list):
            formatted = list[0]
        else:
            formatted = "empty"

        return formatted

    # useful for all  command method
    def listInventory(self):
        str_list = []
        for item in self.inventory:
            str_list.append(item.name)

        if str_list == []:
            return None
        return self.listToGrammarString(str_list)

        """
            #above is the more... pythonic way, below is more OOP ala java
            self.__name = name
            self.__descritpion = description
            self.__inventory = inventory

        def getName(self):
            return self.__name

        #now that I think about it... we don't really need to ever change the name right?
        # so no need for a .setName() method

        def getDescription(self):
            return self.__descritpion

        def getInv(self):
            return self.__inventory

        def addToInv(self, obj):
            self.__inventory.append(obj)

        def removeFromInv(self, obj):
            if obj in self.__inventory:
                self.__inventory.remove(obj)
        """

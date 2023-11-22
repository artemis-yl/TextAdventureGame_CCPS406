class ContainterModel:
    def __init__(self, id, name, description, inventory) -> None:
        self.id = id
        self.name = name
        # this is a list of strings, if only one it will be a list of 1 element
        # the subclasses will describe which index holds what kind of description
        self.description = description
        self.inventory = inventory

    # pythonically, no true data encapsulation, therefore no real need for setter/getters
    # shall include anyway, for now

    # both, name and ID will never change so no need to have setters
    def getName(self):
        return self.name

    def getID(self):
        return self.id

    def getInv(self):
        return self.inventory

    def setInv(self, invList):
        self.inventory = invList

    def getDescription(self):
        return self.description

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

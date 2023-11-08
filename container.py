class ContainterModel:
    def __init__(self, name, description, inventory) -> None:
        """
        self.name = name
        self.descritpion = description
        self.inventory = inventory
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
    
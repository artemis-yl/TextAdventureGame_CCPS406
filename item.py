class Item:
    def __init__(self, name, description, inventory):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.state = "Normal"

    def getName(self):
        return self.name

    def setName(self, new_name):
        self.name = new_name

    def getDescription(self):
        return self.description

    def isWeapon(self):
        return False            # Override if the item is a weapon

    def isShield(self):
        return False            # Override if the item is a shield

    def isRevive(self):
        return False            # Override if the item is for revival

    def isTeleport(self):
        return False            # Override if the item is for teleportation

    def isHealthPotion(self):
        return False            # Override if the item is a health potion



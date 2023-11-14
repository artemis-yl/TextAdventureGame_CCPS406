class Item:
    def __init__(self, name, state_descriptions, state, is_purpose=[False, False, False, False]):
        self.name = name
        self.state_descriptions=state_descriptions
        self.state=state

        #[Weapon, Shield, Teleporter, Revive]
        self.is_purpose=is_purpose

    def getName(self):
        return self.name

    def setName(self, new_name):
        self.name = new_name

    def getDescription(self):
        return self.description

    def isWeapon(self):
        return self.is_purpose[0]           # Override if the item is a weapon

    def isShield(self):
        return self.is_purpose[1]            # Override if the item is a shield

    def isRevive(self):
        return self.is_purpose[2]             # Override if the item is for revival

    def isTeleport(self):
        return self.is_purpose[3]             # Override if the item is for teleportation


    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return f"{self.name}"   

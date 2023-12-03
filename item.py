from container import ContainterModel

class Item(ContainterModel):
    def __init__(self, item):
        super().__init__(
            item["name"],
            item["stateDescriptions"],
            [None]
        )

        self.current_state = item["currentState"]
        self.is_purpose = item["is_purpose"] #[Weapon, Shield, Teleporter, Revive]

    # needs to be overriden in a subclass for weapon, revive, teleporter, etc
    # will currently return True to indicate item is only a puzzle's key
    def use(self):
        return True

    def isWeapon(self):
        return self.is_purpose[0]  # Override if the item is a weapon

    def isShield(self):
        return self.is_purpose[1]  # Override if the item is a shield

    def isRevive(self):
        return self.is_purpose[2]  # Override if the item is for revival

    def isTeleport(self):
        return self.is_purpose[3]  # Override if the item is for teleportation

    def setState(self, new_state):
        self.current_state = new_state

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"
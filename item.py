from container import ContainterModel


class Item(ContainterModel):
    def __init__(self, puzzle):
        super().__init__(
            self,
            puzzle["name"],
            puzzle["stateDescriptions"],
            [None],
        )

        self.current_state = puzzle["currentState"]
        self.is_purpose = puzzle["is_purpose"] #[Weapon, Shield, Teleporter, Revive]

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


"""          
# Load item data from file
with open("items.json", 'r') as items_file:
    items_data = json.load(items_file)
    item_instances = []

    for item_info in items_data['items']:
        new_item = Item(
            item_info["name"],
            item_info["stateDescriptions"],
            item_info["currentState"],
            [
                item_info["isWeapon"],
                item_info["isShield"],
                item_info["isTeleporter"],
                item_info["isRevive"]
            ]
        )
        item_instances.append(new_item)

# Example usage...
# Access and manipulate the Item instances
for item in item_instances:
    print(f"Item Name: {item.getName()}")
    print(f"Description: {item.getDescription()}")
    print(f"Is Weapon: {item.isWeapon()}")
    print(f"Is Shield: {item.isShield()}")
    print(f"Is Teleport: {item.isTeleport()}")
    print(f"Is Revive: {item.isRevive()}")
    print("\n")
"""

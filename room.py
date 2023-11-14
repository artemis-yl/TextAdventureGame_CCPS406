class Room:
    def __init__(self, room_name,connected_to,associated_door,initial_inventory,character):
        self.room_name = room_name
        self.connected_to = connected_to
        self.associated_door = associated_door
        self.initial_inventory=initial_inventory
        self.characters_inside=[]
        self.state = None

    def getRoom(self):
        return self.room_id

    def getDoor(self):
        return self.connected_to

    def getState(self):
        return self.state

    def setState(self, new_state):
        self.state = new_state


    def __str__(self):
        return f"{self.room_name}"
    
    def __repr__(self):
        return f"{self.room_name}"

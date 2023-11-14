class Room:
    def __init__(self, room_id):
        self.room_id = room_id
        self.connected_rooms = {}
        self.connected_doors = {}
        self.state = None

    def getRoom(self):
        return self.room_id

    def getDoor(self):
        return self.connected_doors

    def getState(self):
        return self.state

    def setState(self, new_state):
        self.state = new_state

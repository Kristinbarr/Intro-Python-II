# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.cur_room = starting_room

    def move(self, direction):
        # player can move in a direction
        next_room = self.cur_room.get_room_in_direction(direction)
        # new room has to be defined
        if next_room is not None:
            self.cur_room = next_room
            print(self.cur_room)
        else:
            print('You cannot move in that direction')
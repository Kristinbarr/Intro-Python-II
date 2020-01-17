# Write a class to hold player information, e.g. what room they are in currently.
class Player:
    def __init__(self, name, start_room):
        self.name = name
        self.cur_room = start_room
        # self.item = item
        # self.holding = holding

    def travel(self, direction):
        # player should be able to travel in a direction
        # below creates a variable and calls a method on a room instance
        next_room = self.cur_room.get_next_room(direction)
        if next_room is not None:
            self.cur_room = next_room
            print(f"You are in the: {self.cur_room}")
        else:
            print("No room in that direction, try again!")

    # def travel(self, direction):
    #     next_room = self.cur_room.get_room_in_direction(direction)
    #     if next_room is not None:
    #         self.cur_room = next_room
    #     else:
    #         print("You cannot move in that direction.")

    # def grab(self):
    #     holding.append(self.item)
    # def drop(self):
    #     holding.remove(self.item)

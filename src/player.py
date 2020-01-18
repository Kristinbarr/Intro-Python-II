# Write a class to hold player information, e.g. what room they are in currently.
class Player:
    def __init__(self, name, start_room):
        self.name = name
        self.cur_room = start_room
        self.items = None

    def travel(self, direction):
        # player should be able to travel in a direction
        # below creates a variable and calls a method on a room instance
        next_room = self.cur_room.get_next_room(direction)
        if next_room is not None:
            self.cur_room = next_room
            print(f"\nYou are in the: {self.cur_room}\n")
            print(f"This room contains: {', '.join(self.cur_room.items)}\n")
            print(f'To grab an item, enter "grab: [item]"')
        else:
            print("No room in that direction, try again!")

    def grab_item(self, item):
        print("test!", str(item) in self.cur_room.items)
        if item in self.cur_room.items:
            self.cur_room.withdraw_item(item)
            self.items.append(item)
            print(f"You are now holding: {self.items}")
        else:
            print(f"This room doesn't have that item.")

    def drop_item(self, item):
        if item in self.items:
            self.items.remove(item)
            self.cur_room.deposit_item(item)
            if len(self.item) == 0:
                return f"You are not holding any items"
            else:
                return f"You are now holding: {','.join(self.items)}"
        else:
            return f"You are not holding that item."

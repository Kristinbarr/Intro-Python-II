import sys
from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
    
player1 = Player('Joe', room['outside'], 'n')
print()
print("======= Welcome to the Dungeon =======")
print()
# playerName = input('What is your name? ')
# print(f'welcome {playerName}')
# print(player1.printRoom())
cmd = input("Press [n][s][e][w] to move through rooms, [q] to quit.")

while True:
    print(player1.cur_room)
    cmd = input('--> ').lower()

    if cmd in ['n','s','e','w']:
        current_room = player1.cur_room
        next_room = getattr(current_room, f"{cmd}_to")

        if next_room is not None:
            # move player by setting new cur room
            player1.cur_room = player1.cur_room.n_to
        else:
            print("You cannot move in that direction.")

    elif cmd == 'q':
        print('Goodbye!')
        exit()
    else:
        print('Not a valid command, try again! [n][s][e][w] or [q]')
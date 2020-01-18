from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons", ["fig leaf", "key"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east.""", ["hat", "shoes"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air.""", ["pretzel shaped twig"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""", ["silver ring", "treasure chest", "sachel of gold coins"]),
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
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# welcome message
player = Player("Player1", room["outside"])
print(f"\nWelcome to the Mad House, {player.name}!")
print(f"\nYou are here: {player.cur_room}")
print("\nGo [n] North [s] South [e] East [w] West  or  [q] to Quit.")

# initialize cmd
directions = ["n", "s", "e", "w"]

# LOOP
while True:
    # READ
    # print(f'welcome {player.name}')
    cmd = input("~~> ").lower()

    # PRINT
    # current room name description
    if cmd in directions:
        player.travel(cmd)

    elif cmd.split(':')[0] == "grab":
        item = cmd.split(':')[1]
        player.grab_item(item)
    # if user quits game
    elif cmd == "q":
        print("\nGoodbye!\n")
        exit()
    else:
        # prompt user to make another selection
        print('\nCould not recognize that command. Try again!\n')
        # print("[n] North [s] South [e] East [w] West   [q] Quit")

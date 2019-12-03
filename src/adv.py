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
#

# Make a new player object that is currently in the 'outside' room.
Darren = Player('Darren', room['outside'])


# Write a loop that:
quit = False 

while not quit:
    current_room = Darren.current_room
    print(f"{current_room}")
    command = input('What direction are you going? N, S, E, W?:')
    command = command.lower()
    if command == 'q':
        quit = True

   # Room moves
    if current_room == room['outside'] and command != "n":
       print('No Room in that direction!')

    if current_room == room['foyer'] and command == "w":
       print('No Room in that direction!')
    
    if current_room == room['overlook'] and command == "s":
       print('No Room in that direction!')

    if current_room == room['narrow'] and command == "s" or "e":
       print('No Room in that direction!')

    if current_room == room['treasure'] and command != "s":
       print('No Room in that direction!')

   #Room moves
    if current_room == room['outside'] and command == "n":
        Darren.current_room = room['foyer']

    if current_room == room['foyer'] and command == "s":
        Darren.current_room = room['outside']   
    
    if current_room == room['foyer'] and command == "n":
        Darren.current_room = room['overlook']   
        # print(f"{current_room}")

    if current_room == room['foyer'] and command == "e":
        Darren.current_room = room['narrow']     
    
    if current_room == room['overlook'] and command == "s":
        Darren.current_room = room['foyer']

    if current_room == room['narrow'] and command == "w":
        Darren.current_room = room['foyer']
    
    if current_room == room['narrow'] and command == "n":
        Darren.current_room = room['treasure']

    if current_room == room['treasure'] and command == "s":
        Darren.current_room = room['narrow']


#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

print('im the curren room',Darren.current_room)
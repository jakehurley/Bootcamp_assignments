#adventure game
# Define the rooms and their descriptions
rooms = {
    "Corridor": "You are in a corridor leads to the main hall and lifts.",
    "Main Hall": "You are in the main hall. There is a grand chandelier hanging from the ceiling,has immense L-shaped coach and a long desk. Looks like people using this area for leisure time.",
    "Manager's Office": "You are in the manager's room. There is a desk with a comfy office chair which has a huge bookshelf and a tv unite.",
    "Meeting Room": "You are in the meeting room. There is a long conference table.",
    "Team Leader's Office": "You are in the team leader's office.",
    "Emergency Exit": "You are in emergecy room. The walls are covered in symbols leads to the emergency exit",
    "Big Office": "You are in a big office. It is spacious and well-lit.There are several cubicles",
    "Kitchen": "You are in the kitchen.",
    "Balcony": "You are on the balcony. You have a view of the garden below."
}

# Define the room connections
room_connections = {
    "Main Hall": {"north": "Balcony", "south": "Corridor", "northwest": "Manager's Office", "southwest": "Team Leader's Office","northeast":"Emergency Exit","east":"Big Office","southeast":"Kitchen","west":"Team Leader's Office"},
    "Corridor": {'north': 'Main Hall'},
    "Manager's Office": {"east": "Main Hall", "north": "Balcony", "south": "Meeting Room"},
    "Team Leader's Office": {"north":"Meeting Room","east":"Main Hall",},
    "Balcony": {'south': 'Main Hall', 'southwest': 'Manager Room'},
    "Meeting Room": {"north": "Manager Room", "south": "Team Leader's Office", 'west': 'Main Hall'},
    "Emergency Exit": {'east': 'Main Hall'},
    "Big Office": {'west': 'Main Hall', 'south': 'Kitchen'},
    "Kitchen": {'north': 'Big Office', 'east': 'Main Hall'},
}

# Initialize the player's position
current_room = "Main Hall"

# Main game loop
while True:
    # Display the current room's description
    print(rooms[current_room])

    # List available directions
    available_directions = room_connections[current_room].keys()
    print('Available directions:', ', '.join(available_directions))

    # Get user input
    user_input = input('Enter your move (e.g., "north", "east", "south", "west","southwest","southeast","northeast","northwest" or "quit"): ').lower()

    # Check if the user wants to quit the game
    if user_input == 'quit':
        print('Thanks for playing!')
        break

    # Check if the entered direction is valid
    if user_input in available_directions:
        current_room = room_connections[current_room][user_input]
    else:
        print('You can\'t move in that direction. Try a different direction or "quit".')
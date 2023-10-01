# The Haunted Door - A Halloween Adventure
print("Welcome to 'The Haunted Door' - A Halloween Adventure!")
print("You find yourself in a spooky, ancient castle on Halloween night.")
print("You see three mysterious doors in front of you.")

# Ask the player to choose a door
door_choice = input("Which door will you choose? (1/2/3): ")

# Use conditional statements to create different outcomes based on the door choice
if door_choice == "1":
    print("\nYou open the first door and find a room filled with friendly ghosts.")
    print("They offer you a bowl of candy. Happy Halloween!")
elif door_choice == "2":
    print("\nYou open the second door and are greeted by a mischievous witch.")
    print("She offers you a choice: a trick or a treat. What will you choose?")
    trick_or_treat = input("Type 'trick' or 'treat': ")
    if trick_or_treat == "trick":
        print("\nThe witch casts a funny spell, and you turn into a pumpkin!")
        print("Game over!")
    elif trick_or_treat == "treat":
        print("\nThe witch gives you a bag of delicious Halloween treats.")
        print("You continue your adventure.")
    else:
        print("\nInvalid choice. The witch disappears, and you're stuck.")
        print("Game over!")
else:  # This covers door_choice == "3" or any other input
    print("\nYou open the third door and find yourself in a room with a friendly vampire.")
    print("He offers to take you on a thrilling night flight.")
    flight_choice = input("Do you want to go on the flight? (yes/no): ")
    if flight_choice.lower() == "yes":
        print("\nYou embark on a breathtaking night flight with the vampire.")
        print("What an amazing Halloween adventure!")
    else:
        print("\nYou decline the offer and explore the castle further.")
        print("The adventure continues.")

# Thank the player for playing
print("\nThank you for playing 'The Haunted Door' - A Halloween Adventure!")

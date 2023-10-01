# Space Exploration - A Galactic Adventure

print("Welcome to 'Space Exploration' - A Galactic Adventure!")
print("You are an astronaut on a mission to explore the cosmos.")
print("You find yourself in a spaceship with three different routes to choose from.")

# Ask the player to choose a route
print("Routes:")
print("1. Route to the Mysterious Nebula")
print("2. Route to the Red Planet Mars")
print("3. Route to the Distant Exoplanet Kepler-186f")

route_choice = input("Choose a route (1/2/3): ")

# Use conditional statements to create different outcomes based on the route choice
if route_choice == "1":
    print("\nYou embark on the route to the Mysterious Nebula.")
    print("As you approach, you encounter a colorful swirl of gas and stars.")
    print("Do you wish to investigate it further?")
    nebula_choice = input("Type 'yes' or 'no': ")
    if nebula_choice.lower() == "yes":
        print("\nYou navigate the nebula and discover an ancient alien artifact.")
        print("It's a remarkable find for humanity!")
    else:
        print("\nYou continue on your route, bypassing the nebula.")
        print("The adventure continues.")
elif route_choice == "2":
    print("\nYou choose the route to the Red Planet Mars.")
    print("As you land, you spot signs of Martian life!")
    print("Do you want to explore further?")
    mars_choice = input("Type 'yes' or 'no': ")
    if mars_choice.lower() == "yes":
        print("\nYou explore Martian terrain and make groundbreaking discoveries.")
        print("Your mission is a huge success!")
    else:
        print("\nYou return to your spaceship and continue your journey.")
        print("The adventure continues.")
else:  # This covers route_choice == "3" or any other input
    print("\nYou opt for the route to the Distant Exoplanet Kepler-186f.")
    print("As you approach the exoplanet, you receive a strange signal.")
    print("Do you wish to investigate the signal source?")
    signal_choice = input("Type 'yes' or 'no': ")
    if signal_choice.lower() == "yes":
        print("\nYou trace the signal to an alien civilization and make first contact!")
        print("Humanity's place in the cosmos is forever changed.")
    else:
        print("\nYou continue your exploration of the exoplanet's surface.")
        print("The adventure continues.")

# Thank the player for playing
print("\nThank you for playing 'Space Exploration' - A Galactic Adventure!")

import random

# Function to display game introduction
def introduction():
    print("Welcome to Space Exploration!")
    print("You're on a mission to explore the far reaches of the galaxy.")
    print("Your decisions will determine your success in this adventure.")
    print("Good luck!\n")

# Function to get player's name
def get_player_name():
    name = input("Enter your astronaut name: ")
    return name

# Function to simulate a space journey
def space_journey(player_name):
    distance = 0
    resources = {
        "fuel": 100,
        "food": 50,
    }

    while distance < 1000:
        print("\n--- Space Journey ---")
        print(f"Distance from Earth: {distance} light-years")
        print(f"Fuel: {resources['fuel']} units")
        print(f"Food: {resources['food']} units")

        action = input("What will you do? (1. Travel, 2. Rest, 3. Quit): ")

        if action == "1":  # Travel
            fuel_needed = random.randint(10, 30)
            distance_traveled = random.randint(50, 150)

            if resources['fuel'] >= fuel_needed:
                distance += distance_traveled
                resources['fuel'] -= fuel_needed
                resources['food'] -= 10
                print(f"You traveled {distance_traveled} light-years.")
            else:
                print("You don't have enough fuel to travel.")

        elif action == "2":  # Rest
            resources['food'] += 10
            print("You rested and replenished your food supply.")

        elif action == "3":  # Quit
            print(f"{player_name}, your space journey ends here.")
            break

        else:
            print("Invalid choice. Choose 1, 2, or 3.")

        # Check for game over conditions
        if resources['food'] <= 0:
            print("You ran out of food. Game over!")
            break
        if resources['fuel'] <= 0:
            print("You ran out of fuel. Game over!")
            break

    if distance >= 1000:
        print(f"Congratulations, {player_name}! You successfully explored the galaxy!")
    

# Main game loop
def main():
    introduction()
    player_name = get_player_name()
    space_journey(player_name)


if __name__ == "__main__":
    main()

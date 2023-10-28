import random

# Initialize player and team stats
team = {
    "name": "",
    "budget": 1000000,
    "players": [],
}

# Define player positions and their corresponding stats
positions = {
    "striker": {"min_price": 50000, "max_price": 100000, "min_skill": 70, "max_skill": 90},
    "midfielder": {"min_price": 40000, "max_price": 80000, "min_skill": 60, "max_skill": 85},
    "defender": {"min_price": 30000, "max_price": 60000, "min_skill": 50, "max_skill": 80},
    "goalkeeper": {"min_price": 20000, "max_price": 40000, "min_skill": 40, "max_skill": 70},
}

# Function to display game introduction
def introduction():
    print("Welcome to Python Football Manager!")
    print("You are the manager of a football team.")
    print("Buy and sell players, manage your budget, and lead your team to victory!")
    print("Good luck!\n")

# Function to get team name
def get_team_name():
    team["name"] = input("Enter your team's name: ")

# Function to display team and player stats
def display_stats():
    print(f"\n{team['name']}'s Budget: ${team['budget']}")
    print("Your Team:")
    for player in team["players"]:
        print(f"{player['name']} ({player['position']} | Skill: {player['skill']} | Price: ${player['price']}K)")

# Function to simulate player transfer market
def transfer_market():
    print("\n--- Transfer Market ---")
    print("Available Players:")
    for position, stats in positions.items():
        player = generate_random_player(position, stats)
        print(f"{position.capitalize()}: {player['name']} | Skill: {player['skill']} | Price: ${player['price']}K")

    action = input("What will you do? (1. Buy Player, 2. Pass): ")

    if action == "1":  # Buy Player
        position = input("Enter the position you want to buy: ").lower()
        if position in positions:
            player = generate_random_player(position, positions[position])
            if team["budget"] >= player["price"]:
                team["players"].append(player)
                team["budget"] -= player["price"]
                print(f"You bought {player['name']} for ${player['price']}K!")
            else:
                print("You don't have enough budget to buy this player.")
        else:
            print("Invalid position. Choose striker, midfielder, defender, or goalkeeper.")
    
    elif action == "2":  # Pass
        print("You passed on this opportunity.")

    else:
        print("Invalid choice. Choose 1 or 2.")

# Function to generate a random player
def generate_random_player(position, stats):
    player = {
        "name": random.choice(["John", "Michael", "David", "Emma", "Sophia", "Oliver"]),
        "position": position,
        "skill": random.randint(stats["min_skill"], stats["max_skill"]),
        "price": random.randint(stats["min_price"], stats["max_price"]) / 1000,  # Represent price in K$
    }
    return player


# Main game loop
def main():
    introduction()
    get_team_name()

    while team["budget"] > 0:
        display_stats()
        transfer_market()

    print(f"Game Over, {team['name']}! You've managed your team and budget well.")


if __name__ == "__main__":
    main()

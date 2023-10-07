import random

# Initialize player and enemy stats
player = {
    "name": "",
    "health": 100,
    "attack": 20,
    "defense": 10,
    "gold": 50,
    "potions": 3,
}

enemies = [
    {"name": "Goblin", "health": 30, "attack": 10, "defense": 5},
    {"name": "Orc", "health": 50, "attack": 15, "defense": 8},
    {"name": "Dragon", "health": 100, "attack": 30, "defense": 20},
]

# Function to display game introduction
def introduction():
    print("Welcome to Heroes of Python and Magic!")
    print("You are the hero of this world, and you must defeat the evil creatures.")
    print("Collect gold, buy potions, and defeat the enemies to win the game.")
    print("Good luck!\n")

# Function to get player's name
def get_player_name():
    player["name"] = input("Enter your hero's name: ")

# Function to display player and enemy stats
def display_stats():
    print(f"\n{player['name']}'s Stats:")
    print(f"Health: {player['health']}")
    print(f"Gold: {player['gold']}")
    print(f"Potions: {player['potions']}\n")

    print("Enemies:")
    for index, enemy in enumerate(enemies):
        print(f"{index + 1}. {enemy['name']} - Health: {enemy['health']}")

# Function to perform a battle with an enemy
def battle(enemy):
    while player["health"] > 0 and enemy["health"] > 0:
        print(f"\n{player['name']} vs {enemy['name']}")
        print(f"{player['name']}'s Health: {player['health']}")
        print(f"{enemy['name']}'s Health: {enemy['health']}\n")

        action = input("What will you do? (1. Attack, 2. Use Potion): ")

        if action == "1":  # Attack
            player_damage = player["attack"] - enemy["defense"]
            enemy_damage = enemy["attack"] - player["defense"]

            if player_damage > 0:
                enemy["health"] -= player_damage
                print(f"You hit {enemy['name']} for {player_damage} damage!")

            if enemy["health"] > 0 and enemy_damage > 0:
                player["health"] -= enemy_damage
                print(f"{enemy['name']} hits you for {enemy_damage} damage!")

        elif action == "2":  # Use Potion
            if player["potions"] > 0:
                player["health"] += random.randint(15, 30)
                player["potions"] -= 1
                print(f"{player['name']} used a potion and healed!")

        else:
            print("Invalid choice. Choose 1 or 2.")

    if player["health"] <= 0:
        print(f"{player['name']} was defeated by {enemy['name']}!")

    if enemy["health"] <= 0:
        print(f"{player['name']} defeated {enemy['name']} and earned {enemy['health']} gold!")
        player["gold"] += enemy["health"]


# Main game loop
def main():
    introduction()
    get_player_name()

    while player["health"] > 0 and len(enemies) > 0:
        display_stats()
        enemy = random.choice(enemies)
        input("Press Enter to battle!")
        battle(enemy)
        enemies.remove(enemy)

    if player["health"] > 0:
        print(f"Congratulations, {player['name']}! You defeated all the enemies and won the game with {player['gold']} gold!")


if __name__ == "__main__":
    main()

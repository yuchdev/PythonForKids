import random
from players_data import football_data, football_clubs


def intro_screen():
    print("Welcome to Python Football Manager!")
    print("You are the manager of a football team.")
    print("Buy and sell players, manage your budget, and lead your team to victory!")
    print("Good luck!\n")


def team_formation():

    # Create a dictionary for your team
    team = {"name": input("Enter your team's name: ")}

    # Choose your game complexity (easy, medium, hard)
    print("Choose your game complexity:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    complexity = input("Enter your choice: ")

    # Set your team's budget based on the game complexity
    if complexity == "1":
        team["budget"] = 3000000000
    elif complexity == "2":
        team["budget"] = 2000000000
    elif complexity == "3":
        team["budget"] = 1500000000
    else:
        print("Invalid choice. Setting game complexity to easy.")
        team["budget"] = 100000000

    # Set your team's strategy (attacking, balanced, defensive)
    print("Choose your team's strategy:")
    print("1. Attacking")
    print("2. Balanced")
    print("3. Defensive")
    strategy = input("Enter your choice: ")

    # Set your team's formation based on the strategy
    # Attacking: 5-3-2-1
    # Balanced: 3-3-4-1
    # Defensive: 2-4-4-1
    if strategy == "1":
        team["formation"] = "5-3-2-1"
    elif strategy == "2":
        team["formation"] = "3-3-4-1"
    elif strategy == "3":
        team["formation"] = "2-4-4-1"
    else:
        print("Invalid choice. Setting team strategy to attacking.")
        team["formation"] = "4-3-2-1"  # -> [4, 3, 2, 1]

    # Choose automatic or manual player selection
    print("Choose your player selection method:")
    print("1. Automatic")
    print("2. Manual")
    selection = input("Enter your choice: ")
    if selection == "1":
        team = automatic_team(team)
    elif selection == "2":
        team = manual_team(team)
    else:
        print("Invalid choice. Setting player selection method to automatic.")
        team = automatic_team(team)
    return team


def available_players(data, role):
    """
    Return list of available players based on the role
    :param data: list of player
    :param role: player role
    """
    players = []
    for player in data:
        if player["role"] == role:
            players.append(player)
    players.sort(key=lambda x: x["contract_price"], reverse=True)
    return players


def pick_random_player(data, role):
    """
    Pick random player from the data based on the role
    :param data: list of players
    :param role: player role
    """
    players = available_players(data, role)
    return random.choice(players)


def manual_purchase(data, role):
    available = available_players(data, role)
    print(f"Available {role}s:")
    for i, player in enumerate(available):
        print(f"{i + 1}. {player['name']} | Skill: {player['efficiency']} | Price: ${player['contract_price']}")
    choice = input("Enter your choice: ")
    if choice.isdigit():
        choice = int(choice)
        if 0 < choice <= len(available):
            return available[choice - 1]
        else:
            print("Invalid choice.")
    else:
        print("Invalid choice.")
    return None


def manual_team(team):
    while len(team["players"]) < 11:
        print("Choose role for player you want to buy:")
        print("1. Striker")
        print("2. Midfielder")
        print("3. Defender")
        print("4. Goalkeeper")
        role = input("Enter your choice: ")
        if role == "1":
            player = manual_purchase(football_data, "Striker")
        elif role == "2":
            player = manual_purchase(football_data, "Midfielder")
        elif role == "3":
            player = manual_purchase(football_data, "Defender")
        elif role == "4":
            player = manual_purchase(football_data, "Goalkeeper")
        else:
            print("Invalid choice.")
            player = None
        if player is not None:
            if team["budget"] >= player["contract_price"]:
                team["budget"] -= player["contract_price"]
                team["players"].append(player)
            else:
                print(f"You don't have enough budget to buy {player['name']}")
    return team


def automatic_team(team):
    # Automatically generate players based on the team's formation
    # parse formation to get numbers
    numbers = team["formation"].split("-")
    attackers, midfielders, defenders, goalkeepers = int(numbers[0]), int(numbers[1]), int(numbers[2]), int(
        numbers[3])

    team["players"] = []
    while len(team["players"]) < 11:
        if attackers > 0:
            player = pick_random_player(football_data, "Striker")
            attackers -= 1
        elif midfielders > 0:
            player = pick_random_player(football_data, "Midfielder")
            midfielders -= 1
        elif defenders > 0:
            player = pick_random_player(football_data, "Defender")
            defenders -= 1
        else:
            player = pick_random_player(football_data, "Goalkeeper")
            goalkeepers -= 1
        if team["budget"] >= player["contract_price"]:
            team["budget"] -= player["contract_price"]
            team["players"].append(player)
        else:
            print(f"You don't have enough budget to buy {player['name']}, new attempt...")
            team["players"] = []
    for player in team["players"]:
        print(f"{player['role']} {player['name']} | Skill: {player['efficiency']} | Price: ${player['contract_price']}")
    return team


def game_loop(team):
    pass


def main():
    intro_screen()
    team = team_formation()
    game_loop(team)


if __name__ == "__main__":
    main()

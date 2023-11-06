import copy
import random
import time
import json
from players_data import football_data
from football_clubs import football_clubs


def intro_screen():
    print("Welcome to Python Football Manager!")
    print("You are the football_manager of a football team.")
    print("Buy and sell players, manage your budget, and lead your team to victory!")
    print("Good luck!\n")


def load_game():
    try:
        f = open("save_game.json", "r")
        team = json.loads(f.read())
        f.close()
        print(f"Loaded game: {team['name']}")
        print(f"Team's budget: ${team['budget']}")
        print(f"Team's formation: {team['formation']}")
        print(f"Team's players: {team['players']}")
        return team
    except FileNotFoundError:
        print("No save game found. Starting new game...")
        return None


def save_game(team):
    f = open("save_game.json", "w")
    f.write(json.dumps(team))
    f.close()


def new_game():
    # Create a dictionary for your team
    team = {
        "name": input("Enter your team's name: "),
        "budget": 0,
        "city": input("Enter your team's city: "),
        "country": input("Enter your team's country: "),
        "stadium": input("Enter your team's stadium: "),
        "players": []
    }

    # Choose your game complexity (easy, medium, hard)
    print("Choose your game complexity:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    complexity = input("Enter your choice: ")
    print(f"You choose {complexity} game complexity")

    # Set your team's budget based on the game complexity
    if complexity == "1":
        team["budget"] = 3000000000
    elif complexity == "2":
        team["budget"] = 2000000000
    elif complexity == "3":
        team["budget"] = 1500000000
    else:
        print("Invalid choice. Setting game complexity to easy.")
        team["budget"] = 3000000000
    print(f"Your team's budget is ${team['budget']}")

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
        print(f"Your team's strategy is attacking.")
        team["formation"] = "5-3-2-1"
    elif strategy == "2":
        print(f"Your team's strategy is balanced.")
        team["formation"] = "3-3-4-1"
    elif strategy == "3":
        print(f"Your team's strategy is defensive.")
        team["formation"] = "2-4-4-1"
    else:
        print("Invalid choice. Setting team strategy to attacking.")
        team["formation"] = "5-3-2-1"  # -> [4, 3, 2, 1]
    print(f"Your team's formation is {team['formation']}")

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

    # Ask if player wants to save the game
    print("Do you want to save the game?")
    print("1. Yes")
    print("2. No")
    choice = input("Enter your choice: ")
    if choice == "1":
        save_game(team)
    elif choice == "2":
        print("Game not saved.")
    else:
        print("Invalid choice. Game not saved.")
    return team


def team_formation():

    # Choose new game or load game
    print("Choose your game mode:")
    print("1. New game")
    print("2. Load game")
    mode = input("Enter your choice: ")
    if mode == "1":
        print(f"Starting new game...")
        team = new_game()
    elif mode == "2":
        print(f"Loading game...")
        team = load_game()
    else:
        print("Invalid choice. Starting new game...")
        team = new_game()
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
            # remove this player from data
            data.remove(available[choice - 1])
            # return chosen player from the list
            return available[choice - 1]
        else:
            print("Invalid choice.")
    else:
        print("Invalid choice.")
    return None


def manual_team(team):
    football_data_copy = copy.deepcopy(football_data)
    while len(team["players"]) < 11:
        print("Choose role for player you want to buy:")
        print("1. Striker")
        print("2. Midfielder")
        print("3. Defender")
        print("4. Goalkeeper")
        role = input("Enter your choice: ")
        if role == "1":
            player = manual_purchase(football_data_copy, "Striker")
        elif role == "2":
            player = manual_purchase(football_data_copy, "Midfielder")
        elif role == "3":
            player = manual_purchase(football_data_copy, "Defender")
        elif role == "4":
            player = manual_purchase(football_data_copy, "Goalkeeper")
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
        print(f"{player['role']} {player['name']} | " +
              f"Skill: {player['efficiency']} | " +
              f"Age: {player['age']} | " +
              f"Price: ${player['contract_price']}")
    return team


def group_stage(groups):
    for group, teams in groups.items():
        print(f"Group {group}: {[team['name'] for team in teams]}")
        group_results = group_stage_play(group, teams)
        # Pick teams with 2 highest scores

    print("Group stage is over. Press button to start playoffs...")


def group_stage_play(group, teams):
    print(f"Group stage: group {group}")
    group_results = {}
    for left_team_index in range(len(teams)):
        for right_team_index in range(left_team_index + 1, len(teams)):
            left_team = teams[left_team_index]
            right_team = teams[right_team_index]
            print(f"Group {group} game: {left_team['name']} vs {right_team['name']}")
            team1_score = random.randint(0, 5)
            team2_score = random.randint(0, 5)
            print(f"Game result: {team1_score} : {team2_score}")
            if team1_score > team2_score:
                winner = left_team['name']
                print(f"Winner: {winner}")
                group_results[winner] = group_results.get(winner, 0) + 3
            elif team1_score < team2_score:
                winner = right_team['name']
                print(f"Winner: {winner}")
                group_results[winner] = group_results.get(winner, 0) + 3
            else:
                print("Draw")
                draw_team1 = left_team['name']
                draw_team2 = right_team['name']
                group_results[draw_team1] = group_results.get(draw_team1, 0) + 1
                group_results[draw_team2] = group_results.get(draw_team2, 0) + 1
            time.sleep(1)
            print()

    # convert dict to list of dicts {"name": "team_name", "score": 5}
    group_results = [{"name": team_name, "score": score} for team_name, score in group_results.items()]

    # sort by score
    group_results.sort(key=lambda x: x["score"], reverse=True)

    # return 2 top teams
    return group_results[0:2]


def pick_clubs():
    """
    Pick up 15 teams from the list of football clubs
    """
    teams = []
    while len(teams) < 15:
        team = random.choice(football_clubs)
        if team not in teams:
            teams.append(team)
    return teams


def break_into_groups(teams):
    """
    Break teams into groups A, B, C, D
    """
    groups = {
        "A": [],
        "B": [],
        "C": [],
        "D": []
    }

    groups["A"].extend(teams[0:4])
    groups["B"].extend(teams[4:8])
    groups["C"].extend(teams[8:12])
    groups["D"].extend(teams[12:16])
    return groups


def main():
    intro_screen()
    team = team_formation()

    print(f"Following clubs participate in the season 2024:")
    clubs = pick_clubs()
    groups = break_into_groups(clubs)
    print(f'Adding {team["name"]} to group D {groups["D"]}')
    groups['D'].append({"name": team["name"], "budget": team["budget"]})
    group_stage(groups)


if __name__ == "__main__":
    main()

players_list = {
    "Lionel Messi": {"age": 34, "role": "Forward", "goals_scored": 30, "contract_price": 200000000, "country": "Argentina"},
    "Cristiano Ronaldo": {"age": 36, "role": "Forward", "goals_scored": 30, "contract_price": 175000000, "country": "Portugal"},
    "Neymar Jr.": {"age": 28, "role": "Forward", "goals_scored": 20, "contract_price": 150000000, "country": "Brazil"},
    "Kylian Mbappé": {"age": 22, "role": "Forward", "goals_scored": 5, "contract_price": 160000000, "country": "France"},
}

ages_list = [
    34,
    36,
    28,
    34
]

roles_list = [
    "Forward",
    "Forward",
    "Forward",
    "Defender"
]

goals_scored_list = [
    30,
    30,
    20,
    5
]

for player_name, player_info in players_list.items():
    print(f"Player name: {player_name}")
    for key, value in player_info.items():
        print(f"    {key}: {value}")

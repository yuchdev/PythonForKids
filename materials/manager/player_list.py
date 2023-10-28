from players_data import football_data

# List of football players
football_players = [
    "Lionel Messi",
    "Cristiano Ronaldo",
    "Neymar Jr.",
    "Kylian Mbappé",
    "Robert Lewandowski",
    "Sergio Ramos",
    "Kevin De Bruyne",
    "Virgil van Dijk",
    "Mohamed Salah",
    "Karim Benzema",
    "Luka Modrić",
    "Joshua Kimmich",
    "Harry Kane",
    "Erling Haaland",
    "Sadio Mané",
    "Bruno Fernandes",
    "Manuel Neuer",
    "Jadon Sancho",
    "Antoine Griezmann",
    "Eden Hazard",
    "Raheem Sterling",
    "Toni Kroos",
    "Gareth Bale",
    "Marc-André ter Stegen",
    "Paul Pogba",
    "Thibaut Courtois",
    "Lautaro Martínez",
    "Marco Reus",
    "Serge Gnabry",
    "Gianluigi Donnarumma",
    "Phil Foden"
]

# List of contract prices for the football players
contract_prices = [
    200000000,  # Messi's contract price
    175000000,  # Ronaldo's contract price
    150000000,  # Neymar's contract price
    160000000,  # Mbappé's contract price
    120000000,  # Lewandowski's contract price
    80000000,   # Ramos's contract price
    130000000,  # De Bruyne's contract price
    100000000,  # Van Dijk's contract price
    140000000,  # Salah's contract price
    110000000,  # Benzema's contract price
    90000000,   # Modrić's contract price
    95000000,   # Kimmich's contract price
    120000000,  # Kane's contract price
    140000000,  # Haaland's contract price
    90000000,   # Mané's contract price
    120000000,  # Fernandes's contract price
    100000000,  # Neuer's contract price
    85000000,   # Sancho's contract price
    120000000,  # Griezmann's contract price
    110000000,  # Hazard's contract price
    110000000,  # Sterling's contract price
    90000000,   # Kroos's contract price
    80000000,   # Bale's contract price
    100000000,  # ter Stegen's contract price
    120000000,  # Pogba's contract price
    95000000,   # Courtois's contract price
    100000000,  # Martínez's contract price
    80000000,   # Reus's contract price
    90000000,   # Gnabry's contract price
    80000000,   # Donnarumma's contract price
    90000000    # Foden's contract price
]

print("In this season " +
      str(len(football_players)) +
      " players available:" +
      str(football_players))

# Make print sentence "Second player in the list: " ... " and his price " ...
print(f"Second player in the list {football_players[1]} and his price {contract_prices[1]}")

assert len(football_data) == len(football_players) == len(contract_prices)

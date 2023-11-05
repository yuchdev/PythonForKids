# Save and load game
team_name = input("Enter your team's name: ")
team_stadium = input("Enter your team's stadium: ")

print(f"Your team's name is {team_name} and your team's stadium is {team_stadium}")

f = open("save_game.txt", "w")
f.write(team_name)
f.write(' ')
f.write(team_stadium)
f.close()

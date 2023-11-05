# Introduction to Loops

# Explain the concept of loops, which allow us to repeat actions or processes in programming.

# Real-World Examples
# Provide real-world examples like brushing teeth, counting stars, or flipping pancakes to illustrate the concept of repetition.

# Loops in Action
# Highlight the idea that loops can help automate repetitive tasks in code.

# Adding For-Loops to the Game

# Show how to use a ranged for-loop to repeat a block of code a specific number of times.

# Example - Launching Space Probes
for probe in range(3):
    print(f"Launching space probe {probe + 1}")
    # Code for launching the probe

# Integrate into the Game
# Integrate a for-loop into the "Space Exploration" game to simulate launching probes and exploring different areas of space.


# The Infinite Universe with While-Loops

# Introduce while-loops, explaining that they repeat code until a certain condition is met.

# Example - Infinite Space
galaxies_discovered = 0
while True:
    galaxies_discovered += 1
    print(f"Discovered galaxy {galaxies_discovered}")
    if galaxies_discovered >= 10:
        break  # Exit the loop after discovering 10 galaxies

# Discuss how while-loops can help explore infinite possibilities like discovering new galaxies.


# Enhancing the Game with While-Loops

# Show how to use a while-loop in the game to create a scenario where players can continue exploring space indefinitely.

# Exiting the Loop
player_choice = ""
while player_choice != "return to Earth":
    player_choice = input("What's your next move? (return to Earth/explore further): ")
    # Code to handle the player's choice



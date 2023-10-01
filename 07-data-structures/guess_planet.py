import random

# List of planets
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# Randomly select a planet from the list
selected_planet = random.choice(planets)

# Create a list to store correct guesses
correct_guesses = []

# Initialize the number of attempts
attempts = 7

print("Welcome to the 'Guess the Planet' game!")
print("Can you guess the name of the hidden planet?")

while attempts > 0:
    # Display the planet name with asterisks for hidden letters
    hidden_name = ""
    for letter in selected_planet:
        if letter in correct_guesses:
            hidden_name += letter
        else:
            hidden_name += "*"
    
    print("\nGuess the planet:", hidden_name)
    print(f"Attempts left: {attempts}")
    
    # Ask the player to guess a letter
    guess = input("Guess a letter or the whole planet: ").strip()
    
    if len(guess) == 1:  # Guessing a letter
        if guess in selected_planet:
            correct_guesses.append(guess)
            print("Correct guess!")
        else:
            print("Incorrect guess.")
            attempts -= 1
    elif guess.lower() == selected_planet.lower():  # Guessing the whole planet
        print(f"Congratulations! You've guessed it. The planet is {selected_planet}.")
        break
    else:
        print("Incorrect guess.")
        attempts -= 1

# Check if the player won or ran out of attempts
if attempts == 0:
    print("\nYou've run out of attempts. The planet was", selected_planet)
    
print("\nThank you for playing the 'Guess the Planet' game!")

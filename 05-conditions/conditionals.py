__doc__ = """

Should I go outside?

  |
 [Yes]
  v
Is it sunny?
  |
 [Yes]
  v
Take sunglasses.
  |
 [No]
  v
Take an umbrella.
  |
 [No]
  v
Enjoy the weather.


Title: The Enchanted Forest

Once upon a time in the Enchanted Forest, a brave adventurer named Alex faced a decision.

Alex came across a fork in the path. Should Alex go left or right?

[Left] - Alex decides to go left, and soon finds a hidden treasure chest.
[Right] - Alex chooses the right path, and stumbles upon a magical creature.

What should Alex do now?

"""

print("Welcome to the Adventure!")
decision = input("Do you want to go on an adventure? (yes/no): ")

if decision == "yes":
    print("Great! You're on an adventure.")
elif decision == "no":
    print("That's okay, maybe next time.")
else:
    print("I didn't understand your choice.")


# Collaborative Adventure Game (a simplified example)

print("You're in a dark cave with two paths. Left or right?")
path_choice = input("Which path will you choose? (left/right): ")

if path_choice == "left":
    print("You've found a chest full of gold!")
elif path_choice == "right":
    print("Oh no, a dragon! Run!")
else:
    print("I didn't understand your choice.")


decision_tree = """
Title: My Adventure

Start

Decision 1:
  [Option A]
  [Option B]

  If Option A:
    Decision 2:
      [Option X]
      [Option Y]

      If Option X:
        End - You found a hidden treasure!
      If Option Y:
        End - You met a friendly alien!

  If Option B:
    Decision 3:
      [Option P]
      [Option Q]

      If Option P:
        End - You entered a haunted house.
      If Option Q:
        End - You discovered a magical forest.

End

"""
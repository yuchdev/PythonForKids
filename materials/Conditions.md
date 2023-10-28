## Conditions

**What are Conditions in Programming?**

Conditions in programming are like "If-Then" statements or rules that help the computer make decisions. Just like how you make decisions in your everyday life, like "If it's raining, then I'll take an umbrella," computers use conditions to make choices based on certain situations or facts.

**How Do Conditions Work?**

Imagine you're playing a game, and you want to check if you've collected enough points to win. You might say, "If I have more than 100 points, then I win!" In programming, we use a similar structure.

We have a question (called a condition), and we check if it's true or false. If it's true, we do one thing, and if it's false, we do something else.

**Example in Real Life:**

Let's say you're going to the park with a friend, and you want to know if you should bring a soccer ball. You might ask:

    If my friend is coming, then I'll bring a soccer ball.
    If my friend isn't coming, then I won't bring a soccer ball.

This is a simple condition you use in your daily life to decide whether to bring the soccer ball or not.

**Example in Programming:**

```
if friend == True:
    bring_soccer_ball()
else:
    do_not_bring_soccer_ball()
```

```
if lives > 0:
    keep_playing()
else:
    game_over()
```

In the code above, we're asking, "If the player has more than 0 lives, then continue the game; otherwise, it's game over."

**The Key Parts of a Condition:**

* **If**: This is where we ask a question or set a condition.
* **Condition**: It's like the "If-Then" rule we want to check (e.g., lives > 0).
* **Then**: This is what happens if the condition is true.
* **Else**: This is what happens if the condition is false.

**Multiple Choices in Conditions: Making Decisions with More Options**

You know how you make choices every day, like picking your favorite ice cream flavor from a variety of options? Well, in programming, we have a way to make decisions when we have several choices, and we call it "multiple choices in conditions."

**Imagine a Snack Bar:**

Let's say you're at a snack bar, and you have a choice of different snacks like popcorn, candy, and chips. You might choose one based on different conditions:

* If you're in the mood for something sweet, then you'll pick candy.
* If you're feeling salty, then you'll go for chips.
* If you want something crunchy, then you'll get popcorn.

In programming, we can do something similar. We can set up a condition with multiple choices to decide what the computer should do.

<div style="page-break-after: always;"></div>

**Example in Programming:**

Imagine you're writing a program for a robot that helps with chores. You want the robot to decide which chore to do based on different conditions. Here's how you might write it in code:

```
if day == "Monday":
    # Robot does the laundry
elif day == "Wednesday":
    # Robot washes the dishes
elif day == "Friday":
    # Robot vacuums the floor
else:
    # Robot takes a break
```
In this code:

* **If** it's Monday, the robot does the laundry.
* **Else if** it's Wednesday, the robot washes the dishes.
* **Else if** it's Friday, the robot vacuums the floor.
* **Else** (if it's not any of those days), the robot takes a break.

The robot has multiple choices for its chores, and it picks the one that matches the condition (the day of the week).

The Key Parts of Multiple Choices:

* If: This is where we start the condition.
* Condition: It's like the question we're asking (e.g., "Is it Monday?").
* Else if: This is where we add more conditions and choices.
* Else: This is what happens if none of the conditions are true.

So, just like choosing snacks at the snack bar, we use multiple choices in conditions to help our programs make decisions when there are lots of options. It's like giving our programs a list of choices and telling them what to do based on different situations.

**In Summary:**

Conditions in programming are like decision-making rules. We use them to make our code do different things based on whether a statement is true or false. It's just like how you make decisions in your daily life!

<div style="page-break-after: always;"></div>


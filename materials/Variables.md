## Variables

Variables in Python are like containers where we can store different types of information or data. 
Think of them as labeled boxes in which we can put things. 
This box is special because it can hold different things at different times. 
We give this box a name, like `player_name`. Inside the box, you can put different things. 
For example, you can put a player's name, the number of goals they scored, or their height. 
You can put words, whole numbers, or numbers with decimal points. 
Since our box has name "`player_name`", we put inside the text "`Lionel Messi`".

The sign `player_name` is called a **variable name**.

The text `Lionel Messi` is a **variable value**.

In Python, we use variables to hold and work with different types of information. For example:

```python
player_name = "Lionel Messi"
goals_scored = 10
height = 1.70
```

### Mathematical Variables Analogy

In math, you might have seen letters like "`x`" or "`y`" used as variables. 
They represent numbers that can change. 
For example, in an equation like `x + 5 = 10`, "`x`" is a variable, and it can be any number that makes the equation true.

You can create the same equation in Python like this:

```python
x = 5
print(x + 7)
```

In Python, variables are a bit like that, but they can also hold other things, not just numbers. 
For instance, you can have a variable called "my_name," and it can hold your name, like "Henry"

### Integer (int)

An integer variable is like a box for storing whole numbers, like how many goals a player scored in a game. It's for counting things.

For instance, if you have a variable called `goals_scored`, you can put a number of goals in it like this: 

```python
goals_scored = 10
```

### Float (float)

A float variable is similar to an integer, but it can store numbers with decimal points, 
like the player's height or the average number of goals per game.

Suppose you have a variable called height, you can put a decimal number in it like this: 

```python
height = 1.70
```

So, in Python, we use variables to hold and work with different types of information. 
We give each variable a name (like the label on a box) and then put the right kind of data inside it, 
whether it's words, whole numbers, or numbers with decimal points. 
This helps us do all sorts of cool stuff with our data in our Python programs!

### String (str)

Imagine a string variable like a box where you can keep words, sentences, or even names. It's like a container for text.

For example, if you have a variable called `player_name`, you can put a player's name inside it like this: `player_name = "Lionel Messi"`

### Formatting Strings in Python: A Fun Way to Make Text Look Cool

#### 1. F-Strings - The Magic of Curly Braces `{}`

Think of f-strings like magic placeholders for your words and numbers. They make it super easy to mix text and values in your messages. Here's how it works

```python
# Let's say you have a number (your age) and a name:
age = 12
name = "Alice"

# You can create a cool message with f-strings:
message = f"Hi, my name is {name}, and I'm {age} years old!"
print(message)
```

In this example:

* The f at the start tells Python it's an f-string.
* Inside the string, you use curly braces `{}` to show where your values will go.
* The variables (like name and age) fill in the curly braces. Python knows to replace them with the actual values.

You can use f-strings to make all sorts of messages, just like in this game:

```python
score = 100
message = f"Congratulations! You scored {score} points!"
```

#### 2. Concatenating Substrings with the Plus (+) Operator - Like Puzzle Pieces

Imagine you have pieces of a puzzle. You can put them together to create a bigger picture. 
Well, you can do the same with text in Python, using the plus (`+`) operator.

```python
# Let's say you have two pieces of a message:
greeting = "Hello, "
name = "Alice"

# You can put them together like a puzzle:
message = greeting + name
print(message)
```

In this example:

* You have two text pieces (variables greeting and name).
* You use the plus (`+`) sign to combine them into a single message.

```python
activity = "playing soccer"
weather = "sunny"
message = "Today, I'm " + activity + " in the " + weather + " weather."
```

**Important:** When using the plus (`+`) operator for combining text and values in Python, 
you need to be careful to convert non-string types to strings using `str()`.

Let me explain why and how this works:

**Python Loves Strings, but Not Always Numbers:**

In Python, when you use the plus (`+`) operator to combine things, like text and numbers, 
it expects everything to be a string. 
Python loves working with strings, but it doesn't automatically know how to mix them with other data types like numbers.

**The Downside: Type Error**

If you try to combine a number and a string without converting the number to a string, 
Python gets confused and might show an error. It's like speaking two different languages at the same time. 

For example:

```python
score = 100
message = "You scored " + score + " points!"
```

This might cause an error because Python can't directly add a number to text. 
It's a bit like trying to add apples to oranges – it just doesn't make sense!

**The Solution: `str()` to the Rescue!**

To avoid errors, you can use `str()` to convert non-string values (like numbers) into strings. 
It's like turning those apples into oranges, so you can mix them. Here's how you can fix the previous example:

```python
score = 100
message = "You scored " + str(score) + " points!"
```

By using `str()`, you tell Python to treat the number as a string, so you can safely mix it with text. 
It's like speaking the same language!

**The Upside: Flexibility**

The plus (+) operator is flexible, and once you convert everything to strings, 
you can combine text and numbers in various creative ways. 
So, it's a great tool once you know how to handle it.

Remember, in Python, it's essential to communicate clearly and make sure everything is in the same format 
when combining text and values. Keep your `str()` in your pocket, and you'll be a Python pro in no time! 

#### So, to Sum It Up:

* F-strings use curly braces `{}` to insert values into your text. It's like magic placeholders.
* Concatenating with the Plus (`+`) Operator is like putting pieces of a puzzle together to create a complete message.

You can create all sorts of messages this way, like:

<div style="page-break-after: always;"></div>



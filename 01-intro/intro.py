# Welcome to Python Pet's Coding Adventure!

# Example 1: A Simple Greeting
# Let's start with a basic Python code to make Python Pet say hello!
print("Hello, Python Pet!")

# Example 2: Basic Math
# Python can also help us with calculations.
# Let's calculate the sum of two numbers and print the result.
num1 = 5
num2 = 7
sum_result = num1 + num2
print("The sum of 5 and 7 is:", sum_result)

# Example 3: A Fun Drawing
# Now, let's create a more advanced program to draw a smiley face.
# We'll use the 'turtle' module to do this.
import turtle

# Create a turtle screen
screen = turtle.Screen()

# Create a turtle named 'smiley'
smiley = turtle.Turtle()

# Set the turtle's speed and shape
smiley.speed(0)
smiley.shape("circle")

# Draw a smiley face
smiley.penup()
smiley.goto(0, -100)
smiley.pendown()
smiley.begin_fill()
smiley.color("yellow")
smiley.circle(100)
smiley.end_fill()

# Draw the left eye
smiley.penup()
smiley.goto(-40, 50)
smiley.pendown()
smiley.begin_fill()
smiley.color("white")
smiley.circle(40)
smiley.end_fill()

# Draw the right eye
smiley.penup()
smiley.goto(40, 50)
smiley.pendown()
smiley.begin_fill()
smiley.color("white")
smiley.circle(40)
smiley.end_fill()

# Draw the mouth
smiley.penup()
smiley.goto(0, 20)
smiley.pendown()
smiley.setheading(-60)
smiley.pensize(2)
smiley.circle(60, 120)
smiley.hideturtle()

# Example 4: Adding an Image
# Now, let's add an image of Python Pet to our smiley face drawing.
# You can find the 'python.png' image asset in our materials.

# To add an image, we'll use the 'turtle' module and the 'PIL' library.
from turtle import RawTurtle, ScrolledCanvas
from PIL import Image

# Create a turtle screen with scrolling support
canvas = ScrolledCanvas()
screen = canvas.canv

# Create a new turtle named 'python_pet'
python_pet = RawTurtle(screen)

# Load the 'python.png' image
image = Image.open('python.png')

# Register the image as a turtle shape
screen.addshape("python_pet", shape=image)

# Set the turtle's shape to the loaded image
python_pet.shape("python_pet")

# Position the image on the canvas
python_pet.penup()
python_pet.goto(-30, 100)
python_pet.pendown()

# Hide the turtle
python_pet.hideturtle()

# That's it for our introductory lecture! Have fun on Python Pet's coding adventure!

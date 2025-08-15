import turtle
import math

# Draw a right angle triangle. Requires the knowledge of angle calculation

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")  # Set background color to black
screen.setup(800, 600)   # Set screen size to 800x600 pixels

# Set up the turtle
t = turtle.Turtle()
t.pencolor("green")     # Set pen color to green

# Draw a right-angled triangle (3-4-5 triangle)
scale = 50  # Scale factor to fit the screen
t.forward(3 * scale)  # First leg (3 units scaled)
t.left(90)            # Turn 90 degrees for the right angle
t.forward(4 * scale)  # Second leg (4 units scaled)
t.left(143)           # Figure it out by using calculator (or trial and error..start with 90, 100, and so on)
t.forward(5 * scale)  # Hypotenuse (5 units scaled)

# Keep the window open until clicked
turtle.done()
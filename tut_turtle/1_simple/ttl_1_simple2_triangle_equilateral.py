import turtle

# draw equilateral triangle step by step

# STEP1: Without for loop

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")  # Set background color to black
screen.setup(800, 600)   # Set screen size to 800x600 pixels

# Set up the turtle
t = turtle.Turtle()
t.pencolor("green")     # Set pen color to green

# Draw an equilateral triangle
side_length = 200       # Length of each side
t.forward(side_length)  # Move forward by side length
t.left(120)         # Turn 120 degrees (external angle)

t.forward(side_length)  # Move forward by side length
t.left(120)         # Turn 120 degrees (external angle)

t.forward(side_length)  # Move forward by side length
t.left(120)         # Turn 120 degrees (external angle)


# Keep the window open until clicked
turtle.done()

###################################################
# STEP2: With for loop

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")  # Set background color to black
screen.setup(800, 600)   # Set screen size to 800x600 pixels

# Set up the turtle
t = turtle.Turtle()
t.pencolor("green")     # Set pen color to green

# Draw an equilateral triangle
side_length = 200       # Length of each side
for i in range(3):
    t.forward(side_length)  # Move forward by side length
    t.left(120)         # Turn 120 degrees (external angle)


# Keep the window open until clicked
turtle.done()
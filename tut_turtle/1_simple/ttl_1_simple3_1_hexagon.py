import turtle

# A hexagon

#STEP1:  A hexagon without for loop

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")  # Set background color to black
screen.setup(800, 600)   # Set screen size to 800x600 pixels

# Set up the turtle
t = turtle.Turtle()
t.pencolor("green")      # Set pen color to green

# Draw a regular hexagon
side_length = 100        # Length of each side

t.forward(side_length)   # Move forward by side length
t.left(60)               # Turn 60 degrees (external angle)

t.forward(side_length)   # Move forward by side length
t.left(60)               # Turn 60 degrees (external angle)

t.forward(side_length)   # Move forward by side length
t.left(60)               # Turn 60 degrees (external angle)

t.forward(side_length)   # Move forward by side length
t.left(60)               # Turn 60 degrees (external angle)

t.forward(side_length)   # Move forward by side length
t.left(60)               # Turn 60 degrees (external angle)

t.forward(side_length)   # Move forward by side length
t.left(60)               # Turn 60 degrees (external angle)

# Keep the window open until clicked
turtle.done()

#############################################
#STEP2:  A hexagon with for loop

# # Set up the screen
# screen = turtle.Screen()
# screen.bgcolor("black")  # Set background color to black
# screen.setup(800, 600)   # Set screen size to 800x600 pixels

# # Set up the turtle
# t = turtle.Turtle()
# t.pencolor("green")      # Set pen color to green

# # Draw a regular hexagon
# side_length = 100        # Length of each side
# for i in range(6):       # Six sides
#     t.forward(side_length)   # Move forward by side length
#     t.left(60)               # Turn 60 degrees (external angle)

# # Keep the window open until clicked
# turtle.done()

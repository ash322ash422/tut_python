import turtle

# Here we will draw a spiral

# STEP1: A static circle

# # Set up the turtle
# t = turtle.Turtle()
# t.speed(1)  # Set drawing speed (1 is slowest, 10 is fastest)

# # Draw a circle with radius 50
# t.circle(50)

# # Keep the window open until clicked
# turtle.done()

#####################################

# STEP2: A circle with static radius. This is same as above.

# # Set up the turtle
# t = turtle.Turtle()
# t.speed(10)  # Faster speed for smoother drawing

# for i in range(360):  # One full rotation (360 degrees)
#     t.forward(1)      # Move forward a small step
#     t.left(1)         # Turn 1 degree
#     t.forward(1) # Slightly increase the radius effect

# # Keep the window open until clicked
# turtle.done()

#####################################

# STEP3: A circle with increasing radius.

# # Set up the turtle
# t = turtle.Turtle()
# t.speed(10)  # Faster speed for smoother drawing

# for i in range(360):  # One full rotation (360 degrees)
#     t.forward(1)      # Move forward a small step
#     t.left(1)         # Turn 1 degree
#     t.forward(i/200)  # Slightly increase the radius effect

# # Keep the window open until clicked
# turtle.done()

#####################################

# STEP4: a spiral

# # Set up the turtle
# t = turtle.Turtle()
# t.speed(10)  # Faster speed for smoother drawing

# # Draw one spiral with three rounds
# for i in range(1080):  # Three full rotations (3 * 360 degrees)
#     t.forward(1)       # Move forward a small step
#     t.left(1)          # Turn 1 degree
#     t.forward(i/200)   # Slightly increase the radius effect

# # Keep the window open until clicked
# turtle.done()


#########################################

# STEP5: a spiral that stays on screen, different background color

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")  # Set background color to black
screen.setup(800, 600)   # Set screen size to 800x600 pixels

# Set up the turtle
t = turtle.Turtle()
t.speed(0)              # Fastest speed for drawing
t.pencolor("green")     # Set pen color to green

# Draw one spiral with three rounds
for i in range(1080):   # Three full rotations (3 * 360 degrees)
    t.forward(1)        # Move forward a small step
    t.left(1)           # Turn 1 degree
    t.forward(i/400)    # Smaller radius increment to keep spiral on screen

# Keep the window open until clicked
turtle.done()
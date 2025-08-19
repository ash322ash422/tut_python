import turtle

# A hexagon
# Here I show how to generalize a formula: triangle -> square -> pentagon -> hexagon -> septagon -> octagon...

# #STEP1:  A triangle without for loop

# # Set up the screen
# screen = turtle.Screen()
# screen.bgcolor("black")  # Set background color to black
# screen.setup(800, 600)   # Set screen size to 800x600 pixels

# # Set up the turtle
# t = turtle.Turtle()
# t.pencolor("green")      # Set pen color to green

# # Draw a triangle. 
# # 1) A triangle has num_of_sides = 3
# # 2) Here each left angle is 360/3 = 120 or 360/num_of_sides

# t.forward(100)   # Move forward by side length
# t.left(120)              # turn left by angle 

# t.forward(100)   # Move forward by side length
# t.left(120)              # turn left by angle  

# t.forward(100)   # Move forward by side length
# t.left(120)              # turn left by angle  
               
# # Keep the window open until clicked
# turtle.done()

#############################################

# # STEP2: Now lets put 100 and 120 into a variable and use that variable. Also increase the pensize
# # Set up the screen
# screen = turtle.Screen()
# screen.bgcolor("black")  # Set background color to black
# screen.setup(800, 600)   # Set screen size to 800x600 pixels

# # Set up the turtle
# t = turtle.Turtle()
# t.pencolor("green")      # Set pen color to green
# t.pensize(4)

# # Draw a triangle. 
# # 1) A triangle has num_of_sides = 3
# # 2) Here each left angle is 360/3 = 120 or 360/num_of_sides

# length = 100       # Length of each side
# left_angle = 120   # left angle

# t.forward(length)   # Move forward by side length
# t.left(left_angle)              # turn left by angle 

# t.forward(length)   # Move forward by side length
# t.left(left_angle)              # turn left by angle  

# t.forward(length)   # Move forward by side length
# t.left(left_angle)              # turn left by angle  
               
# # Keep the window open until clicked
# turtle.done()

####################################################

# STEP3: Now lets dynamically calculate left_angle from num_of_sides of figure. 
# # Set up the screen
# screen = turtle.Screen()
# screen.bgcolor("black")  # Set background color to black
# screen.setup(800, 600)   # Set screen size to 800x600 pixels

# # Set up the turtle
# t = turtle.Turtle()
# t.pencolor("green")      # Set pen color to green
# t.pensize(4)

# # Draw a triangle. 
# # 1) A triangle has num_of_sides = 3
# # 2) Here each left angle is 360/3 = 120 or 360/num_of_sides

# num_of_sides = 3
# length = 100       # Length of each side
# left_angle = 360/num_of_sides   # left angle

# t.forward(length)   # Move forward by side length
# t.left(left_angle)              # turn left by angle 

# t.forward(length)   # Move forward by side length
# t.left(left_angle)              # turn left by angle  

# t.forward(length)   # Move forward by side length
# t.left(left_angle)              # turn left by angle  
               
# # Keep the window open until clicked
# turtle.done()

##########################################

# STEP4: Now put this in for loop
# # Set up the screen
# screen = turtle.Screen()
# screen.bgcolor("black")  # Set background color to black
# screen.setup(800, 600)   # Set screen size to 800x600 pixels

# # Set up the turtle
# t = turtle.Turtle()
# t.pencolor("green")      # Set pen color to green
# t.pensize(4)

# # Draw a triangle. 
# # 1) A triangle has num_of_sides = 3
# # 2) Here each left angle is 360/3 = 120 or 360/num_of_sides

# num_of_sides = 3
# length = 100       # Length of each side
# left_angle = 360/num_of_sides   # left angle

# for i in range(num_of_sides):
#     t.forward(length)   # Move forward by side length
#     t.left(left_angle)              # turn left by angle 
               
# # Keep the window open until clicked
# turtle.done()

###################################################

# STEP5: Now change the num_of_sides to 4,5,6,7
# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")  # Set background color to black
screen.setup(800, 600)   # Set screen size to 800x600 pixels

# Set up the turtle
t = turtle.Turtle()
t.pencolor("green")      # Set pen color to green
t.pensize(4)

# Draw a triangle. 
# 1) A triangle has num_of_sides = 3
# 2) Here each left angle is 360/3 = 120 or 360/num_of_sides

num_of_sides = 8
length = 100       # Length of each side
left_angle = 360/num_of_sides   # left angle

for i in range(num_of_sides):
    t.forward(length)   # Move forward by side length
    t.left(left_angle)              # turn left by angle 
               
# Keep the window open until clicked
turtle.done()



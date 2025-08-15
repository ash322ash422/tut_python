import turtle

# Create the screen
screen = turtle.Screen()
screen.bgcolor("black")
speed = 0

# Create two turtles
red_turtle = turtle.Turtle()
red_turtle.color("red")
red_turtle.speed(speed)
red_turtle.pensize(2)

blue_turtle = turtle.Turtle()
blue_turtle.color("blue")
blue_turtle.speed(speed)
blue_turtle.pensize(2)

# Move turtles to starting positions
red_turtle.penup()
red_turtle.goto(-100, 0)
red_turtle.pendown()

blue_turtle.penup()
blue_turtle.goto(100, 0)
blue_turtle.pendown()

# Draw overlapping circles with both turtles
for i in range(36):
    red_turtle.circle(50)
    red_turtle.left(10)
    blue_turtle.circle(50)
    blue_turtle.right(10)

# Keep the window open
turtle.done()

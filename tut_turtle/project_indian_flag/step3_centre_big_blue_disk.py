import turtle
from turtle import*

#screen for output
screen = turtle.Screen()

# Defining a turtle Instance
t = turtle.Turtle()
speed(0)

# initially penup()
t.penup()
t.goto(-400, 250)
t.pendown()

###############################################

# STEP1: Orange Rectangle 
#white rectangle
t.color("orange")

t.begin_fill()
t.forward(800)
t.right(90)
t.forward(167)
t.right(90)
t.forward(800)
t.end_fill()

t.left(90)
t.forward(167)

###############################################


# STEP2: Green Rectangle
t.color("green")
t.begin_fill()
t.forward(167)
t.left(90)
t.forward(800)
t.left(90)
t.forward(167)
t.end_fill()

###############################################

# STEP3: Center Big Blue Circle 

t.penup()
t.goto(70, 0)
t.pendown()
t.color("navy")
t.begin_fill()
t.circle(70)
t.end_fill()


#to hold the 
#output window
turtle.done()
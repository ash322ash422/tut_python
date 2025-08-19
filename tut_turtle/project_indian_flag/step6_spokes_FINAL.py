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

################################################

# STEP4: Big White Circle inside blue circle
t.penup()
t.goto(60, 0)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(60)
t.end_fill()

################################################
# STEP5: Small Blue Circle
t.penup()
t.goto(20, 0)
t.pendown()
t.color("navy")
t.begin_fill()
t.circle(20)
t.end_fill()

###################################################
# STEP6: Spokes: We want 360/15 = 24 spokes. S
t.penup()
t.goto(0, 0)
t.pendown()
t.pensize(2)
for i in range(24): # 24 = 360/15
    t.forward(60)
    t.backward(60)
    t.left(15) # left by 15 degrees


#to hold the 
#output window
turtle.done()
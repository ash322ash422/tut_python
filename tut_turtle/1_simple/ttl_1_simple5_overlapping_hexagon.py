import turtle
t = turtle.Turtle()
t.speed(1)
turtle.bgcolor("black")  # Set background color
t.pencolor("green")  # Set pen color 


for i in range(6):
    for j in range(6):
        t.forward(60)
        t.left(60)
    t.right(60)
turtle.done()

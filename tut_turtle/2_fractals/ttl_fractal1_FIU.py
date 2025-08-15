import turtle


def koch_fractal(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        koch_fractal(t, order-1, size/3)
        t.left(60)
        koch_fractal(t, order-1, size/3)
        t.right(120)
        koch_fractal(t, order-1, size/3)
        t.left(60)
        koch_fractal(t, order-1, size/3)

# Set up the turtle and screen
t = turtle.Turtle()
t.speed(0)         
turtle.bgcolor("white")
t.pencolor("blue")

t.penup()
t.goto(-150, 90)
t.pendown()

# Draw three sides of the snowflake
for i in range(3):
    koch_fractal(t, 3, 300)  # change order for more/less detail
    t.right(120)

turtle.done()

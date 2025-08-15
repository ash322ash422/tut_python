import turtle

# A star polygon: requires math knowledge to figure out the 144 degrees angle for side of length = 100

# step1: without for loop

# t = turtle.Turtle()
# t.speed(1)

# length = 100
# angle = 144


# t.forward(length)
# t.right(angle)

# t.forward(length)
# t.right(angle)

# t.forward(length)
# t.right(angle)

# t.forward(length)
# t.right(angle)

# t.forward(length)
# t.right(angle)

# turtle.done()

###############################

# step2: with for loop

t = turtle.Turtle()
t.speed(1)

length = 100
angle = 144

for i in range(5):
    t.forward(length)
    t.right(angle)
turtle.done()

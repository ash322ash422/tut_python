import turtle

# Spiral Square Pattern

# STEP1: without for loop
t = turtle.Turtle()
t.speed(1)


t.forward(0)
t.left(90)

t.forward(10)
t.left(90)

t.forward(20)
t.left(90)

t.forward(30)
t.left(90)

t.forward(40)
t.left(90)

t.forward(50)
t.left(90)

t.forward(60)
t.left(90)

t.forward(70)
t.left(90)

t.forward(80)
t.left(90)


turtle.done()


#########################################

# # STEP2: with for loop
# t = turtle.Turtle()
# t.speed(1)


# for i in range(50):
#     t.forward(i * 10)
#     t.left(90)
# turtle.done()

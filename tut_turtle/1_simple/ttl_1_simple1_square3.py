import turtle

# STEP1: Lets draw following figure: forward and then left. Keep increasing the forward distance
# t = turtle.Turtle()
# turtle.bgcolor("black")
# t.speed(20)              
# t.pencolor("green") 

# t.forward(5)
# t.left(95)

# t.forward(10)
# t.left(95)

# t.forward(15)
# t.left(95)

# t.forward(20)
# t.left(95)

# t.forward(25)
# t.left(95)

# t.forward(30)
# t.left(95)

# t.forward(35)
# t.left(95)


# # Keep the window open until clicked
# turtle.done()

#########################################

# # STEP2: Now lets use for loop
# t = turtle.Turtle()
# turtle.bgcolor("black")
# t.speed(20)              
# t.pencolor("green") 

# for i in range(5,36,5): # i = 5,10,15,..30
#     t.forward(i)
#     t.left(95)

# # Keep the window open until clicked
# turtle.done()

#########################################

# # STEP3: Now lets increase the number of iteration in for loop
# t = turtle.Turtle()
# turtle.bgcolor("black")
# t.speed(20)              
# t.pencolor("green") 

# for i in range(5,401,5): # changed iteration to higher number
#     t.forward(i)
#     t.left(95)

# # Keep the window open until clicked
# turtle.done()

#########################################

# # STEP4: Now lets change the parameters of iteration in for loop
# t = turtle.Turtle()
# turtle.bgcolor("black")
# t.speed(20)              
# t.pencolor("green") 

# for i in range(0,401,1): # changed: i=0,1,2,3,...400 
#     t.forward(i)
#     t.left(95)

# # Keep the window open until clicked
# turtle.done()

#########################################

# # STEP5: Now lets change the left angle to 85,100
# t = turtle.Turtle()
# turtle.bgcolor("black")
# t.speed(20)              
# t.pencolor("green") 

# for i in range(0,401,1): 
#     t.forward(i)
#     t.left(85) # change this to 75,80,85,100,110

# # Keep the window open until clicked
# turtle.done()


#########################################
# STEP Final: Now change the left angle to 91
t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(20)              
t.pencolor("green") 

for i in range(0,401,1):
    t.forward(i)
    t.left(91)    # changed to 91


# Keep the window open until clicked
turtle.done()
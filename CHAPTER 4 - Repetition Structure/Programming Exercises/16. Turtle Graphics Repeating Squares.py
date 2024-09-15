"""
In this chapter, you saw an example of a loop that draws a square. Write a turtle graphics pro-
gram that uses nested loops to draw 100 squares, to create the design shown in Figure 4-13.
"""
import turtle
turtle.hideturtle()

a = 5
b = 0

# https://stackoverflow.com/questions/32804572/how-to-hide-a-turtle-icon-pointer-in-python
myTurtle = turtle.Turtle(visible=False) #    turtle.hideturtle()
turtle.speed(0)

def mysquare(edge):
    turtle.penup()
    turtle.goto(200, -200)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)

for i in range(0, 100):
    a = b + 5
    print(a)
    mysquare(a)
    i = i + 1
    b = a 
    

turtle.mainloop()
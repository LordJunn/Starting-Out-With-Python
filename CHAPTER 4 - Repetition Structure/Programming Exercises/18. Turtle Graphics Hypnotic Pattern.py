"""
Use a loop with the turtle graphics library to draw the design shown in Figure 4-15
"""

import turtle
move = 5
turtle.setheading(90)
for x in range(15):
    for x in range(4):
        turtle.forward (move)
        turtle.left(90)
        move += 5


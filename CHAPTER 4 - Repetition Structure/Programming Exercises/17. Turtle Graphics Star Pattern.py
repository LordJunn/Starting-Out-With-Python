"""
Use a loop with the turtle graphics library to draw the design shown in Figure 4-14.
""" #https://www.chegg.com/homework-help/questions-and-answers/17-turtle-graphics-star-pattern-use-loop-turtle-graphics-library-draw-design-shown-figure--q26738583
import turtle
turtle.hideturtle()
turtle.speed(100)

l = 100

for j in range(500): # purely to play like osu
    for i in range(8):
        turtle.forward(l)
        turtle.right(45 + 180)
        l += 3

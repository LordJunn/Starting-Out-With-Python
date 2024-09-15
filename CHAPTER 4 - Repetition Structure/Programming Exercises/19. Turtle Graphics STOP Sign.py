"""
In this chapter, you saw an example of a loop that draws an octagon. Write a program that
uses the loop to draw an octagon with the word “STOP” displayed in its center. The STOP
sign should be centered in the graphics window.
""" #https://www.chegg.com/homework-help/questions-and-answers/17-turtle-graphics-star-pattern-use-loop-turtle-graphics-library-draw-design-shown-figure--q26738583
import turtle
turtle.hideturtle()
turtle.speed(1)

l = 100

for i in range(8):
    turtle.forward(l)
    turtle.right(45)

turtle.penup()
turtle.forward(l/2)
turtle.right(90)
turtle.forward((l*3)/2)
turtle.right(90)
turtle.forward((l*1)/3)
turtle.write("STOP", font = ('Times New Roman', 30, 'normal'))
"""
Write a function named triangle that uses the turtle graphics library to draw a triangle.
The functions should take arguments for the X and Y coordinates of the triangle’s verti-
ces, and the color with which the triangle should be filled. Demonstrate the function in a
program. 
""" 
import turtle

def main():
    x1 = int(input("What's the coordinates for x1? "))
    y1 = int(input("What's the coordinates for y1? "))    
    x2 = int(input("What's the coordinates for x2? "))
    y2 = int(input("What's the coordinates for y2? "))  
    x3 = int(input("What's the coordinates for x3? "))
    y3 = int(input("What's the coordinates for y3? "))  
    colour = input("What's the colour you want for your triangle? ")

    triangle(x1, y1, x2, y2, x3, y3, colour) # (0, 0, 60, 90, 120, 0, "blue")


def triangle(x1, y1, x2, y2, x3, y3, colour): # https://www.youtube.com/watch?v=MvCQWD4c1lQ
    turtle.speed(1)
    turtle.fillcolor(colour)
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()    
    turtle.goto(x2, y2)
    turtle.goto(x3, y3)
    turtle.goto(x1, y1)    
    turtle.end_fill()
    input()
    
main()
    

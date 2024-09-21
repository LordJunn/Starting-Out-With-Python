"""
Write a turtle graphics program that draws a city skyline similar to the one shown in Figure
5-33. The program’s overall task is to draw an outline of some city buildings against a
night sky. Modularize the program by writing functions that perform the following tasks:
• Draw the outline of buildings.
• Draw some windows on the buildings.
• Use randomly placed dots as the stars (make sure the stars appear on the sky, not on the
buildings). 
""" # https://youtu.be/QGrW7pkt0LY?si=hjjK6VCKKnEtUOai
# black sky, ~7 white stars, grey buildings, white windows
import turtle
import random

def main():
    turtle.speed(10)
    turtle.setup(500, 500)
    sky = input('What is the colour of the sky? ')
    turtle.bgcolor(sky)
    bintang = input('What are the colours of the stars? ')
    bilangan = int(input('How many stars are there? '))
    stars(bintang, bilangan)
    bangunan = input('What colour is the building? ')
    buildings(bangunan)
    tingkap = input('What colours are the windows? ')
    windows(tingkap)
    input()
    
def stars(colour, amount):
    turtle.fillcolor(colour)
    for x in range(amount):
        xpos = random.randint(-250, 250)
        ypos = random.randint(-50, 250)
        turtle.penup()
        turtle.goto(xpos, ypos)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(3)
        turtle.end_fill()
        
def buildings(colour):
    turtle.penup()
    turtle.goto(-250, -250)
    turtle.fillcolor(colour)
    turtle.begin_fill()
    turtle.setheading(90)
    turtle.forward(100)
    turtle.setheading(0)    
    turtle.forward(100)    
    turtle.setheading(90)
    turtle.forward(80)    
    turtle.setheading(0)    
    turtle.forward(100)     
    turtle.setheading(90)       
    turtle.forward(150)    
    turtle.setheading(0)       
    turtle.forward(100)
    turtle.setheading(270)       
    turtle.forward(170)   
    turtle.setheading(0)       
    turtle.forward(100)       
    turtle.setheading(90)
    turtle.forward(100)    
    turtle.setheading(0)    
    turtle.forward(100)     
    turtle.setheading(270)
    turtle.goto(250, -250)
    turtle.goto(-250, -250)  
    turtle.end_fill()  

def window(x, y):
    turtle.penup()
    turtle.goto(x, y) 
    turtle.pendown()
    turtle.begin_fill()   
    turtle.setheading(0)
    
    for x in range(4):
        turtle.forward(10)
        turtle.right(90)
        
    turtle.end_fill()
    
def windows(colour):
    turtle.fillcolor(colour)

    window(-140, -80)
    window(-40, 60) 
    window(-40, 40) 
    window(160, 0) 
            
main()
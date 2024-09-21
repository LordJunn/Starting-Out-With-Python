"""
In a program, write a function named drawPattern that uses the turtle graphics library
to draw the rectangular pattern shown in Figure 5-31. The drawPattern function should
accept two arguments: one that specifies the pattern’s width, and another that specifies the
pattern’s height. (The example shown in Figure 5-31 shows how the pattern would appear
when the width and the height are the same.) When the program runs, the program should
ask the user for the width and height of the pattern, then pass these values as arguments to
the drawPattern function
""" # https://youtu.be/izX9It2-JJ8?si=g5LAl797ZDm1L9I8
import turtle

x = 200
y = 200

def main():
    w = int(input('Enter the width of the pattern: '))
    h = int(input('Enter the height of the pattern: '))
    drawPattern(w, h)
    input()

def drawPattern(w, h):
    square(x, y, w, h)
    square((x-30), (y-30), (w-60), (h-60)) 
    
    turtle.begin_fill()             
    square((x-60), (y-60), (w-120), (h-120))      
    turtle.end_fill()  
    
    line((x-w/2), y, h, 270)
    line(x, (y-h/2), h, 180)
    dagline(x, y, x-w, y-h)
    dagline((x-w), y, x, (y-h))
    
def square(x, y, w, h):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(180)
    for count in range(2):
        turtle.forward(w)
        turtle.left(90)
        turtle.forward(h)
        turtle.left(90)         

def line(x, y, h, heading):          
    turtle.penup()        
    turtle.goto(x, y)
    turtle.pendown() 
    turtle.setheading(heading)    
    turtle.forward(h)     
   
def dagline(x, y, a, b):          
    turtle.penup()        
    turtle.goto(x, y)
    turtle.pendown()    
    turtle.goto(a, b)       
   
main()    
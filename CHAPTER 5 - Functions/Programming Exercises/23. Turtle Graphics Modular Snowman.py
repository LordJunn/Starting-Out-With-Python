"""
Write a program that uses turtle graphics to display a snowman, similar to the one shown
in Figure 5-30. In addition to a main function, the program should also have the following
functions:
• drawBase. This function should draw the base of the snowman, which is the large snow-
ball at the bottom.
• drawMidSection. This function should draw the middle snowball.
• drawArms. This function should draw the snowman’s arms.
• drawHead. This function should draw the snowman’s head, with eyes, mouth, and other
facial features you desire.
• drawHat. This function should draw the snowman’s hat.
""" # https://www.youtube.com/watch?v=qkgrb9CNweo
import turtle

def main(): # illusion of free choice
    x1 = int(input("What's the x coordinates for the base? "))
    y1 = int(input("What's the y coordinates for the base? "))
    s1 = int(input("What's the size for the base? "))     
    drawBase(x1, y1, s1)
    
    x2 = int(input("What's the x coordinates for the midsection? "))
    y2 = int(input("What's the y coordinates for the midsection? "))
    s2 = int(input("What's the size for the midsection? "))     
    drawMidSection(x2, y2, s2)    
    
    drawArms()
    
    x3 = int(input("What's the x coordinates for the head? "))
    y3 = int(input("What's the y coordinates for the head? "))
    s3 = int(input("What's the size for the head? "))     
    drawHead(x3, y3, s3)
    
    warna = input("What is the colour of the hat? ")
    drawHat(warna)
    
    input()
    
    
def drawBase(x1, y1, size): # 0, -200, 70
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.circle(size)
    turtle.penup()
    
def drawMidSection(x1, y1, size): # 0, -60, 50
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.circle(size) 
    turtle.penup()   
    
def drawArms():
    def rightArm():
        turtle.penup()
        turtle.goto(50, -10)
        turtle.pendown()
        turtle.setheading(35)
        turtle.forward(70)
        turtle.setheading(0)        
        turtle.forward(10)
        turtle.backward(10)        
        turtle.setheading(75)        
        turtle.forward(10)   
        
    def leftArm():
        turtle.penup()
        turtle.goto(-50, 10)
        turtle.pendown()
        turtle.setheading(170)
        turtle.forward(50)
        turtle.setheading(90)        
        turtle.forward(10)
        turtle.backward(10)        
        turtle.setheading(170)        
        turtle.forward(10)
        
    rightArm()
    leftArm()
        
def drawHead(x1, y1, size): # 0, 90, 25
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.circle(size)   
    turtle.penup()
    turtle.goto(-10, 60)
    turtle.pendown()
    turtle.penup()
    turtle.goto(-5, 70)
    turtle.pendown()
    turtle.circle(3)
    turtle.penup()
    turtle.goto(5, 70)
    turtle.pendown()         
    turtle.circle(3)        
        
def drawHat(colour):
    turtle.penup() # layer 1
    turtle.goto(-50, 85)    
    turtle.pendown()
    turtle.fillcolor(colour)
    turtle.begin_fill()
    turtle.goto(50, 85)     
    turtle.setheading(90)
    turtle.forward(20)
    turtle.setheading(180)                
    turtle.forward(100)        
    turtle.setheading(270)           
    turtle.forward(20)
    turtle.end_fill()
    turtle.penup()
    
    turtle.goto(-20, 105)
    turtle.fillcolor(colour)
    turtle.begin_fill()  
    turtle.pendown()
    turtle.goto(20, 105)
    turtle.setheading(90)
    turtle.forward(30)
    turtle.setheading(180)                
    turtle.forward(40)        
    turtle.setheading(270)           
    turtle.forward(30)
    turtle.end_fill()
    turtle.penup()    
    
main()
    
    
     
        
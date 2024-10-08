# https://www.chegg.com/homework-help/questions-and-answers/15-turtle-graphics-drawings-use-turtle-graphics-library-write-programs-reproduce-designs-s-q26567428
from turtle import *

def mydesign1():
    d = Pen()
    d.screen.bgcolor("cyan")
    d.color("black")
    d.right(-45)
    d.forward(200)
    d.right(90)
    d.forward(100)
    d.right(90)
    d.forward(100)
    d.right(90)
    d.forward(200)
    d.right(-90)
    d.forward(100)
    d.right(-90)
    d.forward(100)
    
def mydesign2():
    d = Pen()
    d.screen.bgcolor("cyan")
    d.color("black")
    d.forward(150)
    d.left(120)
    d.forward(150)
    d.left(120)
    d.forward(150)
    d.left(150)
    d.forward(90)
    d.right(60)
    d.forward(90)

def mydesign3():
    d = Pen()
    d.screen.bgcolor("cyan")
    d.color("black")
    for i in range(4):
        d.forward(50)
        d.left(90)
    d.penup()
    d.setposition(-100,100)
    d.pendown()
    for i in range(4):
        d.forward(50)
        d.left(90)
    d.left(45)
    d.setposition(0,0)
    d.penup()
    d.left(45)
    d.setposition(50,0)
    d.pendown()
    d.setposition(-50,100)
    d.penup()
    d.left(45)
    d.setposition(-50,150)
    d.pendown()
    d.setposition(50,50)
    d.penup()
    d.left(45)
    d.setposition(0,50)
    d.pendown()
    d.setposition(-100,150)

def mydesign4():
    d = Pen()
    d.screen.bgcolor("cyan")
    d.color("black")
    d.circle(30)
    d.penup()
    d.setposition(200,0)
    d.pendown()
    d.penup()
    d.setposition(80,0)
    d.pendown()
    d.circle(30)
    d.penup()
    d.setposition(160,0)
    d.pendown()
    d.circle(30)
    d.penup()
    d.setposition(40,-30)
    d.pendown()
    d.circle(30)
    d.penup()
    d.setposition(120,-30)
    d.pendown()
    d.circle(30)

def mydesign5():
    d = Pen()
    d.screen.bgcolor("cyan")
    d.color("black")
    d.setposition(0,0)
    d.write("North")    
    d.right(90)
    d.forward(100)
    d.penup()
    d.forward(15)
    d.write("South")
    d.setposition(-50,-50)
    d.write("West")
    d.left(90)
    d.pendown()
    d.forward(100)
    d.write("East")
    d.penup()
    d.setposition(0,-60)
    d.pendown()
    d.circle(10)
    
def mydesign6():
    d = Pen()
    d.screen.bgcolor("cyan")
    d.color("black")
    d.dot(5,"black")
    d.right(90)
    d.forward(150)
    d.dot(5,"black")
    d.left(135)
    d.forward(210)
    d.dot(5,"black")
    d.right(135)
    d.dot(5,"black")
    d.forward(150)
    d.dot(5,"black")
    d.setposition(0,0)
    d.left(90)
    for i in range(15):
        d.forward(5)
        d.penup()
        d.forward(5)
        d.pendown()
    d.penup()
    d.setposition(0,-150)
    for i in range(15):
        d.forward(5)
        d.penup()
        d.forward(5)
        d.pendown()
        
mydesign1()
mydesign2()
mydesign3()
mydesign4()
mydesign5()
mydesign6()
# Keep the window open. (Not necessary with IDLE.)

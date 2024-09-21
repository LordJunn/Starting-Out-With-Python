"""
Write a turtle graphics program that uses the square function presented in this chapter,
along with a loop (or loops) to draw the checkerboard pattern shown in Figure petak-32.
""" # https://youtu.be/wI3XStE1T4s?si=GnUFO4SjkSGr9UB- 
# to do wat was intended: 500 wide, 5 petak, black colour
import turtle 

def main():
    turtle.speed(0)
    a = int(input('How wide do you want the screen to be? ')) 
    turtle.setup(a, a)
    petak = int(input('How many squares would you like per row/column? '))
    turtle.penup()
    colour = input('How colour do you want the boards to be? ')
    turtle.fillcolor(colour)
    x = 0 - (a/2)
    y = a/2

    if(petak % 2 == 0):
        for mainloop in range(petak//2):
            hitamStarter(x, y, a, petak)
            y -= a/petak
            putihStarter(x, y, a, petak)
            y -= a/petak
            
    else:
        for mainloop in range(petak//2):
            hitamStarter(x, y, a, petak)
            y -= a/petak
            putihStarter(x, y, a, petak)
            y -= a/petak
        hitamStarter(x, y, a, petak)    
        
    input()

def hitam(a, petak):
    turtle.begin_fill()
    for x in range(4):
        turtle.forward(a/petak)
        turtle.right(90)
    turtle.end_fill()

def putih(a, petak):
    for x in range(4):
        turtle.forward(a/petak)
        turtle.right(90)    

def hitamStarter(x, y, a, petak):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
    if(petak % 2 == 0):
        for starterloop in range(petak//2):
            hitam(a, petak)
            x += a/petak
            turtle.goto(x, y)
            putih(a, petak)
            x += a/petak
            turtle.goto(x, y) 
            
    else:
        for starterloop in range(petak//2):
            hitam(a, petak)
            x += a/petak
            turtle.goto(x, y)
            putih(a, petak)
            x += a/petak
            turtle.goto(x, y) 
        hitam(a, petak)        
        
def putihStarter(x, y, a, petak):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    if(petak % 2 == 0):
        for starterloop in range(petak//2):
            putih(a, petak)
            x += a/petak
            turtle.goto(x, y)
            hitam(a, petak)
            x += a/petak
            turtle.goto(x, y)
            
    else:
        for starterloop in range(petak//2):
            putih(a, petak)
            x += a/petak
            turtle.goto(x, y)
            hitam(a, petak)
            x += a/petak
            turtle.goto(x, y)        
        putih(a, petak)

main()
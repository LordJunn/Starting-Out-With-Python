"""
Write a program that simulates a Magic 8 Ball, which is a fortune-telling toy that displays a
random response to a yes or no question. In the student sample programs for this book, you
will find a text file named 8_ball_responses.txt. The file contains 12 responses, such
as “I don’t think so”, “Yes, of course!”, “I’m not sure”, and so forth. The program should
read the responses from the file into a list. It should prompt the user to ask a question, then
display one of the responses, randomly selected from the list. The program should repeat
until the user is ready to quit.
"""
import random 

def main():
    repeat = 'y'
    while (repeat != 'quit'):
        w = input('Enter a question: ')
        ball = fileOpenIndexConvertStr('8_ball_responses.txt')
        rng = random.randint(1, 12)
        print(ball[rng - 1])
        repeat = input('To quit, enter quit. Anything else to continue. ')

def fileOpenIndexConvertStr(fileName): # opens a file, converts item in it into string
    infile = open(fileName, 'r')
    acc = infile.readlines()
    infile.close()
    
    index = 0
    while index < len(acc):
        acc[index] = str(acc[index].strip()) # strip is necessary
        index += 1  
        
    return acc  

main()
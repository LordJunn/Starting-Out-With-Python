"""
In the student sample programs for this book, you will find a text file named 1994_Weekly_
Gas_Averages.txt. The file contains the average gas price for each week in the year 1994.
(There are 52 lines in the file.) Using matplotlib, write a Python program that reads the
contents of the file then plots the data as either a line graph or a bar chart. Be sure to display
meaningful labels along the X and Y axes, as well as the tick marks.
""" # this doesnt work on my machine
import matplotlib.pyplot as plt

def main():
    gas = fileOpenIndexConvertFloat('1994_Weekly_Gas_Averages.txt')
    choice = input('Line graph or a bar chart? ')
    
    plt.title('1994 Weekly Gas Averages')
    plt.xlabel('Week')
    plt.ylabel('Price') 
    
    plt.xlim(xmin = 0, xmax = 52) 
    plt.ylim(ymin = 0.9, ymax = 1.2) # range of 0.9 to 1.2 to see, since thats the range
    
    if choice == '1':
        xc = list(range(1, 53))
        yc = gas
        plt.plot(xc, yc) # x coord, y coord

    else:
        width = 1
        edges = list(range(1, 53)) # edge = x
        heights = gas # height = y
        plt.bar(edges, heights, width, color=('r', 'g', 'b', 'k')) # changable colours
        
    plt.show()       

def fileOpenIndexConvertFloat(fileName): # opens a file, converts item in it into int, gpt ver
    with open(fileName, 'r') as infile:
        lines = infile.readlines()
    
    acc = [float(line.strip()) for line in lines] # think of it as for line in lines, do the thing
    
    return acc


main()
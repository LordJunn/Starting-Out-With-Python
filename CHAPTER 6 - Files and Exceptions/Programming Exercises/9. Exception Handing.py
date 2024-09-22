"""
Modify the program that you wrote for Exercise 6 so it handles the following exceptions:
• It should handle any IOError exceptions that are raised when the file is opened and data
is read from it.
• It should handle any ValueError exceptions that are raised when the items that are read
from the file are converted to a number.
"""

def main():
    nama = input('Name of a file to read? ')
    try:
        count = lineReadCounter(nama)
        total = linePrint(nama, count)
        print(f'Average: {total}')
    except IOError:
        print(f'An error occurred trying to read {nama}.')    
    except ValueError:
        print('Non-numeric data found in the file.')

def lineReadCounter(name):
    infile = open(name, 'r')
    counter = 0
    while (infile.readline() != ''):
        counter += 1
    infile.close()
    return counter

def linePrint(name, lines):
    total = 0
    infile = open(name, 'r')
    for count in range(lines): 
        total += int(infile.readline())
    infile.close()    
    return total/lines    
    
main()  
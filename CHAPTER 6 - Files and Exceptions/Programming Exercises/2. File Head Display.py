"""
Write a program that asks the user for the name of a file. The program should display only
the first five lines of the file’s contents. If the file contains less than five lines, it should
display the file’s entire contents.
"""

def main():
    nama = input('Name of a file to read? ')
    count = lineReadCounter(nama)
    if (count >= 5):
        linePrint(nama, 5)
    else:
        linePrint(nama, count)        

def lineReadCounter(name):
    infile = open(name, 'r')
    counter = 0
    while (infile.readline() != ''):
        counter += 1
    infile.close()
    return counter

def linePrint(name, lines):
    infile = open(name, 'r')
    for count in range(lines): 
        print(infile.readline()) # this works as opposed to print(contents), refer line 18
    infile.close()        
    
main()
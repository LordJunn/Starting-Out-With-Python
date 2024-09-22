"""
Assume a file containing a series of integers is named numbers.txt and exists on the
computer’s disk. Write a program that calculates the average of all the numbers stored in
the file.
""" # stolen from C6PE5

def main():
    nama = input('Name of a file to read? ')
    count = lineReadCounter(nama)
    total = linePrint(nama, count)
    print(f'Average: {total}')    

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
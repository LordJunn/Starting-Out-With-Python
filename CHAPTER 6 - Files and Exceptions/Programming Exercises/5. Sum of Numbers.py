"""
Assume a file containing a series of integers is named numbers.txt and exists on the com-
puter’s disk. Write a program that reads all of the numbers stored in the file and calculates
their total.
""" 

def main():
    nama = input('Name of a file to read? ')
    count = lineReadCounter(nama)
    total = linePrint(nama, count)
    print(f'Total: {total}')    

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
    return total    
    
main()  
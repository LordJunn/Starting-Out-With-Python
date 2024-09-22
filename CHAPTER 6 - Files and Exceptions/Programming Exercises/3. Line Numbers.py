"""
Write a program that asks the user for the name of a file. The program should display the
contents of the file with each line preceded with a line number followed by a colon. The
line numbering should start at 1.
"""

def main():
    nama = input('Name of a file to read? ')
    count = lineReadCounter(nama)
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
        print(f'{count + 1}: {infile.readline()}' ) # this works as opposed to print(contents), refer line 18
    infile.close()        
    
main()  
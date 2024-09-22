"""
Assume a file containing a series of integers is named numbers.txt and exists on the com-
puter’s disk. Write a program that displays all of the numbers in the file.
"""

def main():
    infile = open('C6PE1.txt', 'r')
    file_contents = infile.read()
    infile.close()
    print(file_contents)

main()
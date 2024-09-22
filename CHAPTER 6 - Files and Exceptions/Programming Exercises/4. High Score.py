"""
Assume that a file named scores.txt exists on the computer’s disk. It contains a series of
records, each with two fields – a name, followed by a score (an integer between 1 and 100).
Write a program that displays the name and score of the record with the highest score, as
well as the number of records in the file. (Hint: Use a variable and an “if” statement to
keep track of the highest score found as you read through the records, and a variable to
keep count of the number of records.)
"""
high = -1

def main():
    nama = input('Name of a file to read? ')
    count = lineReadCounter(nama)
    name, highest = linePrint(nama, count)    
    print(f'Highest score, {highest} belongs to {name}')
    print(f'Total records: {count}')

def highest(score):
    global high
    if(score > high):
        high = score
        return True

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
        C6PE4 = infile.readline()
        name, skor = C6PE4.strip().split()
        owo = int(skor)
        if highest(owo):
            person = name
            tinggi = owo
            print(owo)

    infile.close()  
    return person, tinggi
    
main()  
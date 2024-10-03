"""
If you have downloaded the source code you will find a file named WorldSeriesWinners.
txt in the Chapter 07 folder. This file contains a chronological list of the World Series win-
ning teams from 1903 through 2009. (The first line in the file is the name of the team that
won in 1903, and the last line is the name of the team that won in 2009. Note the World
Series was not played in 1904 or 1994.)
Write a program that lets the user enter the name of a team, then displays the number of
times that team has won the World Series in the time period from 1903 through 2009.

TIP: Read the contents of the WorldSeriesWinners.txt file into a list. When the
user enters the name of a team, the program should step through the list, counting the
number of times the selected team appears.
"""

YEARS = 104

def main():
    winners = fileOpenIndexConvertStr('WorldSeriesWinners.txt')
    counter = 0
    
    search = input('Enter a team to search: ')
    for i in range(YEARS):
        if (search == winners[i]):
            counter += 1
            
    print(f'{search} has won the World Series {counter} times in the time period from 1903 through 2009. ')
    
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
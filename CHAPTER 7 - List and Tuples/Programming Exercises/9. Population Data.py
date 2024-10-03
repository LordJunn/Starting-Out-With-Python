"""
If you have downloaded the source code you will find a file named USPopulation.txt
in the Chapter 07 folder. The file contains the midyear population of the United States, in
thousands, during the years 1950 through 1990. The first line in the file contains the popu-
lation for 1950, the second line contains the population for 1951, and so forth.
Write a program that reads the file’s contents into a list. The program should display the
following data:
• The average annual change in population during the time period
• The year with the greatest increase in population during the time period
• The year with the smallest increase in population during the time period
"""
YEARS = 40

def main():
    pop = fileOpenIndexConvertInt('USPopulation.txt')

    yhigh = float('-inf')
    ylow = float('inf')    
    total = 0
    
    for i in range(YEARS + 1):
        if (i == 0):
            change = pop[1] - pop[0]
            high = change
            low = change
        else:
            change = pop[i] - pop[i - 1]
            print(f'Increase in year {i + 1950}: {change}')
        
            if (change > high):
                yhigh = i
                high = change
            elif (change < low):
                ylow = i
                low = change
                
        total += change
            
    print(f'The average annual change in population during the time period: {total/(YEARS - 1)}')
    print(f'The year with the greatest increase in population during the time period: {yhigh + 1950}, +{high} ')
    print(f'The year with the smallest increase in population during the time period: {ylow + 1950}, +{low} ')        

def fileOpenIndexConvertInt(fileName): # opens a file, converts item in it into int
    infile = open(fileName, 'r')
    acc = infile.readlines()
    infile.close()
    
    index = 0
    while index < len(acc):
        acc[index] = int(acc[index])
        index += 1  
        
    return acc  

main()
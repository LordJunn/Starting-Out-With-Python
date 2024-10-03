"""
If you have downloaded the source code you will find the following files in the Chapter 07
folder:
• GirlNames.txt This file contains a list of the 200 most popular names given to girls
born in the United States from the year 2000 through 2009. 
• BoyNames.txt This file contains a list of the 200 most popular names given to boys
born in the United States from the year 2000 through 2009.
Write a program that reads the contents of the two files into two separate lists. The user
should be able to enter a boy’s name, a girl’s name, or both, and the application will display
messages indicating whether the names were among the most popular.
(You can access the Premium Companion Website at www.pearsonglobaleditions.com/gaddis.)
""" 

def main():
    gals = fileOpenIndexConvertStr('GirlNames.txt')
    bois = fileOpenIndexConvertStr('BoyNames.txt')
    truth = 0
    
    search = input('Enter a name to search: ')
    
    if search in gals:
        print(f'{search} was a popular name given to girls born in the United States from the year 2000 through 2009.')
        truth += 10
    else: 
        truth += 1
               
    if search in bois:
        print(f'{search} was a popular name given to boys born in the United States from the year 2000 through 2009.')
        truth += 10
    else:
        truth += 1

    if (truth == 2):
        print(f'{search} was neither a popular name given to boys nor girls born in the United States from the year 2000 through 2009.')
    elif(truth == 20):
        print(f'{search} was a popular name given to both boys and girls born in the United States from the year 2000 through 2009.')

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
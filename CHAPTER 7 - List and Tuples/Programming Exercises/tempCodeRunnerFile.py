"""
Create a text file that contains your expenses for last month in the following categories:
• Rent
• Gas
• Food
• Clothing
• Car payment
• Misc
Write a Python program that reads the data from the file and uses matplotlib to plot a pie
chart showing how you spend your money.
"""
import matplotlib.pyplot as plt

CATEGORIES = 6

def main():
    file = input('What is the text file that contains your expenses for last month? ')
    fileOpenIndexConvertInt(file)
    expenses = [0] * CATEGORIES
    
    for i in range(CATEGORIES):
        expenses[i] = file[i]
    
    plt.pie(expenses)
    plt.show()
    

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
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
""" # this doesnt work on my machine
import matplotlib.pyplot as plt

CATEGORIES = 6
CATEGORY_NAMES = ['Rent', 'Gas', 'Food', 'Clothing', 'Car payment', 'Misc']

def main():
    file = input('What is the text file that contains your expenses for last month? ')
    expenses = fileOpenIndexConvertInt(file)
    
    choice = input('Would you like to include labels and percentages? Press 1. ')
    if choice == '1':
        plt.pie(expenses, labels=CATEGORY_NAMES, autopct='%1.1f%%')
        plt.show()
    else:
        plt.pie(expenses)
        plt.show()

def fileOpenIndexConvertInt(fileName): # opens a file, converts item in it into int, gpt ver
    with open(fileName, 'r') as infile:
        lines = infile.readlines()
    
    acc = [int(line.strip()) for line in lines]
    
    return acc

main()
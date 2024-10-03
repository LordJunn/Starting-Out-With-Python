"""
If you have downloaded the source code from the Premium Companion Website you will
find a file named charge_accounts.txt in the Chapter 07 folder. This file has a list of a
company’s valid charge account numbers. Each account number is a seven-digit number,
such as 5658845.
Write a program that reads the contents of the file into a list. The program should then
ask the user to enter a charge account number. The program should determine whether
the number is valid by searching for it in the list. If the number is in the list, the program
should display a message indicating the number is valid. If the number is not in the list, the
program should display a message indicating the number is invalid.
(You can access the Premium Companion Website at www.pearsonglobaleditions.com/gaddis.)
""" # charge_accounts.txt stolen from https://www.chegg.com/homework-help/questions-and-answers/need-help-python-problem-5-charge-account-validation-downloaded-source-code-book-s-compani-q14024057

def main():
    account = fileOpenIndexConvertInt('charge_accounts.txt')
    checker = int(input('Enter a charge account number: '))
    if checker in account:
        print('Valid.')
    else:
        print('Invalid.')

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
    
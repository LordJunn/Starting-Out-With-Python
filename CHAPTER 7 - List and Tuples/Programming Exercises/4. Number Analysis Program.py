"""
Design a program that asks the user to enter a series of 20 numbers. The program should
store the numbers in a list then display the following data:
• The lowest number in the list
• The highest number in the list
• The total of the numbers in the list
• The average of the numbers in the list
""" # stolen from C7PE3
 
SERIES = 20

def main():
    total = 0
    number = [0] * SERIES
    
    for i in range(SERIES):
        number[i] = int(input(f'Enter number #{i + 1}: '))
        total += number[i]

    avg = total/SERIES

    high = number[0]
    low = number[0]
    
    for i in range(SERIES):
        if(number[i] > high):
            high = number[i]
        elif(number[i] < low):
            low = number[i]
            
    print(f'The lowest number in the list: {low}')    
    print(f'The highest number in the list: {high}')   
    print(f'The total of the numbers in the list: {total}')
    print(f'The average of the numbers in the list: {avg}') 

main()
"""
Design a program that uses a loop to build a list named valid_numbers that contains only
the numbers between 0 and 100 from the numbers list below. The program should then
determine and display the total and average of the values in the valid_numbers list.
numbers = [74, 19, 105, 20, −2, 67, 77, 124, −45, 38]
"""

def main():
    total = 0
    num = 0
    valid_numbers = []
    numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38] 

    for index in numbers:
        if (0 <= index <= 100):
            valid_numbers.append(index)
            total += index
            num += 1
    
    for index in valid_numbers:
        print(index)
        
    avg = total/num
        
    print(f'Total: {total}, Average: {avg:.3f}')

main()
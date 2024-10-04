"""
Many companies use telephone numbers like 555-GET-FOOD so the number is easier for
their customers to remember. On a standard telephone, the alphabetic letters are mapped to
numbers in the following fashion:
A, B, and C = 2
D, E, and F = 3
G, H, and I = 4
J, K, and L = 5
M, N, and O = 6
P, Q, R, and S = 7
T, U, and V = 8
W, X, Y, and Z = 9
Write a program that asks the user to enter a 10-character telephone number in the for-
mat XXX-XXX-XXXX. The application should display the telephone number with any
alphabetic characters that appeared in the original translated to their numeric equiva-
lent. For example, if the user enters 555-GET-FOOD, the application should display
555-438-3663.
"""

def main():
    number = input('Enter a 10-character telephone number in the format XXX-XXX-XXXX: ')
    if (len(number) != 12 or number[3] != '-' or number[7] != '-'):
        print("Invalid format. Please enter the number in the format XXX-XXX-XXXX.")
        return main()   
    
    numeric = translator(number)
    print(f'{number} would be: {numeric} numerically.')

def charToNum(char):
    if char in 'ABC':
        return '2'
    elif char in 'DEF':
        return '3'
    elif char in 'GHI':
        return '4'
    elif char in 'JKL':
        return '5'
    elif char in 'MNO':
        return '6'
    elif char in 'PQRS':
        return '7'
    elif char in 'TUV':
        return '8'
    elif char in 'WXYZ':
        return '9'
    else:
        return char
    
def translator(target):
    output = []
    for char in target:
        output.append(charToNum(char))
    
    return ''.join(output)

main()
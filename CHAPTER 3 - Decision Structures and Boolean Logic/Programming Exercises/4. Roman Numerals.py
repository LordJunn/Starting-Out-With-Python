"""
Write a program that prompts the user to enter a number within the range of 1 through 10.
The program should display the Roman numeral version of that number. If the number is
outside the range of 1 through 10, the program should display an error message. The fol-
lowing table shows the Roman numerals for the numbers 1 through 10:
Number Roman Numeral
1 I
2 II
3 III
4 IV
5 V
6 VI
7 VII
8 VIII
9 IX
10 X
"""

num = int(input('Enter a number between 1 and 10: '))

if num == 1:
    roman = 'I'
elif num == 2:
    roman = 'II'
elif num == 3:
    roman = 'III'
elif num == 4:
    roman = 'IV'
elif num == 5:
    roman = 'V'
elif num == 6:
    roman = 'VI'
elif num == 7:
    roman = 'VII'
elif num == 8:
    roman = 'VIII'
elif num == 9:
    roman = 'IX'
elif num == 10:
    roman = 'X'
else:
    roman = None

if roman: # gpt cuz imagine typing 10 of them
    print(f'The Roman numeral for {num} is {roman}')
else:
    print('Error: Number must be between 1 and 10.')
"""
The Lo Shu Magic Square is a grid with 3 rows and 3 columns, shown in Figure 7-18. The
Lo Shu Magic Square has the following properties:
• The grid contains the numbers 1 through 9 exactly.
• The sum of each row, each column, and each diagonal all add up to the same number.
This is shown in Figure 7-19.
In a program you can simulate a magic square using a two-dimensional list. Write a func-
tion that accepts a two-dimensional list as an argument and determines whether the list is
a Lo Shu Magic Square. Test the function in a program.
"""
ROWS = 3
COLUMNS = 3

def main():
    lsm = [[0] * COLUMNS for _ in range(ROWS)] # GPT, means 000 (row 1) 000 (row 2) ...
    
    for r in range(ROWS):
        for c in range(COLUMNS):
            lsm[r][c] = checker(1, 9)
            
    if IsItLSM(lsm):
        print('True!')
    else:
        print('False!')
            
            
    print(lsm)

def checker(min, max):
    
    while True:
        try:
            num = int(input(f'Input a number between {min} & {max}: '))
            if (min <= num <= max):
                return num
            else:
                print(f'This is not a number between {min} & {max}. ')
        except ValueError:
            print('Invalid input. Please enter a valid integer.')            

def IsItLSM(square):
    magic = 15 # cuz 1 + 2...8 + 9 = 45 divide 3 = 15
    
    all = []
    for row in square: # [num for row in square for num in row]
        for num in row:
            all.append(num)
            
    print(all)
    
    
    if sorted(all) != list(range(1, 10)): # [1, 2, 3, 4, 5, 6, 7, 8, 9]
        return False
            
    for row in square: # row check
        if sum(row) != magic:
            return False
        
    for col in range(COLUMNS): # col check
        csum = sum(square[r][col] for r in range(ROWS))  # ok idk waddis is its GPT, how is C++ easier
        if csum != magic:
            return False
    
    # Check sums of diagonals, GPT
    if (sum(square[i][i] for i in range(ROWS)) != magic or sum(square[i][ROWS - 1 - i] for i in range(ROWS)) != magic):
        return False    
            
    return True
        
main()
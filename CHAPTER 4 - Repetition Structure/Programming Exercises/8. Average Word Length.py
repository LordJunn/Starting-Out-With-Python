"""
Write a program with a loop that repeatedly asks the user to enter a word. The user should
enter nothing (press Enter without typing anything) to signal the end of the loop. Once the
loop ends, the program should display the average length of the words entered, rounded to
the nearest whole number.
"""

repeat = 'w'
total = 0
counter = 0
avg = 0

while repeat != '':
    repeat = input('Enter a word, or enter nothing to quit: ')
    total += len(repeat) # apparently word.len() or word.length() doesnt exist
    counter += 1
    
if counter <= 1:
    print('No words are entered.')
else:    
    avg = (total)/(counter - 1)
    print(f'Average length of the words entered: {round(avg)}') # instead of {avg:.0f}
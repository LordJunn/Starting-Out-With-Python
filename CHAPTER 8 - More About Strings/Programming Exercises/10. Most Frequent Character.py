"""
Write a program that lets the user enter a string and displays the character that appears most
frequently in the string.
"""

def main():
    string = input('Enter a string: ')
    amount, letter = mode(string)
    print(f'The letter {letter} has appeared most frequently in the string, with a count of {amount}.')
    

def mode(string):
    counts = [0] * 26
    newString = ""
    newString = string.upper()
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'    

    for char in newString:
        if char.isalpha():
            if char in letters:
                index = letters.index(char) #  Find the index of the letter
                counts[index] += 1
                
    count = max(counts) # counts = the [0, 0, 3, 2....]
    freqIndex = counts.index(count)
    freq = letters[freqIndex]
    
    return count, freq
                
main()              
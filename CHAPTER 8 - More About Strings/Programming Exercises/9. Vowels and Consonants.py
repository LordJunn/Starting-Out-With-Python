"""
Write a program with a function that accepts a string as an argument and returns the
number of vowels that the string contains. The application should have another function
that accepts a string as an argument and returns the number of consonants that the string
contains. The application should let the user enter a string, and should display the number
of vowels and the number of consonants it contains.
"""
def main():
    string = input('Enter a string: ')
    vowel = vowels(string)
    consonant = consonants(string)
    print(f'V: {vowel} C: {consonant}')

def vowels(string):
    newString = ""
    count = 0
    
    newString = string.upper()
    
    for char in newString:
        if char.isalpha():
            if char in 'AEIOU':
                count += 1
            
    return count

def consonants(string):
    newString = ""
    count = 0
    
    newString = string.upper()
    
    for char in newString:
        if char.isalpha():
            if char not in 'AEIOU':
                count += 1
            
    return count

main()
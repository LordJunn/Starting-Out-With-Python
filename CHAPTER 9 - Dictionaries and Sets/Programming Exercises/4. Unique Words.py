"""
Write a program that opens a specified text file then displays a list of all the unique words
found in the file.
Hint: Store each word as an element of a set.
"""
import string
def main():

    file = input('Input the name of a text file: ')
    myset = uniques(file)
    if myset is not None: # making sure it isnt empty
        print("Unique words found in the file:")
        for word in sorted(myset):
            print(word)
        
def uniques(file):
    unique = set()
    
    try:
        with open(file, 'r') as file:
            lines = file.readlines()
        
        for words in lines:
            # Creates a translation table for removing characters, # Applies the translation table to the string.
            words = words.translate(str.maketrans('', '', string.punctuation)) # words.lower().translate to make it case-insensitive
            # string.punctuation includes characters like !"#$%&'()*+,-./:;<=>?@[\]^_{|}~`
            word = words.split()
            unique.update(word) # since it wont get repeated

    except FileNotFoundError:
        print(f"The file '{file}' was not found.")
        return None         
    
    return unique
    
main()
    



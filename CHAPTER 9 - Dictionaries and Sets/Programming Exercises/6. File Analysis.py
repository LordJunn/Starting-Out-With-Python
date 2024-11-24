"""
Write a program that reads the contents of two text files and compares them in the fol-
lowing ways:
• It should display a list of all the unique words contained in both files.
• It should display a list of the words that appear in both files.
• It should display a list of the words that appear in the first file but not the second.
• It should display a list of the words that appear in the second file but not the first.
• It should display a list of the words that appear in either the first or second file, but not
both.
Hint: Use set operations to perform these analyses.
"""
import string
def main():

    file1 = input('Input the name of a text file: ')
    myset1 = uniques(file1)
            
    file2 = input('Input the name of a text file: ')
    myset2 = uniques(file2)

    myunion = myset1.union(myset2)
    myintersect = myset1.intersection(myset2)
    diff1 = myset1.difference(myset2)
    diff2 = myset2.difference(myset1)
    mysymmetric = myset1.symmetric_difference(myset2)

    if myunion is not None: # making sure it isnt empty
        print("List of all the unique words contained in both files:")
        for word in sorted(myunion):
            print(word)    

    if myintersect is not None: 
        print("\nList of the words that appear in both files:")
        for word in sorted(myintersect):
            print(word)    
            
    if diff1 is not None: 
        print("\nList of the words that appear in the first file but not the second:")
        for word in sorted(diff1):
            print(word)               

    if diff2 is not None: 
        print("\nList of the words that appear in the second file but not the first:")
        for word in sorted(diff2):
            print(word)    
            
    if mysymmetric is not None: 
        print("\nList of the words that appear in either the first or second file, but not both:")
        for word in sorted(mysymmetric):
            print(word)    

        
def uniques(file): # stolen from C9PE6
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
    
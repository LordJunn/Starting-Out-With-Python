"""
Write a program that accepts as input a sentence in which all of the words are run together,
but the first character of each word is uppercase. Convert the sentence to a string in which
the words are separated by spaces, and only the first word starts with an uppercase letter. For
example the string “StopAndSmellTheRoses.” would be converted to “Stop and smell
the roses.”
"""

def main():
    string = input('Enter a string: ')
    newstring = separate(string)
    print(newstring)

def separate(string):
    newWord = True
    newString = ""
    
    for char in string:
        if char.isupper():
            if not newWord:
                newString += ' '
                newWord = True
            newString += char.lower()
            newWord = False
        else:
            newString += char
            newWord = False
            
    newString = newString.capitalize() # Capitalize the first letter of the resulting string  
                
    return newString
                
main()
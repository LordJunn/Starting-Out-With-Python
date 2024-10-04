"""
Write a program with a function that accepts a string as an argument and returns a copy
of the string with the first character of each sentence capitalized. For instance, if the argu-
ment is “hello. my name is Joe. what is your name?” the function should return the string
“Hello. My name is Joe. What is your name?” The program should let the user enter
a string and then pass it to the function. The modified string should be displayed.
"""
def main():
    string = input('Enter a string: ')
    newstring = capitalise(string)
    print(newstring)

def capitalise(string):
    newSentence = True
    newString = ""
    
    for lines in string:
        for char in lines:
            if (char.isalpha() and newSentence):
                newString += char.upper()
                newSentence = False
            else:
                newString += char
            
            if (char == '.' or char == '!' or char == '?'): # or use if char in '.!?'
                newSentence = True
                
    return newString
                
main()
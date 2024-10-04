"""
Write a program that accepts a sentence as input and converts each word to “Pig Latin.” In
one version, to convert a word to Pig Latin, you remove the first letter and place that letter
at the end of the word. Then, you append the string “ay” to the word. Here is an example:
English: I SLEPT MOST OF THE NIGHT
Pig Latin: IAY LEPTSAY OSTMAY FOAY HETAY IGHTNAY
"""

def main():
    string = input('Enter a string to be translated into pig latin: ')
    oink = pig(string)
    print(oink)

def pig(string):
    newString = []
    string = string.upper()
    words = string.split()
    pork = []
    
    for word in words:
        pork = word[1:] + word[:1] + 'AY'        
        newString.append(pork)

    return ' '.join(newString)

main()
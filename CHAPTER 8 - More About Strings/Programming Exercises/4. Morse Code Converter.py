"""
Morse code is a code where each letter of the English alphabet, each digit, and various
punctuation characters are represented by a series of dots and dashes. Table 8-4 shows part
of the code.
Write a program that asks the user to enter a string, then converts that string to Morse code.
"""
morsecode = [ # tuple, GPT
    ('A', '.-'),       ('B', '-...'),     ('C', '-.-.'),     ('D', '-..'),      ('E', '.'),       
    ('F', '..-.'),     ('G', '--.'),      ('H', '....'),     ('I', '..'),       ('J', '.---'),    
    ('K', '-.-'),      ('L', '.-..'),     ('M', '--'),       ('N', '-.'),       ('O', '---'),     
    ('P', '.--.'),     ('Q', '--.-'),     ('R', '.-.'),      ('S', '...'),      ('T', '-'),       
    ('U', '..-'),      ('V', '...-'),     ('W', '.--'),      ('X', '-..-'),     ('Y', '-.--'),    
    ('Z', '--..'),     ('0', '-----'),    ('1', '.----'),    ('2', '..---'),    ('3', '...--'),   
    ('4', '....-'),    ('5', '.....'),    ('6', '-....'),    ('7', '--...'),    ('8', '---..'),   
    ('9', '----.'),    ('.', '.-.-.-'),   (',', '--..--'),   ('?', '..--..'),   ("'", '.----.'),   
    ('!', '-.-.--'),   ('/', '-..-.'),    ('(', '-.--.'),    (')', '-.--.-'),   ('&', '.-...'),    
    (':', '---...'),   (';', '-.-.-.'),   ('=', '-...-'),    ('+', '.-.-.'),    ('-', '-....-'),   
    ('_', '..--.-'),   ('"', '.-..-.'),   ('@', '.--.-'),    (' ', ' ')
]

def main():
    word = input('What word would you like to translate into morse code? ')
    morse = converter(word.upper())
    print(f'{word} = {morse}')

def converter(words):
    output = []
    for char in words:
        found = False
        for pairer in morsecode:
            if pairer[0] == char:
                output.append(pairer[1])
                found = True
                break
        if not found:
            output.append('?')
            
    result = ' '.join(output)
    
    return result

main()
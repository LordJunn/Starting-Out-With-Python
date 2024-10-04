"""
A “Caesar Cipher” is a simple way of encrypting a message by replacing each letter with a
letter a certain number of spaces up the alphabet. For example, if shifting the message by
13 an A would become an N, while an S would wrap around to the start of the alphabet to
become an F.
Write a program that asks the user for a message (a string) and a shift amount (an integer).
The values should be passed to a function that accepts a string and an integer as arguments,
and returns a string representing the original string encrypted by shifting the letters by the
integer. For example, a string of “BEWARE THE IDES OF MARCH” and an integer of 13
should result in a string of “ORJNER GUR VQRF BS ZNEPU”.
"""
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
    string = input('Enter a message: ')
    shift = int(input('Enter a shift amount: '))
    cipher = caesar(string, shift)
    print(cipher)

def caesar(msg, shift):
    global alphabet
    encrypt = ""
    for char in msg:
        if char.isalpha():
            if char.isupper():
                alphabet = alphabet.upper() # change to upper, if it was lower
            else:
                alphabet = alphabet.lower() # change to lower
            cindex = alphabet.find(char) # character index, A = 0, B = 1... Z = 25
            sindex = (cindex + shift) % 26 # character index + shift amount, "minus 26"
            shifted = alphabet[sindex] # find index of character
            encrypt += shifted 
        else:
            encrypt += char # in case it isnt a character
            
    return encrypt

main()
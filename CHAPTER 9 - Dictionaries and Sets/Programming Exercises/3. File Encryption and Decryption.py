"""
Write a program that uses a dictionary to assign “codes” to each letter of the alphabet. For
example:
codes = { ‘A’ : ‘%’, ‘a’ : ‘9’, ‘B’ : ‘@’, ‘b’ : ‘#’, etc . . .}
Using this example, the letter A would be assigned the symbol %, the letter a would be
assigned the number 9, the letter B would be assigned the symbol @, and so forth.
The program should open a specified text file, read its contents, then use the dictionary
to write an encrypted version of the file’s contents to a second file. Each character in the
second file should contain the code for the corresponding character in the first file.
Write a second program that opens an encrypted file and displays its decrypted contents
on the screen.
""" # use yes sir.txt
codes = {
    'A': '%', 'B': '@', 'C': '#', 'D': '&', 'E': '*', 'F': '(', 'G': ')', 'H': '!',
    'I': '-', 'J': '=', 'K': '+', 'L': '[', 'M': ']', 'N': '{', 'O': '}', 'P': '|',
    'Q': ';', 'R': ':', 'S': "'", 'T': '"', 'U': '<', 'V': '>', 'W': ',', 'X': '.',
    'Y': '/', 'Z': '?', 'a': '9', 'b': '8', 'c': '7', 'd': '6', 'e': '5', 'f': '4',
    'g': '3', 'h': '2', 'i': '1', 'j': '0', 'k': '!', 'l': '@', 'm': '#', 'n': '$',
    'o': '%', 'p': '^', 'q': '&', 'r': 'v', 's': '(', 't': ')', 'u': '-', 'v': '=',
    'w': '+', 'x': '[', 'y': ']', 'z': '{', ' ': ' '  # Space remains unchanged, may contain repeated stuff
}
sedoc = {v: k for k, v in codes.items()} # reversed dict, key: value becomes value: key (swapped)

def main():
    choice = 2
    while (choice != 3):
        choice = menu()
        if choice > 3:
            print("This isn't valid. Do it again.")
        elif choice == 1:
            encrypt()
        elif choice == 2:
            decrypt()
        
    print("Exiting program!")

def menu():
    print("File Encryption and Decryption Program")
    print("|------------------------------------|")
    print("Select your choice: ")
    choice = int(input("1. Encrypt a file \n2. Decrypt a file \n3. Exit program\n"))
    
    return choice

def encrypt():
    filename = input('What is the name of the file to encrypt? ')
    file = filename.strip(".txt")
    outputFile = file + "_encrypted.txt"
    
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        with open(outputFile, 'w') as f:
            for line in lines:
                for char in line:
                    if char in codes:
                        f.write(codes[char])
                    else:
                        f.write(char)
                        
        print(f'{filename} successfully encrypted, its contents is now in {outputFile}.')

    except FileNotFoundError:
        print(f"The file '{file}' was not found.")
        return None     
    
def decrypt():
    filename = input('What is the name of the file to decrypt? ')
    file = filename.strip(".txt")
    outputFile = file + "_decrypted.txt"
    
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        with open(outputFile, 'w') as f:
            for line in lines:
                for char in line:
                    if char in sedoc:
                        f.write(sedoc[char])
                    else:
                        f.write(char)

        print(f'{filename} successfully decrypted, its contents is now in {outputFile}.')

    except FileNotFoundError:
        print(f"The file '{file}' was not found.")
        return None     

main()
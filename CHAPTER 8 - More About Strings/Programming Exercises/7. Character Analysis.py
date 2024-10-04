"""
If you have downloaded the source code you will find a file named text.txt in the Chapter 08
folder. Write a program that reads the file’s contents and determines the following:
• The number of uppercase letters in the file
• The number of lowercase letters in the file
• The number of digits in the file
• The number of whitespace characters in the file
"""

def main():
    file = 'text.txt'
    up, low, dig, space, idk = analyser(file)    
    
    print(f"""
• The number of uppercase letters in the file: {up}
• The number of lowercase letters in the file: {low}
• The number of digits in the file: {dig}
• The number of whitespace characters in the file: {space}
• The number of unknown characters in the file: {idk}
""")
    
def analyser(file): 
    try:
        
        uppers = 0
        lowers = 0
        digits = 0
        whites = 0
        idk = 0
        
        with open(file, 'r') as file:
        
            for lines in file: # Iterate over each line in the file
                for char in lines: # Iterate over each character in the line
                    if char.isupper():
                        uppers += 1
                    elif char.islower():
                        lowers += 1
                    elif char.isdigit():
                        digits += 1
                    elif char.isspace():
                        whites += 1
                    else:
                        idk += 1
                        
        
        return uppers, lowers, digits, whites, idk

    except FileNotFoundError:
        print(f"The file '{file}' was not found.")
        return None    
    
main()
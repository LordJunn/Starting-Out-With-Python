"""
Write a program that asks the user for the name of a file. The program should read all of
the file’s data into a list and display the number of lines of data that the file contains, and
then ask the user to enter the number of the line that they want to view. The program should
display the specified line.
The program should handle the following exceptions by displaying an error message:
• IOError exceptions that are raised when the specified filename cannot be found or
opened.
• ValueError exceptions that are raised when a non-integer value is given as a line number.
• IndexError exceptions that are raised when the line number is outside the range of the
data list.
"""

def main():
    name = input('What is the name of a file? ')
    try:
        file = fileOpenIndexConvertStr(name)
        print(f'{name} has a total of {len(file)} lines')
        line = int(input(f'Enter a line that you want to view in {name}: '))
        print(file[line - 1]) # oh i could just do this instead of a whole function
        
    except IOError:
        print(f'{name} cannot be found or opened.')
        
    except ValueError:
        print('A non-integer value is given as a line number.')
        
    except IndexError:
        print(f'{line} is outside the range of the data list.')
    
def fileOpenIndexConvertStr(fileName): # opens a file, converts item in it into string
    infile = open(fileName, 'r')
    acc = infile.readlines()
    infile.close()
    
    index = 0
    while index < len(acc):
        acc[index] = str(acc[index].strip()) # strip is necessary
        index += 1  
        
    return acc  

main()
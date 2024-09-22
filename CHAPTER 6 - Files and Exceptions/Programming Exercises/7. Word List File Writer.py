"""
Write a program that asks the user how many words they would like to write to a file, and
then asks the user to enter that many words, one at a time. The words should be written
to a file.
"""

def main():
    file = input('Name of a file to write into? ') #C6PE7.txt
    words = int(input(f'How many words they would like to write into {file}? '))
    lineWrite(file, words)
    print(f'Finished writing {words} words into {file}.')

def lineWrite(name, count):
    infile = open(name, 'w')
    for num in range(count):
        word = input(f'Write the #{num + 1} word: ')
        infile.write(word + '\n')
        
main()
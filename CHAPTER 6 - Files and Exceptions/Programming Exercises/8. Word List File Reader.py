"""
This exercise assumes you have completed the Programming Exercise 7, Word List File
Writer. Write another program that reads the words from the file and displays the follow-
ing data:
• The number of words in the file.
• The longest word in the file.
• The average length of all of the words in the file.
"""

def main():
    file = input('Name of a file to read into? ') #C6PE7.txt
    count = lineReadCounter(file)
    total, longest = lineRead(file, count)
    print(f'The number of words in {file}: {total}')
    print(f'The longest word in {file}: {longest}')   
    print(f'The average length of all of the words in {file}: {total}') 

def lineReadCounter(name):
    infile = open(name, 'r')
    counter = 0
    while (infile.readline() != ''):
        counter += 1
    infile.close()
    return counter

def lineRead(name, lines):
    total = 0
    longest_word = ""
    infile = open(name, 'r')
    for count in range(lines): 
        word = infile.readline().rstrip("\n")
        wordlen = len(word)
        total += wordlen
        if (wordlen > len(longest_word)):
            longest_word = word
        
    infile.close()    
    return total, longest_word       
    
main()
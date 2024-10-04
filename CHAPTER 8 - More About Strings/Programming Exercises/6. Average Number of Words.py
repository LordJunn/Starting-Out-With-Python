"""
If you have downloaded the source code from the Premium Companion Website you will
find a file named text.txt in the Chapter 08 folder. The text that is in the file is stored
as one sentence per line. Write a program that reads the file’s contents and calculates the
average number of words per sentence.
(You can access the Premium Companion Website at www.pearsonglobaleditions.com/gaddis.)
"""

def main():
    file = 'text.txt'
    avg = average(file)
    print(f'The average number of words per sentence: {avg}')
    
def splitter(sentence):
    words = sentence.split()
    
    return len(words)
    
def average(file): 
    try:
        with open(file, 'r') as file:
            lines = file.readlines()
            
        sentences = 0
        words = 0
        
        for line in lines:
            sentence = line.strip()
            if sentence:
                sentences += 1
                words += splitter(sentence)
                
        if sentences == 0:
            return 0
        
        avg = words/sentences
        return avg

    except FileNotFoundError:
        print(f"The file '{file}' was not found.")
        return None    
    
main()
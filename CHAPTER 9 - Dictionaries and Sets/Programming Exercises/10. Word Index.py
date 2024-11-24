"""
Write a program that reads the contents of a text file. The program should create a diction-
ary in which the key-value pairs are described as follows:
• Key. The keys are the individual words found in the file.
• Values. Each value is a list that contains the line numbers in the file where the word
(the key) is found.
For example, suppose the word “robot” is found in lines 7, 18, 94, and 138. The dictionary
would contain an element in which the key was the string “robot”, and the value was a list
containing the numbers 7, 18, 94, and 138.
Once the dictionary is built, the program should create another text file, known as a word
index, listing the contents of the dictionary. The word index file should contain an alpha-
betical listing of the words that are stored as keys in the dictionary, along with the line
numbers where the words appear in the original file. Figure 9-1 shows an example of an
original text file (Kennedy.txt) and its index file (index.txt).
""" # https://stackoverflow.com/questions/65535897/write-a-program-that-reads-the-contents-of-a-text-file-and-return-index-of-words

def main():
    keys = {}
    with open ('kennedy.txt', 'r') as f:
        for i,line in enumerate(f):
            words = line.strip().split()
            for word in set(words):
                keys.setdefault(word, []).append(i+1) 

    for k in sorted(keys):
        print(k+':', *keys[k])
    
    index(keys)

def index(keys):
    filename = input('What is the name of the file to index? ')
    file = filename.strip(".txt")
    outputFile = file + "_indexed.txt"
    
    try:
        with open(outputFile, 'w') as f:
            for k in sorted(keys):
                f.write(f"{k}: {' '.join(map(str, keys[k]))}\n")
                        
        print(f'{filename} successfully written, its contents is now in {outputFile}.')

    except FileNotFoundError:
        print(f"The file '{file}' was not found.")
        return None     
    
main()
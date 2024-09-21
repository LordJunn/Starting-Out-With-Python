"""
Python allows you to repeat a string by multiplying it by an integer, e.g. 'Hi' * 3 will give
'HiHiHi'. Pretend that this feature does not exist, and instead write a function named
repeat that accepts a string and an integer as arguments. The function should return a
string of the original string repeated the specified number of times, e.g. repeat('Hi', 3)
should return 'HiHiHi'.
"""

def main():
    word = input('Write a word: ')
    repetition = int(input('How many times do you want it to be repeated? '))
    final = repeater(word, repetition)
    print(final)

def repeater(item, reps): #gpt
    result = ''
    for count in range(reps):
        result += item
    return result
        
main()
        
"""
this wouldnt work
def repeater(item, reps):
    for count in range(reps):
        print(item)
"""
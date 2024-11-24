"""
Write a program that generates 100 random numbers between 1 and 10. The program
should store the frequency of each number generated in a dictionary with the number as
the key and the amount of times it has occurred as the value. For example, if the program
generates the number 6 a total of 11 times, the dictionary will contain a key of 6 with an
associated value of 11. Once all of the numbers have been generated, display information
about the frequency of each number.
"""
import random
generated = {}

def main():
    generating = 100
    min = 1
    max = 10
    
    generate(generating, min, max)
    for frequency in sorted(generated):
        print(f'{frequency}: {generated[frequency]}')
    
def generate(i, min, max):
    for _ in range(i):
        num = random.randint(min, max)
        if num not in generated:
            generated[num] = 1
        else:
            generated[num] += 1
            
main()
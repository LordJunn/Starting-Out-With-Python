"""
The Springfork Amateur Golf Club has a tournament every weekend. The club president
has asked you to write two programs:
1. A program that will read each player’s name and golf score as keyboard input, then
save these as records in a file named golf.txt. (Each record will have a field for the
player’s name and a field for the player’s score.)
2. A program that reads the records from the golf.txt file and displays them.
""" # it could be expanded to read other stuff, but it says golf.txt

def main():
    heading()
    choice = int(input('Now, enter your choice: '))     
    while(choice != 0):
        
        if(choice == 1):
            players = writer('golf.txt')
            print()
        elif(choice == 2):   
            print('Number\tName\tScore')             
            reader('golf.txt', players)
            print()
        else:
            print("{choice} was an invalid choice.")
        heading()
        choice = int(input('Now, enter your choice: '))    

def writer(name):
    infile = open(name, 'w')
    cont = 'y' 
    count = 1
    while (cont != 'n'):
        name = input(f"Write down player #{count}'s name: ")
        score = input(f"Write down player {name}'s score: ")   
        infile.write(name + ' ' + score + '\n')   
        cont = input('Would you like to continue? Press n if not. ')  
        count += 1
    return count
           
def reader(name, lines):
    infile = open(name, 'r')
    for count in range(lines - 1): # lines - 1 as a fix so that it wouldnt read the empty line below
        C6PE10 = infile.readline()
        name, skor = C6PE10.strip().split()
        print(f'{count + 1}\t{name}\t{skor}')
    infile.close()      

def heading():
    print('Springfork Amateur Golf Club')
    print('Choose 1 to write scores')
    print('Choose 2 to read scores') 
    print('Choose 0 to quit')   
    
main()
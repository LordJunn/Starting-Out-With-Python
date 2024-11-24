"""
Write a program that keeps vegetable names and prices in a dictionary as key-value pairs.
The program should display a menu that lets the user see a list of all vegetables and their
prices, add a new vegetable and price, change the price of an existing vegetable, and delete
an existing vegetable and price. The program should pickle the dictionary and save it to a
file when the user exits the program. Each time the program starts, it should retrieve the
dictionary from the file and unpickle it.
"""
import pickle

def main():
    information = 'C9PE8.dat'
    vegetables = sayur(information)
    choice = 9
    while choice != 5:
        choice = menu()
        if (choice < 0) or (choice > 5):
            print("This isn't a valid choice. ")
        elif choice == 0:
            clear_file(information)
        elif choice == 1:
            satu(vegetables)
        elif choice == 2:
            dua(vegetables)
        elif choice == 3:
            tiga(vegetables)
        elif choice == 4:
            empat(vegetables)
        elif choice == 5:
            lima(vegetables, information)
            print('Data saved.')
    
    print('Exiting program.')
            
def menu(): 
    print("          Pickled Vegetables Program          ")
    print("------------------------------------------------")
    print("(1) List of all vegetables and their prices")
    print("(2) Add a new vegetable and price")
    print("(3) Change the price of an existing vegetable")
    print("(4) Delete an existing vegetable and price")
    print("(5) Exit program")
    choice = int(input("\nNow, choose a choice: "))
    
    return choice

def sayur(data): # loads data (.DAT) into dict
    with open(data, 'rb') as file:
        try:
            return pickle.load(file)
        except EOFError:
            return {}

def satu(data): # (1) List of all vegetables and their prices
    if not data:
        print('No vegetables to display.')
    else:
        print(f"Name:\t\t\tPrice:")  
        for name, price in data.items():
            print(f"{name}\t\t\t{price}")
            
def dua(data): # (2) Add a new vegetable and price, Referenced from C9-2 

    name = input('Name: ').strip()
    
    try:
        price = int(input('Price: '))
    except ValueError:
        print("Invalid price. Please enter a numeric value.")
        return
    
    if name not in data:
        data[name] = price
        print(f"Added {name} with price {price}.")
    else:
        print("This vegetable already exists.")

def tiga(data): # (3) Change the price of an existing vegetable, Referenced from C9-2
    
    name = input('Enter a vegetable: ').strip() 
    if name in data:
        price = input('Enter the new price: ')
        data[name] = price
        
    else:
        print('That vegetable is not found.')

def empat(data): # (4) Delete an existing vegetable and price, Referenced from C9-2
    name = input('Enter a vegetable: ').strip() 
    if name in data:
        del data[name]
        
    else:
        print('That vegetable is not found.')    
        
def lima(data, fileN): # (5) Exit program, saves file
    with open(fileN, 'wb') as file:
        pickle.dump(data, file)
        
def clear_file(filename): # pure gpt, in case needed
    # Open the file in write-binary mode ('wb') to clear its contents
    with open(filename, 'wb') as file:
        # Write an empty dictionary to the file
        pickle.dump({}, file)
    print("The file has been cleared.")

main()








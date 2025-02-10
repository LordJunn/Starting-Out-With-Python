"""This exercise assumes you have created the RetailItem class for Programming Exer-
cise 5. Create a CashRegister class that can be used with the RetailItem class. The
CashRegister class should be able to internally keep a list of RetailItem objects. The
class should have the following methods:
• A method named purchase_item that accepts a RetailItem object as an argument.
Each time the purchase_item method is called, the RetailItem object that is passed
as an argument should be added to the list.
• A method named get_total that returns the total price of all the RetailItem objects
stored in the CashRegister object’s internal list.
• A method named show_items that displays data about the RetailItem objects stored
in the CashRegister object’s internal list.
• A method named clear that should clear the CashRegister object’s internal list.
Demonstrate the CashRegister class in a program that allows the user to select several
items for purchase. When the user is ready to check out, the program should display a list
of all the items he or she has selected for purchase, as well as the total price."""
from RetailItem import RetailItem
import pickle

class CashRegister:
    def __init__(self):
        self.__items = []
        
    def purchase_item(self, item):
        if isinstance(item, RetailItem):
            self.__items.append(item)
        else:
            raise TypeError("Only RetailItem objects can be added.")
    
    def get_total(self):
        total = sum(item.priceG() for item in self.__items)
        return total
    
    def show_items(self):
        if not self.__items:
            print("No items in the cart.")
        else:
            print(f"{'Item':<20} {'Unit':<10} {'Price':<10}")
            print("-" * 40)
            for item in self.__items:
                print(f"{item.itemG():<20} {item.unitG():<10} ${item.priceG():<10.2f}")
                
    def clear(self):
        self.__items.clear()

def main():
    register = CashRegister()
    retail = RetailItem()
    choicem = 0   
    while choicem != 3:
        choicem = menu()
        if choicem == 1:
            choicer = retailMenu()
            if choicer == 1:
                print('owo')
            elif choicer == 2:
                lookup(retail, "item")
        elif choicem == 2:
            choicec = cashMenu()
        
    
def menu():
    choice = 0
    while choice != 3:
        print("Something")
        print("(1) Enter the Retail Shop")
        print("(2) Enter the Cash Registry")
        choice = int(input("\nNow, choose a choice: "))
        if choice == 1:
            retailMenu()
        elif choice == 2:
            cashMenu()
    
    return choice    
 
def retailMenu():
    file = 'C10PE8rm.dat'
    load(file, RetailItem())
    choice = 0
    while choice != 6:
        print("                   Retail Shop                   ")
        print("-------------------------------------------------")
        print("(1) Display all the retail items")
        print("(2) Look up an item")
        print("(3) Add a new item")
        print("(4) Change an existing items stock and price")
        print("(5) Delete an item")
        print("(6) Exit the Retail Shop")
        choice = int(input("\nNow, choose a choice: "))
        
    save(file, RetailItem())
    
    return choice     

def lookup(info, owo):
    id = input(f"Enter an {owo} to look up: ")
    if id in info:
        print(info[id])
    else:
        print(f"{owo} not found.")    
    
def load(filename, item):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return item

def save(filename, item):
    with open(filename, 'wb') as file:
        pickle.dump(item, file)
    
    

def cashMenu():
    choice = 0
    while choice != 5:
        print("                   Cash Registry                   ")
        print("---------------------------------------------------")
        print("(1) Add an item to cart")
        print("(2) Checkout")
        print("(3) Display cart")
        print("(4) Clear cart")
        print("(5) Exit the Cash Registry")
        choice = int(input("\nNow, choose a choice: "))
    
    return choice  












main()



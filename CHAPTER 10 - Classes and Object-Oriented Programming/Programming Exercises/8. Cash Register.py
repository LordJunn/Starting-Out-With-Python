"""This exercise assumes you have created the RetailItem class for Programming Exer-
cise 5. Create a CashRegister class that can be used with the RetailItem class. The
CashRegister class should be able to internally keep a list of RetailItem objects. The
class should have the following methods:
• A method named purchase_item that accepts a RetailItem object as an argument.
Each time the purchase_item method is called, the RetailItem object that is passed
as an argument should be added to the list.
• A method named get_total that returns the total price of all the RetailItem objects
stored in the CashRegister object’s internal list.
• A method named show_items that displays info about the RetailItem objects stored
in the CashRegister object’s internal list.
• A method named clear that should clear the CashRegister object’s internal list.
Demonstrate the CashRegister class in a program that allows the user to select several
items for purchase. When the user is ready to check out, the program should display a list
of all the items he or she has selected for purchase, as well as the total price.""" # i give up fixing it, have fun with multiple instances of it
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
            print(f"{'Item':<20}{'Price':<10}")
            print("-" * 40)
            for item in self.__items:
                print(f"{item.itemG():<20} ${item.priceG():<10.2f}")
                
    def clear(self):
        self.__items.clear()

def main():
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
        
################ LOAD & SAVE FILE ################  
 
def load(filename, item):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        if item == 'retail':
            return {}
        elif item == 'register':
            return []
        else:
            raise ValueError("Unknown item specified")

def save(filename, item):
    with open(filename, 'wb') as file:
        pickle.dump(item, file)
 
################ RETAIL ################ 
 
def retailMenu():
    file = 'C10PE8rm.dat'
    retail = load(file, 'retail')
    while True: # forced
        print("                   Retail Shop                   ")
        print("-------------------------------------------------")
        print("(1) Display all the retail items")
        print("(2) Look up an item")
        print("(3) Add a new item")
        print("(4) Change an existing items stock and price")
        print("(5) Delete an item")
        print("(6) Exit the Retail Shop")
        choice = int(input("\nNow, choose a choice: "))
        
        if choice == 1:
            display(retail, "retail")
        elif choice == 2:
            lookup(retail, "item")
        elif choice == 3:
            add(retail)
        elif choice == 4:
            change(retail)
        elif choice == 5:
            delete(retail)
        elif choice == 6:
            save(file, retail)
            break            

def display(info, type):
    if not info:
        print(f'No {type} to display.')
    else:
        if type == "retail":
            print(f"{'Name':<20} {'Stock':<10} {'Price':<10}")
            print("-" * 40)
            for name, item in info.items(): # name = key, item = wat we want
                print(f"{item.itemG():<20} {item.unitG():<10} ${item.priceG():<10.2f}") # general formatting
        elif type == "register":
            print(f"{'Name':<20} {'Unit Price':<10} {'Amount':<10} {'Total Price':<10}")
            print("-" * 40)
            for name, item in info.items(): # name = key, item = wat we want
                print(f"{item.itemG():<20} {item.unitG():<10} ${item.priceG():<10.2f}") # general formatting            
            
def lookup(info, owo):
    name = input(f"Enter an {owo} to look up: ")
    if name in info:
        print(info[name])
    else:
        print(f"{owo} not found.")    
    
def add(info):   
    name = input(f"Enter item's name: ") 
    unit = int(input(f"Enter {name}'s stock: "))
    price = float(input(f"Enter {name}'s price: "))
    if name not in info:
        info[name] = RetailItem(name, unit, price)
    else:
        print(f"{name} already exists.")

    
    
def change(info):
   name = input(f"Enter item's name to change their info: ") 
   if name in info:
        unit = int(input(f"Enter {name}'s new stock: "))
        price = float(input(f"Enter {name}'s new price: "))
        info[name] = RetailItem(name, unit, price)
   else:
       print(f"{name} not found.")        
    
def delete(info):
   name = input(f"Enter item's name to change their info: ") 
   if name in info:
        del info[name]
        print(f'{name} has been deleted.')
   else:
       print(f"{name} not found.")            

################ CASH REGISTER ################ 

def cashMenu():
    register = CashRegister()
    shop = 'C10PE8rm.dat'
    market = load(shop, 'retail')
    
    while True: # forced
        print("                   Cash Registry                   ")
        print("---------------------------------------------------")
        print("(1) Add an item to cart")
        print("(2) Checkout")
        print("(3) Display cart")
        print("(4) Clear cart")
        print("(5) Exit the Cash Registry")
        choice = int(input("\nNow, choose a choice: "))

        if choice == 1:
            buy(register)
        elif choice == 2:
            register.show_items() 
            print(f"Total: ${register.get_total():.2f}")
            register.clear()
        elif choice == 3:
            register.show_items()
            print(f"Total: ${register.get_total():.2f}")
        elif choice == 4:
            register.clear()
        elif choice == 5:
            break        

def buy(register):
    name = input("Enter the item name to add to cart: ")
    retail = load('C10PE8rm.dat', 'retail')
    if name in retail:
        item = retail[name]
        quantity = int(input("Enter the quantity: "))
        
        if quantity <= item.unitG():
            for _ in range(quantity):
                register.purchase_item(item)
            print(f"{quantity}x {name} added to cart.")
        else:
            print(f"Only {item.unitG()} of {name} is available.")
    else:
        print(f"{name} is not available in retail items.") 









main()



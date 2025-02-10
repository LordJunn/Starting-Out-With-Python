"""
Write a class named RetailItem that holds data about an item in a retail store. The class
should store the following data in attributes: item description, units in inventory, and price.
Once you have written the class, write a program that creates three RetailItem objects
and stores the following data in them:
Description Units in Inventory Price
Item #1 Jacket 12 59.95
Item #2 Designer Jeans 40 34.95
Item #3 Shirt 20 24.95
"""
import RetailItem # changed to do C10PE8

def main():
    item1 = RetailItem.RetailItem("Jacket", 12, 59.95)
    item2 = RetailItem.RetailItem("Designer Jeans", 40, 34.95)
    item3 = RetailItem.RetailItem("Shirt", 20, 24.95)
    
    print('Name\t\tUnits in Inventory\tPrice')
    print(f'{item1.itemG()}\t\t{item1.unitG()}\t\t\t{item1.priceG()}')
    print(f'{item2.itemG()}\t{item2.unitG()}\t\t\t{item2.priceG()}')
    print(f'{item3.itemG()}\t\t{item3.unitG()}\t\t\t{item3.priceG()}')   
    
main()
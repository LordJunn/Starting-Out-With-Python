class RetailItem:
    def __init__(self, item, unit, price):
        self.__item = item
        self.__unit = unit
        self.__price = price
        
    def __init__(self, item='', unit='', price=0.0): # made for C10PE8
        self.__item = item
        self.__unit = unit
        self.__price = price

    def itemG(self):
        return self.__item
    
    def unitG(self):
        return self.__unit
    
    def priceG(self):
        return self.__price
    
    def __str__(self): # Added cuz of C10PE8
        return f"Name: {self.__item} \nStock: {self.__unit} \nPrice: {self.__price}"
    
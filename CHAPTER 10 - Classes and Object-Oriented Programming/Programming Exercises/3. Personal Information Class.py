"""
Design a class that holds the following personal data: name, address, age, and phone num-
ber. Write appropriate accessor and mutator methods. Also, write a program that creates
three instances of the class. One instance should hold your information, and the other two
should hold your friends’ or family members’ information.
""" # slight gpt to save some lines for me
class Information:
    def __init__(self, name, address, age, phone): # nah imma treat u as the mutator of this
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone
        
    def nameS(self, name):
        self.__name = name
    
    def addressS(self, address):
        self.__address = address
    
    def ageS(self, age):
        if age > 0:
            self.__age = age
    
    def phoneS(self, phone):
        self.__phone = phone       
        
    def nameG(self):
        return self.__name
    
    def addressG(self):
        return self.__address
    
    def ageG(self):
        return self.__age
    
    def phoneG(self):
        return self.__phone
    
def main():
    people = []
    labels = ["yourself", "friend", "family"]
    
    for role in labels:
        if role == 'yourself':
            print(f"\nEnter information for {role}:")
        else:
            print(f"\nEnter information for your {role}:") 
        
        name = input('What is the name? ')
        address = input('What is the address? ')
        age = int(input('What is the age? '))
        phone = input('What is the phone number? ')
        
        person = Information(name, address, age, phone)
        people.append(person)
        print()
        
    for label, person in zip(labels, people):
        if label == 'yourself':
            print(f"\nInformation for {label}:")
        else:
            print(f"\nInformation for your {label}:")            
        print(f"Name: {person.nameG()}")
        print(f"Address: {person.addressG()}")
        print(f"Age: {person.ageG()}")
        print(f"Phone: {person.phoneG()}")

main()
"""
This exercise assumes you have created the Employee class for Programming Exercise 4.
Create a program that stores Employee objects in a dictionary. Use the employee ID num-
ber as the key. The program should present a menu that lets the user perform the following
actions:
• Look up an employee in the dictionary
• Add a new employee to the dictionary
• Change an existing employee’s name, department, and job title in the dictionary
• Delete an employee from the dictionary
• Quit the program
When the program ends, it should pickle the dictionary and save it to a file. Each time the
program starts, it should try to load the pickled dictionary from the file. If the file does not
exist, the program should start with an empty dictionary.
""" # stolen from C9PE8
from Employee import Employee # if just import Employee gotta type Employee.Employee
import pickle

def main():
    information = 'C10PE7.dat'
    pekerja = load(information)
    choice = 9
    while choice != 5:
        choice = menu()

        if choice == 1:
            lookup(pekerja)
        elif choice == 2:
            add(pekerja)
        elif choice == 3:
            update(pekerja)
        elif choice == 4:
            delete(pekerja)
        elif choice == 5:
            save(information, pekerja)

def menu():
    print("                   Employee Management System                   ")
    print("-----------------------------------------------------------------")
    print("(1) Look up an employee")
    print("(2) Add a new employee")
    print("(3) Change an existing employee’s name, department, and job title")
    print("(4) Delete an employee")
    print("(5) Exit program")
    choice = int(input("\nNow, choose a choice: "))
    
    return choice    

def load(filename):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}

def lookup(pekerja):
    id = input("Enter employee ID to look up: ")
    if id in pekerja:
        print(pekerja[id])
    else:
        print("Employee not found.")

def add(pekerja):
    name = input("Enter employee's name: ")
    ID = input("Enter employee ID: ")
    department = input("Enter department: ")
    title = input("Enter job title: ")
    if ID not in pekerja:
        pekerja[ID] = Employee(name, ID, department, title)
        print("Employee added.")
    else:
        print(f"Sorry, ID {ID} has been used, please choose another.")
    
def update(pekerja):
    id = input("Enter employee ID to update: ")
    if id in pekerja:
        name = input("Enter new name: ")
        department = input("Enter new department: ")
        title = input("Enter new job title: ")
        pekerja[id] = Employee(name, id, department, title)
        print("Employee updated.")
    else:
        print("Employee not found.")

def delete(pekerja):
    id = input("Enter employee ID to delete: ")
    if id in pekerja:
        del pekerja[id]
        print("Employee deleted.")
    else:
        print("Employee not found.")

def save(filename, data):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)
    print('Data saved.')

main()
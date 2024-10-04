"""
Write a program that gets strings containing a person’s first and last name as separate
values, and then displays their “initials”, “name in address book”, and “username”. For
example, if the user enters a first name of “John” and a last name of “Smith”, the program
should display “J.S.”, “John SMITH”, and “jsmith”.
"""

def main():
    first = input('Enter your first name: ')
    last = input('Enter your last name: ')
    
    ini = initial(first, last)
    add = address(first, last)
    user = username(first, last)
    
    print(f'Initials: {ini}')
    print(f'Name in address book: {add}')
    print(f'Username: {user}')
    
def initial(first, last):
    n1 = first[0:1]
    n2 = last[0:1]
    name = n1 + "." + n2 + "."
    return name
 
def address(first, last):
    name = first + " " + last.upper()
    return name
       
def username(first, last):
    n1 = first[0:1]
    n1 = n1.lower()
    name = n1 + last
    name = name.lower()
    return name
    
main()
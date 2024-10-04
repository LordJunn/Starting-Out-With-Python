"""
Write a program that reads a string from the user containing a date in the form mm/dd/yyyy.
It should print the date in the format March 12, 2018.
"""

months = [ 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December' ]

def main():
    date = input('Enter a date: ')
    format = american(date)
    print(format)
    
def american(date):
    list = date.split('/')
    month = int(list[0])
    m = months[month - 1]
    d = list[1]
    y = list[2]
    format = m + " " + d + ", " + y
    return format
    
main()
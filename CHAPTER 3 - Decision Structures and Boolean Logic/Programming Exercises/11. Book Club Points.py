"""
Serendipity Booksellers has a book club that awards points to its customers based on the
number of books purchased each month. The points are awarded as follows:
• If a customer purchases 0 books, he or she earns 0 points.
• If a customer purchases 2 books, he or she earns 5 points.
• If a customer purchases 4 books, he or she earns 15 points.
• If a customer purchases 6 books, he or she earns 30 points.
• If a customer purchases 8 or more books, he or she earns 60 points.
Write a program that asks the user to enter the number of books that he or she has pur-
chased this month, then displays the number of points awarded.
"""

book = int(input("Enter the number of books that you purchased this month: "))

if(book >= 8):
    print('+60 points.')
elif(book >= 6):
    print('+30 points.')
elif(book >= 4):
    print('+15 points.')
elif(book >= 2):
    print('+5 points.')
else:
    print('No points.')
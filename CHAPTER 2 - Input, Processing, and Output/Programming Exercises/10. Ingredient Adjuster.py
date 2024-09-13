"""
A cookie recipe calls for the following ingredients:
• 1.5 cups of sugar
• 1 cup of butter
• 2.75 cups of flour
The recipe produces 48 cookies with this amount of the ingredients. Write a program that
asks the user how many cookies he or she wants to make, then displays the number of cups
of each ingredient needed for the specified number of cookies.
"""

cookies = float(input('How many cookies you want to make? '))
sugar = (1.5/48) * cookies
butter = (1/48) * cookies
flour = (2.75/48) * cookies

print(format(sugar, '.2f'), 'cups of sugar needed')
print(format(butter, '.2f'), 'cups of butter needed')
print(format(flour, '.2f'), 'cups of flour needed')
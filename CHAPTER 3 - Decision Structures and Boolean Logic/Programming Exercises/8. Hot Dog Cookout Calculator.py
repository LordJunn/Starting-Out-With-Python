"""
Assume hot dogs come in packages of 10, and hot dog buns come in packages of 8. Write a
program that calculates the number of packages of hot dogs and the number of packages of
hot dog buns needed for a cookout, with the minimum amount of leftovers. The program
should ask the user for the number of people attending the cookout and the number of hot
dogs each person will be given. The program should display the following details:
• The minimum number of packages of hot dogs required
• The minimum number of packages of hot dog buns required
• The number of hot dogs that will be left over
• The number of hot dog buns that will be left over
"""
hd = 10
hdb = 8

people = int(input("The number of people attending the cookout? "))
dog = int(input("The number of hot dogs each person will be given? "))

total = people * dog

# gpt cuz i have no idea how to do this without using while loop
dogpack = (total + hd - 1) // hd
bunpack = (total + hdb - 1) // hdb

dogleft = (dogpack * hd) - total
bunleft = (bunpack * hdb) - total

print('The minimum number of packages of hot dogs required:', dogpack)
print('The minimum number of packages of hot dog buns required:', bunpack)
print('The number of hot dogs that will be left over:', dogleft)
print('The number of hot dog buns that will be left over:', bunleft)
"""
You have a group of friends coming to visit for your high school reunion, and you want
to take them out to eat at a local restaurant. You aren’t sure if any of them have dietary
restrictions, but your restaurant choices are as follows:
Joe’s Gourmet Burgers—Vegetarian: No, Vegan: No, Gluten-Free: No
Main Street Pizza Company—Vegetarian: Yes, Vegan: No, Gluten-Free: Yes
Corner Café—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
Mama’s Fine Italian—Vegetarian: Yes, Vegan: No, Gluten-Free: No
The Chef’s Kitchen—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
Write a program that asks whether any members of your party are vegetarian, vegan, or
gluten-free, to which then displays only the restaurants to which you may take the group.
Here is an example of the program’s output:
Is anyone in your party a vegetarian? yes [Enter]
Is anyone in your party a vegan? no [Enter]
Is anyone in your party gluten-free? yes [Enter]
Here are your restaurant choices:
Main Street Pizza Company
Corner Cafe
The Chef's Kitchen
Here is another example of the program’s output:
Is anyone in your party a vegetarian? yes [Enter]
Is anyone in your party a vegan? yes [Enter]
Is anyone in your party gluten-free? yes [Enter]
Here are your restaurant choices:
Corner Cafe
The Chef's Kitchen
""" # semi gpt cuz idk waddis without c++

# Ask the user about dietary restrictions
vegetarian = input("Is anyone in your party a vegetarian? (yes/no) ")
vegan = input("Is anyone in your party a vegan? (yes/no) ")
gluten = input("Is anyone in your party gluten-free? (yes/no) ")

# Convert responses to boolean
vegetarian = vegetarian == "yes"
vegan = vegan == "yes"
gluten = gluten == "yes"

# Determine suitable restaurants based on dietary restrictions
print("Here are your restaurant choices:")

# Joe's Gourmet Burgers
if not vegetarian and not vegan and not gluten:
    print("Joe's Gourmet Burgers")

# Main Street Pizza Company
if (not vegetarian or vegetarian) and (not vegan) and (not gluten or gluten):
    print("Main Street Pizza Company")

# Corner Café
# The Chef's Kitchen
if (not vegetarian or vegetarian) and (not vegan or vegan) and (not gluten or gluten):
    print("Corner Café")
    print("The Chef's Kitchen")

# Mama's Fine Italian
if (not vegetarian or vegetarian) and (not vegan) and (not gluten):
    print("Mama's Fine Italian")
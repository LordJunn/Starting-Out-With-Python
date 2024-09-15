"""
Write a program that uses nested loops to draw this pattern:
##
# #
#  #
#   #
#    #
#     #
"""
# stolen from https://jesushilarioh.com/chapter-4-15-using-nested-loops-no-2-tony-gaddis-starting-out-with-python/
SIZE = 7

output = "\n"

for row in range(SIZE):
    output += "#"

    for column in range(row):
        output += " "
    
    output += "#\n"

print(output)
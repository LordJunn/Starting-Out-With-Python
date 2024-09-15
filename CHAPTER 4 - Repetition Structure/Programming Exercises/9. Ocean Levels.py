"""
Assuming the ocean’s level is currently rising at about 1.6 millimeters per year, create an
application that displays the number of millimeters that the ocean will have risen each year
for the next 25 years.
"""

rise = 1.6

print('Year\tRisen')
print('-------------------')

for m in range(1, 26):
    km = rise * m
    print(f'{m}\t{km:.2f}') # stolen from C4PE6
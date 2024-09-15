"""
At one college, the tuition for a full-time student is $8,000 per semester. It has been announced
that the tuition will increase by 3 percent each year for the next 5 years. Write a program
with a loop that displays the projected semester tuition amount for the next 5 years.
"""

increase = 0.03

print('Year\tTuition')
print('-------------------')

for m in range(1, 6):
    km = 8000 * (1 + increase) ** m # ori: 8000 + (8000 * (0.03) * m), oh ** = pow
    print(f'{m}\t${km:.2f}') # stolen from C4PE9
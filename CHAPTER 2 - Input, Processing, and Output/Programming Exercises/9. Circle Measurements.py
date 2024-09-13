"""
Write a program that asks the user to enter the radius of a circle. The program should cal-
culate and display the area and circumference of the circle using πr2 for the area and 2πr
for the circumference.
Hint: You can either use 3.14159 as the value of pi (π), or add the statement "import math"
to the start of the program and then use "math.pi" wherever you need the value of pi in
the program.
"""
import math

rad = float(input('The radius of a circle? '))

area = math.pi * (rad * rad)
circumference = 2 * math.pi * rad

print('The area of the circle:', format(area, '.5f'))
print('The circumference of the circle:', format(circumference, '.5f'))
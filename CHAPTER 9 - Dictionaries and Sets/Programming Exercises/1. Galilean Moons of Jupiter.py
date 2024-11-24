"""
Write a program that creates a dictionary containing the names of the Galilean moons of
Jupiter as keys and their mean radiuses (in kilometers) as values. The dictionary should
contain the following key-value pairs:
Moon Name (key) Mean Radius (value)
Io 1821.6
Europa 1560.8
Ganymede 2634.1
Callisto 2410.3
The program should also create a dictionary containing the moon names and their surface
gravities (in meters per second squared). The dictionary should contain the following key-
value pairs:
Moon Name (key) Surface Gravity (value)
Io 1.796
Europa 1.314
Ganymede 1.428
Callisto 1.235
The program should also create a dictionary containing the moon names and their orbital
periods (in days). The dictionary should contain the following key-value pairs:
Moon Name (key) Orbital Period (value)
Io 1.769
Europa 3.551
Ganymede 7.154
Callisto 16.689
The program should let the user enter the name of a Galilean moon of Jupiter, then it
should display the moon’s mean radius, surface gravity and orbital period.
""" # function isnt needed then it wont be used
radius = {
    'Io': 1821.6,
    'Europa': 1560.8,
    'Ganymede': 2634.1,
    'Callisto': 2410.3
}
gravity = {
    'Io': 1.796,
    'Europa': 1.314,
    'Ganymede': 1.428,
    'Callisto': 1.235
}
orbit = {
    'Io': 1.769,
    'Europa': 3.551,
    'Ganymede': 7.154,
    'Callisto': 16.689
}

moon = input('Enter the name of a Galilean moon of Jupiter: ')

if moon in radius and moon in gravity and moon in orbit: # an improvement
    print(f"{moon}'s mean radius: {radius[moon]} km")
    print(f"{moon}'s surface gravity: {gravity[moon]} g")
    print(f"{moon}'s orbital period: {orbit[moon]} days")
else:
    print(f"{moon} is an invalid moon name. Please enter a valid Galilean moon of Jupiter.")
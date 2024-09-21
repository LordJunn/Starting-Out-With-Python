"""
In physics, an object that is in motion is said to have kinetic energy. The following formula
can be used to determine a moving object’s kinetic energy:
KE = ½ mv^2
The variables in the formula are as follows: KE is the kinetic energy, m is the object’s mass
in kilograms, and v is the object’s velocity in meters per second.
Write a function named kinetic_energy that accepts an object’s mass (in kilograms)
and velocity (in meters per second) as arguments. The function should return the amount
of kinetic energy that the object has. Write a program that asks the user to enter values
for mass and velocity, then calls the kinetic_energy function to get the object’s kinetic
energy.
"""

def main():
    
    kg = int(input('The object’s mass (in kilograms)? '))
    meter = int(input('The object’s elocity (in meters per second)? '))
    
    energy = kinetic_energy(kg, meter)
    print(f'Kinetic energy = {energy}')

def kinetic_energy(mass, velocity):
    kinetic = (0.5 * (mass * (velocity ** 2)))
    return kinetic

main()
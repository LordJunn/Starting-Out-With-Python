"""
Write a program that asks the user to enter a distance in kilometers, then converts that
distance to miles. The conversion formula is as follows:
Miles = Kilometers x 0.6214
"""
    
def main():
    km = float(input('Enter a distance in kilometers: '))
    miles = kmToMiles(km)
    print(f'{km} in miles is: {miles:.4f}')
    
def kmToMiles(km):
    miles = km * 0.6214
    return miles

main()
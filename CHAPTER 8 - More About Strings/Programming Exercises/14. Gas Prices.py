"""
In the student sample program files for this chapter, you will find a text file named
GasPrices.txt. The file contains the weekly average prices for a gallon of gas in the
United States, beginning on April 5th, 1993, and ending on August 26th, 2013. Figure 8-7
shows an example of the first few lines of the file’s contents:
Each line in the file contains the average price for a gallon of gas on a specific date. Each line
is formatted in the following way:
MM-DD-YYYY:Price
MM is the two-digit month, DD is the two-digit day, and YYYY is the four-digit year. Price is
the average price per gallon of gas on the specified date.
For this assignment, you are to write one or more programs that read the contents of the file
and perform the following calculations:
Average Price Per Year: Calculate the average price of gas per year, for each year in the file.
(The file’s data starts in April of 1993, and it ends in August 2013. Use the data that is pres-
ent for the years 1993 and 2013.)
Average Price Per Month: Calculate the average price for each month in the file.
Highest and Lowest Prices Per Year: For each year in the file, determine the date and amount
for the lowest price, and the highest price.
List of Prices, Lowest to Highest: Generate a text file that lists the dates and prices, sorted
from the lowest price to the highest.
List of Prices, Highest to lowest: Generate a text file that lists the dates and prices, sorted
from the highest price to the lowest.
You can write one program to perform all of these calculations, or you can write different
programs, one for each calculation.
""" # gpt, with modification
def main():
    file = 'GasPrices.txt'
    data = reader(file)
    analyze(data)

def reader(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    
    data = []
    
    for line in lines:
        dateStr, priceStr = line.strip().split(':')
        date = dateStr.strip()
        price = float(priceStr.strip())
        data.append((date, price))
    
    return data

def analyze(data):

    years = []
    months = []
    all = []

    for date, price in data:
        month, day, year = date.split('-')
        year = int(year)
        month = int(month)
        day = int(day) #idk not needed
        
        year_found = False
        for y in years: 
            if y[0] == year:
                y[1].append(price)
                year_found = True
                break
        if not year_found:
            years.append((year, [price])) # means new year

        month_found = False
        for m in months:
            if m[0] == month:
                m[1].append(price)
                month_found = True
                break
        if not month_found:
            months.append((month, [price]))

        all.append((date, price))

    print("Average Price Per Year:")
    for year, prices in years:
        avg = sum(prices) / len(prices)
        print(f"{year}: ${avg:.3f}")

    print("\nAverage Price Per Month:")
    months = rotater(months, 3) # included to make it 1-12 instead of 4-12,1,2,3
    for month, prices in months:
        avg = sum(prices) / len(prices)
        print(f"{month:02d}: ${avg:.3f}")

    # Highest and Lowest Prices Per Year
    print("\nHighest and Lowest Prices Per Year:")
    for year, prices in years:
        dataY = [(date, price) for date, price in data if date.split('-')[2] == str(year)]
        min_price_date = min(dataY, key=lambda x: x[1])
        max_price_date = max(dataY, key=lambda x: x[1])
        print(f"{year}:")
        print(f"  Lowest Price: ${min_price_date[1]:.3f} on {min_price_date[0]}")
        print(f"  Highest Price: ${max_price_date[1]:.3f} on {max_price_date[0]}")
    
    pricesAsc = sorted(all, key=lambda x: x[1]) # x[1] = takes 2nd item of every tuple
    with open('Prices_Low_to_High.txt', 'w') as f:
        for date, price in pricesAsc:
            f.write(f"{date}:{price:.3f}\n")
    
    pricesDes = sorted(all, key=lambda x: x[1], reverse=True) # as above, but in reverse
    with open('Prices_High_to_Low.txt', 'w') as f:
        for date, price in pricesDes:
            f.write(f"{date}:{price:.3f}\n")

def rotater(list, n):
    if len(list) < n:
        raise ValueError("The number of items to rotate exceeds the list length.")
    
    finalN = list[-n:]
    remaining = list[:-n]
    
    rotated = finalN + remaining
    return rotated

main()
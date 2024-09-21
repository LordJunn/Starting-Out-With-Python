"""
A nutritionist who works for a fitness club helps members by evaluating their diets. As part
of her evaluation, she asks members for the number of fat grams and carbohydrate grams
that they consumed in a day. Then, she calculates the number of calories that result from
the fat, using the following formula:
calories from fat = fat grams x 9
Next, she calculates the number of calories that result from the carbohydrates, using the
following formula:
calories from carbs = carb grams x 4
The nutritionist asks you to write a program that will make these calculations.
"""

calorie = 0

def main():
    global calorie
    fat = float(input('Number of fat grams that you consumed in a day? '))
    calorie += calconvert(fat, 9)
    carb = float(input('Number of carbohydrates grams that you consumed in a day? '))
    calorie += calconvert(carb, 4)    
    print(f'Total calories consumed = {calorie}')
    

def calconvert(gram, mult):
    calories = gram * mult
    return calories

main()
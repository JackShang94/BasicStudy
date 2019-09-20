# Calculate a BMI
height = float(input('Enter your height in m: '))
weight = float(input('Enter your weight in kg : '))

bmi = weight / (height * height)

print('Your height is ' + str(height) + 'm')
print('Your weight is ' + str(weight) + 'kg')
print('Your BMI is ' + str(bmi))
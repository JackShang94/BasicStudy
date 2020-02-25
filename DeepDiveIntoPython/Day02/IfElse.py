# Selection Structure
temperature = 40
if temperature > 37.5 :
    print("Tom is having a fever of {:.1f} deg C.".format(temperature))
elif 35 <= temperature <= 37.5:
    print("Tom is healthy.")
else :
    print("Temperature is invalid, please retest.")

# Activity 1
monthlySales = float(input("Enter monthly sales of sales agent:"))
rate = 0
if  monthlySales >= 10000:
    rate = 10
else:
    rate = 5
print("The commission rate is : {}%".format(rate))
print("The commission paid is :${:.2f}".format(monthlySales*rate/100))

# Activity 2
year = int(input("Please enter the year :"))
if year%4 == 0 and year%100 != 0 and year%400 != 0:
    print("{} is a leap year.".format(year))
else:
    print("{} is not a leap year.".format(year))

# Activity 3
temperature = float(input("Enter the outdoor temperature: "))
if temperature <= -5:
    print("Go Bowling.")
elif -5 < temperature <= 0:
    print("Go Skiing.")
elif 0 < temperature <= 20:
    print("Go Jogging.")
elif 20 < temperature <= 25:
    print("Play Tennis; wear white clothes.")
elif 25 < temperature <= 30:
    print("Go Sun-tanning in the park.")
else:
    print("Go Swimming.")
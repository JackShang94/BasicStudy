# Activity 2
def calAverage(x=[1,10,22,44,45,25]):
    Total = 0
    length = len(x)
    for i in range(length):
        Total = Total + x[i]
    
    average = Total/length
    print('Average is {:.2f}'.format(average))

calAverage()

# Activity 3
def calculateBMI(height, weight):   
    bmi = weight / (height * height)
    return bmi

print('Your BMI is : {:.2f}'.format(calculateBMI(1.80,85)))
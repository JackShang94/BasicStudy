# 1)
a,b,c = 4,2,5
result1 = a*c / 3
result2 = b-2
print(result1 >= result2)

print(8 == 8.0)

print (8 == '8.0')

print(True and False or False)

print((True or False) and False)

print(True and (False or not True))

print(not(True and False or True))

print(str(88) + str(False))

print(7/2)

print(7//2)

print(1%7)

# 2)
import math
r = 0
r = float(input("Please enter the sphere's radius: "))
v = 4/3 * math.pi * r**3
print("Volume is", v)

# 3)
f = float(input("Enter temperature in Fahrenheit(F) : "))
c = 5/9 * (f - 32)
k = 5/9 * (f + 459.67)
print("temperature in Celsius : {}".format(round(c,2)))
print("temperature in Kelvin : {}".format(round(k,2)))

# print("temperature in Celsius : {:.2f}".format(c))
# print("temperature in Kelvin : {:.2f}".format(k))

# 4)
num1dollar = int(input("Enter number of 1-dollar coins : "))
num50Cents = int(input("Enter number of 50-cents coins : "))
num20Cents = int(input("Enter number of 20-cents coins : "))
num10Cents = int(input("Enter number of 10-cents coins : "))
num5Cents = int(input("Enter number of 5-cents coins : "))

totalAmount = num1dollar*1 + num50Cents*0.5 + num20Cents*0.2 + num10Cents*0.1 + num5Cents*0.05

print("Total Amount : ${:.2f}".format(totalAmount))

numOfNotes = totalAmount//2
change = totalAmount - numOfNotes*2

print("Number of 2-dollar notes:{}".format(int(numOfNotes)))
print("Amount of change: ${}".format(round(change,2)))

# 5)
dataPerSec = float(input("Enter amount of data(MB) required per seconds:"))
numOfUsers = int(input("Enter number of concurrent users:"))
totalBandwidth = dataPerSec * numOfUsers
print("Total bandwidth required : {} MBps".format(round(totalBandwidth,1)))
print("1Gbps bandwidth sufficient?", totalBandwidth <= 125)

# 6)
expectedHosts = int(input("Enter number of expected hosts:"))
numOfZeros = int(input("Enter number of 0s:"))
usableHosts = 2**numOfZeros -2
print("Number of usable hosts:",usableHosts)
print("Is planned subnet mask suitable?", expectedHosts <= usableHosts)

# 7)
name = input("Enter device name:")
powerRating = float(input("Enter the power rating for device(watts):"))
hoursPerDay = float(input("Enter average number of hours used per day:"))
monthlyCost = powerRating/1000 * hoursPerDay * 30 * 0.2215
print("The cost of monthly usage cost for deskyop computer is $", round(monthlyCost,3))

# 8)
p = float(input("Enter pricipal amount:"))
r = float(input("Enter interest rate(%):"))/100
n = int(input("Number of times insterest is compounded per year:"))
t = int(input("Enter duration(years):"))
a = p*(1+r/n)**(n*t)
print("The investment balance after {0} years is {1}".format(t,a))


x,y,z = 1,4,14
print(x<=1 or y>1 and z<1) # result is true, T or T and F -> T or (T and F) -> T or F -> T

#s1
time, velocity = 5,3
temp = time
time = velocity
velocity = temp
print(time,velocity)
#s2
time, velocity = 5,3
time, velocity = velocity,time
print(time,velocity)
#s3
time, velocity = 5,3
time = time + velocity
velocity = time - velocity
time = time - velocity
print(time,velocity)

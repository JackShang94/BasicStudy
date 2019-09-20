# 2)
myList1 = ['ans', 'wer', 'is', 'of']
myList2 = ['-', '+', '*', '/']
myList3 = ['5', 10, 4, '0', '2']

print("{0}{1} {2} {3} {4} {5} {6} {7}".format(
    myList1[0].capitalize(),
    myList1[1],
    myList1[3],
    myList3[0],
    myList2[1],
    str(myList3[2]),
    myList1[2],
    str(int(myList3[0]) + myList3[2])
    ))

# 3)
applicationList = [
    ['Electric Fan', 70],
    ['Air Con', 1200],
    ['Refrigerator', 200]    
]

count = len(applicationList)

hrsInput = input("Enter hours daily for the above applicances separated by \';\' :")
hrList = hrsInput.split(';')

print("{:<20}{:<20}{:<20}".format('Name','Energy(Watts/Hr)','Daily Hrs used'))

for i in range(count):
    print("{:<20}{:<20}{:<20}".format(applicationList[i][0],applicationList[i][1],hrList[i]))

totalEnergy = 0.0
for i in range(count):
    totalEnergy = totalEnergy + (applicationList[i][1]/1000)*int(hrList[i])

print("Total daily energy consumed(KW): {:.2f}".format(totalEnergy))
print("Total energy cost($): {:.2f}".format(totalEnergy*0.2215))

# 4)
import math
digit = input("Enter a 8-digit binary number:")
value = 0
for i in range(8):
    if digit[i] == '1':
        value += math.pow(2,7-i)
print("The decimal value for {} is {}".format(digit,int(value)))

# 5)
key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
plaintext = input("")
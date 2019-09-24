import os
import math

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path = ROOT_DIR +'\\'

name = 'distance-based-fare.csv'
file = open(path + name)
file.readline() # to skip file header

distanceFareList = []
for line in file:
    line = line.strip('\n')
    rowList = line.split(',')
    distanceFareList.append(rowList)

file.close()

name = 'bus_174.csv'
file = open(path + name)
file.readline() # to skip file header

busStopList = []
for line in file:
    line = line.strip('\n')
    rowList = line.split(',')
    rowList[1] = int(rowList[1]) 
    busStopList.append(rowList)

file.close()

print('{:<20}{:<20}{:<20}'.format('Bus Stop Code','Road','Bus Stop Description'))
for item in busStopList:
    print('{:<20}{:<20}{:<20}'.format(item[1],item[2],item[3]))

while True:
    distance = 0
    startCode = int(input('Enter boarding busstop(or -1 to exit): '))
    if startCode == -1:
        print('Bye-bye!')
        break
    endCode = int(input('Enter alighting busstop: '))
    for item in busStopList:
        if item[1] == startCode:
            startLocation = float(item[0])
        if item[1] == endCode:
            endLocation = float(item[0])
    distance = abs(startLocation - endLocation)
    print('Distance travelled: {:.1f}km'.format(distance))

    fareToPay = 0
    if distance <= float(distanceFareList[0][0]):
        fareToPay = float(distanceFareList[0][1]/100)
    elif distance >= float(distanceFareList[-1][0]):
        fareToPay = float(distanceFareList[-1][1]/100)
    else:
        for i in range(len(distanceFareList)):
            if distance <float(distanceFareList[i][0]):
                fareToPay = float(distanceFareList[i-1][1])/100
                break
    print('Fare to pay: ${:.2f}'.format(fareToPay))
    print('Estimated duration: {}mins'.format(math.ceil(distance*4)))
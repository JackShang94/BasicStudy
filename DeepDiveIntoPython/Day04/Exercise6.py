import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path = ROOT_DIR +'\\'
name = 'median-resale-prices-for-registered-applications-by-town-and-flat-type.csv'
file = open(path + name)
file.readline() # to skip file header

readList = []
for line in file:
    line = line.strip('\n')
    rowList= line.split(',')
    readList.append(rowList)

file.close()

print('Part A')
totalPrice = 0
counter = 0
for item in readList:
    if '2017' in item[0] and '4-room' in item[2]:
        if item[3].isnumeric():
            totalPrice += float(item[3])
            counter += 1
average = totalPrice/counter
print('The average price for the 4-room flat type is {:.2f}'.format(average))

print('Part B')
for item in readList:
    if '2017' in item[0] and '4-room' in item[2]:
        if item[3].isnumeric():
           if float(item[3]) > average:
               print('{:<20}{:<20}{:<20}'.format(item[0],item[1],item[3]))

print('Part C')
fiveRoomList = []
for item in readList:
    if '2017' in item[0] and '5-room' in item[2]:
        if item[3].isnumeric():
            fiveRoomList.append(item)

highestFiveRoom = max(fiveRoomList, key = lambda x:x[3])
print('The town with the highest resale price for the 5-room flat type in 2017 is {} with the price of {}'.format(highestFiveRoom[1],highestFiveRoom[3]))

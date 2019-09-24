timeList = []
while True:
    time = float(input('Enter the time: '))
    if time <0 or time >23.59:
        break
    else:
        timeList.append(time)

timeList.sort()

uniqueVisit = 1
for i in range(len(timeList)):
    if i < len(timeList) -1:
        if timeList[i+1] - timeList[i] > 1:
            uniqueVisit += 1

print('Time of visit: {}'.format(timeList))

print('No. of unique visits: ', uniqueVisit)
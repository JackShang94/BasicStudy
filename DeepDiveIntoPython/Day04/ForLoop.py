range(9) # 0~8
range(2,9) # 2~8
range(2,10,2) # 2,4,6,8
range(-2,-10,-2) # -2,-4,-6,-8
# Activity 1
measurement = [20.1]
total = 0

## way1
for item in measurement:
    total = total + item
## way 2
for i in range(0,len(measurement)):
    total += measurement[i]

average = total/len(measurement)

# Activity 2
for item in measurement:
    if item > 25 :
        print('Reading exceeded 25C')
        break

# Activity 3
highest = 0
for item in measurement:
    if highest > item:
        continue
    highest = item
count  = 1 
sum = 0
while count <= 5:
    sum += count
    print(count,end = '')
    count ++
else:
    print('End.')

# Activity 2
def calAveTemp(temp_list):
    length = len(temp_list)
    counter = 0
    total = 0
    while counter < length:
        total += temp_list[counter]
        counter += 1
    else:
        average = total/length

    return average

list1 = [20.5,30.5,12.3,45.6] 
print('Average temperature is : {:.2f}'.format(calAveTemp(list1)))

# Activity 3
inputNumber = int(input('Please enter a number :'))
counter = 1
while counter <= 10:
    print('{} X {} = {}'.format(inputNumber,counter,inputNumber*counter))
    counter += 1
# control flow
## break
while True:
    word = input('Please enter a word (anything else to quit): ')
    if word.isalpha():
        print('The word was ' + word)
    else:
        print('Exiting...')
        break
## continue
while True:
    word = input('Please enter a word (anything else to quit): ')
    if word.isalpha():
        print('The word was ' + word)
    else:
        print('You did not enter a word, Please try again.')
        continue
    print('Loop again!')


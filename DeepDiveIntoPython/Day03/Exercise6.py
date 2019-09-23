inputWord = ''
inputList = []
while inputWord != 'exit':
    inputWord = input('Enter a number(\'exit\' to quit): ')
    if inputWord.isnumeric():
        inputList.append(int(inputWord))
else:
    print('Numbers entered are')
    print(inputList)
    print('Count: ', len(inputList))
    print('Sum: ', sum(inputList))
    print('Lowest: ', min(inputList))
    print('Highest: ', max(inputList))
    print('Average: {:.2f}'.format(sum(inputList)/len(inputList)))
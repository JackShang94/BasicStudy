bankList = ['DBS','UOB','OCBC']
friendList = ['Peter',['John','Mary'],'David']
matrix = [[1,2,3],[4,5,6],[7,8,9]]
emptyList = []
mixedList = ['Peter',100,23.5,[10,20]]

# Activity 2
markList = [1,2,3,4,5,6,7,8,9,10]
print(markList[0])

sum = markList[-2] + markList[-1]
print(sum)

markList[1] = markList[1]*2
print(markList[1])

letters = ['a','b']
letters.append('c')
letters.extend(letters)
letters.insert(3,'z')
print(letters)
letters.remove('c')
print(letters)
letters.pop(2)
print(letters)
letters.pop()
print(letters)
for each in letters :
    print(each)
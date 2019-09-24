path = 'C:\\Users\\P1315917\\Desktop\\'
file = open(path + 'test.txt','r')
for line in file:
    print(line, end="")
file.close()

file = open(path + 'test.txt','a')
file.write('\nHello again.')
file.close()

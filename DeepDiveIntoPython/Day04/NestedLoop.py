for i in range(3):
    for j in range(7):
        print('=', end =' ') # print默认是打印一行，结尾加换行。end=' '意思是末尾不换行，加空格。
    print('\n')

for i in range(5):
    for j in range(i+1):
        print(j+1, end = ' ')
    print('\n')



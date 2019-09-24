for i in range(3):
    for j in range(7):
        print('=', end =' ') # print默认是打印一行，结尾加换行。end=' '意思是末尾不换行，加空格。
    print('\n')

for i in range(5):
    for j in range(i+1):
        print(j+1, end = ' ')
    print('\n')

# Activity 2
print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format('S','M','T','W','Th','F','S'))
counter = 1
while counter <= 30:
    if counter % 7 == 1 and counter != 1:
        print('\n', end="")
        print('{:<10}'.format(counter), end='')
    else:
        print('{:<10}'.format(counter), end='')
    counter += 1

print('\n', end="")

print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format('S','M','T','W','Th','F','S'))
d = 1
while d <= 30:
    for i in range(7):
        if d>30:
            break
        print('{:<10}'.format(d), end='')
        d += 1
    print('\n', end="")

# Activity 3
menu =['reboot system now', 'apply sdcard:update.zip', 'wipe data/factory reset', '+++++Go Back+++++']
while True:
    print('Onix Recovery v3.0.1.1')
    print()
    for i in range(len(menu)):
        print('[{}]{}'.format(i+1, menu[i]))
    print('--------------------------------------------')
    selection = int(input())

    if selection == 4:
        break
    else:
        print(menu[selection -1])
        print()
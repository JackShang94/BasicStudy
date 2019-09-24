import math
import random

answer = random.randrange(100)
print(answer)
print('Welcome to Number Guessing Game')
inputNum = int(input('Try 1 : Enter a number between 1 and 100 (or -1 to end): '))

counter = 1
while inputNum != answer:
    if inputNum == -1:
        print('Game Ends.')
        break
    elif counter == 5:
        print('Game Over. The correct answer is: ',answer)
        break
    else:
        counter += 1
        inputNum = int(input('Try {}: Guess again, enter a number between 1 and 100 (or -1 to end): '.format(counter)))

if inputNum == answer:
    print('Bingo, you\'ve got it right! ')

print('\nBye-bye!')



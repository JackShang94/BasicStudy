plate = input("What is the number plate:")
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
last_char = 'AZYXUTSRPMLKJHGEDCB'
length = len(plate)
plateLetter = []

if plate[2].isalpha():
    plateLetter.append(plate[1:])
elif plate[1].isalpha():
    if length == 5:
        plateLetter.append(plate)

firstLetter = (letters.find(plate[1]) + 1) * 9
secondLetter = (letters.find(plate[2]) + 1) * 4
firstNum = int(plate[3]) * 5
secondNum = int(plate[4]) * 4
thirdNum = int(plate[5]) * 3
fourthNum = int(plate[6]) * 2

remainder = (firstLetter + secondLetter + firstNum + secondNum + thirdNum + fourthNum) % 19
print('The checksum is {}'.format(last_char[remainder]))
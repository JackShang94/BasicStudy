numToConvert = input('Enter a number to convert: ')
morseCode = ['-----','.----','..---','...--','....-','.....','-....','--...','---..','----.']
output = ''
for i in numToConvert:
    digit = int(i)
    output = output + morseCode[digit] +'   '

print('The morse code for {} is {}'.format(numToConvert, output))

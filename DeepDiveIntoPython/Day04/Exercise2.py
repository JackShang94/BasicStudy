morseCode = ['-----','.----','..---','...--','....-','.....','-....','--...','---..','----.']
while True:
    numToConvert = input('Enter a number to convert(or -1 to exit): ')
    if numToConvert == '-1':
        print('Bye-bye!')
        break
    output = ''
    for i in numToConvert:
        digit = int(i)
        output = output + morseCode[digit] +'   '

    print('The morse code for {} is {}'.format(numToConvert, output))

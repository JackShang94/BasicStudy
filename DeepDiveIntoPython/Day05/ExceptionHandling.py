import sys

try:
    denominator = int(input('Enter a denominator: '))
    result = 5/ denominator
except ZeroDivisionError:
    print('Invaild input, non zero integer input expected.')
except ValueError:
    print('Invaild input, integer input expected.')
except:
    print('Unexpected error:', sys.exc_info()[0])
finally:
    print('Program End')
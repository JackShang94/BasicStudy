# string formatting
## method 1
text = 'Hello'
text2 = 'World'
print('%s' % text)
print('...%s...%s' % (text,text2))

## method 2 
text = 'Hello'
print(f'...{text}...')

## method 3
text = 'Hello'
print('...{:s}...'.format(text))

print('{}'.format(text))

print('{},{}'.format('one','two','three')) ## different parameter

print('{} {}'.format(1,2))

print('{},{}'.format('one','two','three'))

print('{1},{0}'.format('one','two')) ## rearrangement

print('{2} {3} {5} {1} {4} {6}'.format('See','how', 'the', 'words', 'are', 'mixed', 'up'))

print('{:d}'.format(23)) ## integers

print('{:f}'.format(3.142)) ## float

print('{:.2f}'.format(3.142)) ## float

print('{:10}'.format('Hi')) ## padding left

print('{:>10}'.format('Hi')) ## padding right

print('{:5}'.format('1234567890')) ## no paddings

print('{:_<10}'.format('Hi')) ## under line

print('{:^10}'.format('Hi')) ## specify center

print('{:*^10}'.format('Hi')) ## specify center

# Activity 1
## way 1
print('{:10}{:10}{:10}'.format('a','b','a to power of b'))
print('{:<10}{:<10}{:<10}'.format(1,2,1**2))
print('{:<10}{:<10}{:<10}'.format(2,3,2**3))
print('{:<10}{:<10}{:<10}'.format(3,4,3**4))
print('{:<10}{:<10}{:<10}'.format(4,5,4**5))
print('{:<10}{:<10}{:<10}'.format(5,6,5**6))
## way 2
print('{:10}{:10}{:10}'.format('a','b','a to power of b'))
for value in range(1,6):
    print('{:<10}{:<10}{:<10}'.format(value,value+1,value**(value+1)))


first = 'Learning Strings'
print(first[3:]) # ing Strings 
print(first[3:6]) # rni
print(first[3:9]) # rning
print(first[3:9:2]) # rig
print(first[3:9:-1]) # ''


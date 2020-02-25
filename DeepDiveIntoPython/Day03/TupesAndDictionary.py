#Tuple
tupl1 = (1,2,3)
tupl1[1]

#Dictionary
phoneBook = {'Hafiz':'91238980',1:'b'} # key can be any type
print(phoneBook)
# add new key value pair
phoneBook[2] = 'new'
print(phoneBook)
# replacing value
phoneBook[1] = 'a'
print(phoneBook)
# removing item
phoneBook
phoneBook.pop(1)
print(phoneBook)

phoneBook.pop(3,'Not found')
# basic functions
len(phoneBook)
print(2 in phoneBook)

phoneBook.get(2)

phoneBook.get(2,'Not find')

# Activity 1
phoneBook.clear()
phoneBook = {'Jack':'91238980','Lucy':'12345678','Bob':'87654321','Danny':'22222222'}
for name in phoneBook :
    print(name,'->', phoneBook[name]) 
    
for key,value in phoneBook.items():
    print(key,value)
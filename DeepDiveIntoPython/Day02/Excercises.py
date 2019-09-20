# 2)
myList1 = ['ans', 'wer', 'is', 'of']
myList2 = ['-', '+', '*', '/']
myList3 = ['5', 10, 4, '0', '2']

print("{0}{1} {2} {3} {4} {5} {6} {7}".format(
    myList1[0].capitalize(),
    myList1[1],
    myList1[3],
    myList3[0],
    myList2[1],
    str(myList3[2]),
    myList1[2],
    str(int(myList3[0]) + myList3[2])
    ))




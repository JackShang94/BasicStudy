biddingList = []
quota = int(input('Enter available quota: '))
while True:
    bid = int(input('Enter bid [-1 to end]: '))
    if bid == -1:
        break
    else:
        biddingList.append(bid)

biddingList.sort(reverse = True)

if quota == 0 or len(biddingList) == 0:
    print('The quota or bidding can\'t be empty.')
elif quota >= len(biddingList): # quota more than/ equal to bid
    coePrice = biddingList[-1]
    print('The COE price is ${}'.format(coePrice))
    print('The successful bids are:')
    for each in biddingList:
        print('$',each)
elif biddingList[quota -1] > biddingList[quota]: # quota less than bid and last two not same
    coePrice = biddingList[quota -1]
    print('The COE price is ${}'.format(coePrice))
    print('The successful bids are:')
    for i in range(quota):
        print('$',biddingList[i])
else: # quota less than bid and last two are same
    for i in range(quota):
        if biddingList[i] > biddingList[i +1]: # check from top, when the price is same
            continue
        else:
            coePrice = biddingList[i -1] # get the last not same value as COE
            print('The COE price is ${}'.format(coePrice))
            print('The successful bids are:')
            for x in range(i):
                print('$',biddingList[x])
            break # End loop

# test case: quota = 5, biddings: 100, 88, 70, 70, 70, 70, 41
# Expected results = 100, 88.
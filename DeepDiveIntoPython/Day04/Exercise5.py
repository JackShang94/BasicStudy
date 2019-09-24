import math
def calculateTotalCost(plan, monthlyData, monthlyTalkTime):
    phoneCost, monthlyCost, localData, talkTime = plan[1],plan[2],plan[3],plan[4]
    chargeableData = 0
    chargeableTalkTime = 0
    if monthlyData > localData:
        chargeableData = math.ceil(monthlyData - localData)*10.7
        if chargeableData > 188:
            chargeableData = 188

    if monthlyTalkTime > talkTime:
        chargeableTalkTime = math.ceil(monthlyTalkTime - talkTime)*0.1605

    totalCost = phoneCost + (monthlyCost + chargeableData + chargeableTalkTime)*24
    return totalCost

while True:
    monthlyData = float(input('Average monthly local data(GB): '))
    monthlyTalkTime = float(input('Average monthly talk time(mins): '))
    
    planList = [['A',1248,27.90,0.1,100],
                ['B',1114,42.90,2,200],
                ['C',882,68.90,3,10000],
                ['D',641,95.90,6,10000],
                ['E',0,198.90,12,10000]]
    
    print('{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}'.format('Plan', 'Cost of phone', 'Monthly Cost', 'Local Dat(GB)', 'Talk time(mins)', 'Total Cost'))
    for item in planList:
         print('{:<20}{:<20}{:<20}{:<20}{:<20}${:<20.2f}'.format(item[0], item[1], item[2], item[3], item[4], 
                calculateTotalCost(item, monthlyData, monthlyTalkTime)))


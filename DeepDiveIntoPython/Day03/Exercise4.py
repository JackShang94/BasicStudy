# 4)
from datetime import datetime
_today = '13/5/2018'
dateFormat = '%d/%m/%Y'

def getDaysBeforeDeadline(taskDate):
    convertedDate = datetime.strptime(taskDate,dateFormat)
    today = datetime.strptime(_today,dateFormat) 
    daysBeforeDeadling = (convertedDate - today).days
    
    return daysBeforeDeadling

initialList = [['Pay Bills', '20/5/2018'],
                    ['Submit Proposal', '19/5/2018'],
                    ['Onboard Customer', '21/5/2018']]

for i in initialList:
    taskDay = i[1]
    days = getDaysBeforeDeadline(taskDay)
    i.append(days)

initialList.sort(key= lambda x:x[2])
print("{:<20}{:<20}{:<20}".format('Task','Due Date','Days Until'))
for i in initialList:
    print("{:<20}{:<20}{:<20}".format(i[0],i[1],i[2]))


# 2)
from datetime import datetime

def getDateDifference(dateTime):
    date_format = '%d/%m/%Y'
    converted_date = datetime.strptime(dateTime,date_format)
    today = datetime.today()
    difference = (today - converted_date).days
    return difference

def check_fines(overdue_titile_list, due_date_list, lost_damaged_list):
    totalOverDueFine = 0
    totalLostFine = 0

    overDueBookNum = len(overdue_titile_list)    
    counter = 0
    overDueFeePerDay = 0.15
    while counter < overDueBookNum:
        totalOverDueFine += getDateDifference(due_date_list[counter])*overDueFeePerDay
        counter += 1
    
    lostBookNum = len(lost_damaged_list)
    counter = 0
    lostFeePerBook = 7.15
    while counter < lostBookNum:
        totalLostFine += lostFeePerBook + lost_damaged_list[counter][1]
        counter += 1

    return totalOverDueFine,totalLostFine

initialList = [
        ['Beginning Python', 'Stay Happy'],
        ['19/9/2018', '18/9/2018'],
        [
            ['A Lost Book', 15],
            ['Another Lost Book', 20]
        ]]

result = check_fines(initialList[0],initialList[1],initialList[2])

print('The total overdue fine is: ${:.2f}'.format(result[0]))
print('The total lost/damaged fine is: ${:.2f}'.format(result[1]))
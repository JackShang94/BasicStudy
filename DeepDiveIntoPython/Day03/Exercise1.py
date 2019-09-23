# 1)
def calculate_average_marks(markList):
    firstCourse = markList[1].split(';')
    secondCourse = markList[2].split(';')
    firstMark = float(firstCourse[0])*(float(firstCourse[1])/100)
    secondMark = float(secondCourse[0])*(float(secondCourse[1])/100)
    finalMark = firstMark + secondMark
    return finalMark

initial = 'Alan Ang#60;60#90;40/Bobby Boey#80;50#26;50'
studentList = initial.split('/')
firstMarkList = studentList[0].split('#')
secondMarkList = studentList[1].split('#')
print('{:<30}{:<20}{:<20}{:<20}'.format('Name','First','Second','Mark'))
print('{:<30}{:<20}{:<20}{:<20.2f}'.format(firstMarkList[0],firstMarkList[1]+"%",firstMarkList[2]+"%",calculate_average_marks(firstMarkList)))
print('{:<30}{:<20}{:<20}{:<20.2f}'.format(secondMarkList[0],secondMarkList[1]+"%",secondMarkList[2]+"%",calculate_average_marks(secondMarkList)))

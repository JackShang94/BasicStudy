# some build in functions
list1 = [1,2,3]
sum(list1)
pow(2,3)
a = -4
abs(a)
divmod(7,3)
max(list1)
min(list1)

b = 1.414435345
round(b,1)

sorted(list1,reverse=True) # a lot of things can learn about sort
# math functions
import math
math.pi
math.pow(2,2)

# date time functions
from datetime import date
today = date.today()
print(today)
date_format = '%d/%m/%Y'
converted_date = date.strptime('19/9/2018',date_format)
print(converted_date)

my_birthday = date(1994,8,3)
time_to_birthday = abs(my_birthday - today)

import urllib.request
import re
url = "http://checkip.dyndns.org"
request = urllib.request.urlopen(url).read().decode('utf-8')
theIP = re.findall(r'(?:\d{1,3}\.)+(?:\d{1,3})',request)

print('Your IP Address is ',theIP[0])
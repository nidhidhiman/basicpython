#Time Function
import time
print(time.time()) #time()is used to count the number of seconds
print(time.gmtime()) #
print(time.asctime())
print(time.ctime())

import datetime
from datetime import date
print(datetime.MINYEAR)
print(datetime.MAXYEAR)
print(date.today())
print(datetime.date(1996,12,9))
print(date.min)
print(date.max)

import math
print(math.pi)
print(math.pow(5,2))
print(math.nan)

import os
print(os.name)
print(os.getcwd())
print (os.error)

import time
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)


import datetime
a = '2010-01-31'
d = datetime.datetime.strptime(a, "%Y-%m-%d")
print("The month is",d.month)

#Or

import datetime
d = datetime.date.today()
print(d.month)

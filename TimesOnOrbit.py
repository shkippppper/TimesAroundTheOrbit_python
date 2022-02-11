#shkipper

import pytz 
from datetime import datetime


startNumber = 0

for i in pytz.all_timezones:
    startNumber +=1
    currentTimezone = pytz.all_timezones[startNumber]
    currentTimezoneName = pytz.timezone(currentTimezone)
    currentTimezoneTime = datetime.now(currentTimezoneName)
    lineToProcess = currentTimezoneTime.strftime("DATE %d-%m-%y, TIME %H:%M:%S / %Z")
    lineToPrint = currentTimezone, lineToProcess
    print(lineToPrint)

    if currentTimezone =="Zulu" :
        break
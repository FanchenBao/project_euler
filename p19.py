#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

''' define 1 = Mon, 2 = Tue, 3 = Wed, 4 = Thu, 5 = Fri, 6 = Sat, 0 = Sun.
We know 1/1/1900 was 1, so 12/1/1900 was 6.
'''

def dayOfWeek(preMonthDays, preFirstDay):
    curFirstDay = (preMonthDays % 7 + preFirstDay) % 7
    return curFirstDay

count = 0
firstOfMonth = [7] * 13
firstOfMonth[12] = 6 # set to Dec 1st, 1900
monthDays = [29, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # first element for leap year Feb

for year in range(1901, 2001):
    for month in range(1, 13):
        preMonth = 12 if month == 1 else month - 1

        if month == 3 and ((not year % 4) or (not year % 400)):
            firstOfMonth[month] = dayOfWeek(monthDays[0], firstOfMonth[preMonth])
        
        firstOfMonth[month] = dayOfWeek(monthDays[preMonth], firstOfMonth[preMonth])
    
    count += firstOfMonth.count(0)

print(count)


# runtime = 



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

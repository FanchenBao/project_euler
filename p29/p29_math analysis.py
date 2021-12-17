#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
All non-powered numbers have unique distinct powers. All powered numbers have to consider repetition against lower powers.

Numbers to consider
Sqaure: 4, 9, 25, 36, 49, 100
Cube: 8, 27, 
4th power: 16, 81,
5th power: 32
6th power: 64

The power numbers need to be analyzed separatedly to assure no repetition
'''
result = 87 * 99 # count non-power numbers

hashMap = [0] * (6 * 100 + 1) # biggest power is 600. The check starts from 101 and up

nonRepeats = [] # record the number of non-repeat item for square, cube, 4th, 5th, and 6th power
for power in range(2, 7):
    i = 100 // power + 1 # starting point
    count = 0
    while(i <= 100):
        if not hashMap[power * i]:
            count += 1
            hashMap[power * i] = 1
        i += 1
    nonRepeats.append(count)

result += (6 * nonRepeats[0] + 2 * nonRepeats[1] + 2 * nonRepeats[2] + nonRepeats[3] + nonRepeats[4])

print(result)




# runtime = not relevant



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

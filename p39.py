#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
From mathematical analysis, we have

a^2 + b^2 = c^2
a + b + c = p        --> a = p/2 * (p - 2b)/(p - b)

Since also a + c > b, thus p - b > b, thus b < p/2
Thus looping b from 1 to p/2, calculating a and recording only the whole number a would give all solutions for a given p.

Looping p from 12 to 1000 with only even numbers gives the number of solutions for each p.

NOTE: the formula for a CANNOT be written as p/2 * (1 - b/(p - b)). 
For whatever float precision reason, this formula cannot reconcile some whole number in float form. 
e.g. (60*(1 - 2/3)).is_integer returns False, while it actually equals 20. But (60*(1/3)).is_integer returns True
'''

def findTriangle(ansDict, p):
    count = 0
    for b in range(1, p // 2):
        a = p / 2 * ((p - 2 * b) / (p - b))
        intA = int(a)
        if (a == intA):
            abPair = tuple(sorted((intA, b)))
            if abPair not in ansDict:
                ansDict[abPair] = p - intA - b
                count += 1
    return count

ansDict = {}
maxCount = 0
for p in range(12, 1001, 2):
    currentCount = findTriangle(ansDict, p)
    if currentCount > maxCount:
        ansP = p
        maxCount = currentCount

print(ansP)






# runtime = 0.06 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

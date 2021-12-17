#! /usr/bin/env python3
import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Author: Fanchen Bao
Date: 10/07/2018

Project Euler: Problem 64

Solution: 
	With understanding of how deep fraction works, it is easy to get a, b, and c for each level.
suppose after the previous level we have a + (sqrt(n) - b) / c, then in the next level:
    c = (n - b**2) // c
    a = int((sqrt(n) + b) / c) # this is the KEY. Each level is to convert a fraction into an integer plus a smaller-than-one fraction
    b = a * c - b
Then all we need to do is check when the pair (b, c) repeats itself.
'''
from math import sqrt

# period = [] # record the repeated period
coeffDict = {} # record all coefficients that have occurred, and whether they can produce valid outcome (true) or not (false)
count = 0

for n in range(2, 10001):
    b = int(sqrt(n))
    if b**2 != n: # skip perfect squares
        c = 1
        # period.clear()
        coeffDict.clear()
        pLen = 0
        while True:
            coeffDict[(b, c)] = True # record previous coefficient pair

            # calculate current coefficients
            c = (n - b**2) // c
            a = int((sqrt(n) + b) / c) # this is the KEY. Each level is to convert a fraction into an integer plus a smaller-than-one fraction
            b = a * c - b
            # period.append(a)
            pLen += 1
            if (b, c) in coeffDict:
                break
        # print("sqrt({})=[{}; {}], period = {}".format(n, int(sqrt(n)), period, len(period)))
        if pLen % 2:
            count += 1

print(count)

# runtime = 0.4 s


print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

#! /usr/bin/env python3
import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Author: Fanchen Bao
Date: 10/04/2018

Project Euler: Problem 63

Solution: 
	Find the range of base whose n-power is n-digit long. n goes from 1 until such range doesn't exist anymore.
Note that for whatever n, the largest base is always 9. So basically it is to find at which n, 9^n has n + 1 digit
'''

from math import log10

n = 1
sigma = 0
i = 1 # the base to try
while int(n * log10(9) + 1) == n: # do not calculate the power first. do n * log(base) instead of log(base^n)
    while i < 10: # base increases each iteration of n. If i^n has fewer digits than n, then i^(n + 1) definitely has fewer digits than n + 1
        if int(n * log10(i) + 1) == n:
            sigma += 9 - i + 1
            break
        i += 1
    n += 1

print(sigma)
# runtime = 0.0006 s


print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

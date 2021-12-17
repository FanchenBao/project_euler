#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

import math

''' 
Brute force, with optimization of finding divisors. 
Optimization 1: only find divisor until sqrt(n), because there is always another cooresponding divisor larger than sqrt(n)
Optimization 2: find only odd number divisor for odd number
'''

def findDivisor(n):
    divisors = [1]
    sqrtRoot = math.sqrt(n)
    if sqrtRoot == int(sqrtRoot) and sqrtRoot not in divisors:
        divisors.append(sqrtRoot)
    if n % 2: # odd number
        for i in range(3, int(sqrtRoot), 2):
            if not (n % i):
                divisors.append(i)
                divisors.append(n // i)
    else: # even number
        for i in range(2, int(sqrtRoot)):
            if not (n % i):
                divisors.append(i)
                divisors.append(n // i)
    return divisors

amiNums = []
for i in range(1, 10000):
    if i not in amiNums:
        a = i
        b = sum(findDivisor(i))
        if (a == sum(findDivisor(b))) and a != b:
            amiNums.append(i)

print(sum(amiNums))
print(amiNums)


# runtime = 0.1 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
from math import sqrt

s = time()
def isPrime(n):
    i = 3
    while(i < (sqrt(n) + 1)): # using list is the main cause of inefficiency. So a for loop using range() is much slower than while loop without any list
        if not (n % i):
            return 0
        i += 2
    return 1

i = 3
length = 1
while(length < 10001):
    if isPrime(i):
        length += 1
    i += 2

print(i - 2)
print("Time: {}".format(time() - s))



logging.debug('End of program.\n\n\n')

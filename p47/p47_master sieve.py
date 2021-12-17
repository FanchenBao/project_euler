#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
This is a brilliant way to modify the Eratosthenes' sieve to record the number of unique prime factors each number.
Credit to Brian
'''

n = 1000000
targetValue = 4
count = 0

primeFactors = [0] * n

for i in range(2, n):
    if not primeFactors[i]: # i is prime
        count = 0
        j = 2
        while (i * j < n):
            primeFactors[i * j] += 1
            j += 1
    else:
        if primeFactors[i] == targetValue:
            count += 1
            if count == targetValue:
                print(i - (targetValue - 1))
                break
        else:
            count = 0


# runtime = 1.3 s

print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

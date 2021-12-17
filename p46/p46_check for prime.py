#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Loop through odd composite, check each double square to see whether the difference is a prime.
'''

def primeSieve(n):
    rawPrimes = [1] * (n + 1)
    rawPrimes[0] = 0
    rawPrimes[1] = 0
    for i in range(4, n, 2):
        rawPrimes[i] = 0
    for i in range(3, n, 2):
        j = i
        while(i * j < n):
            rawPrimes[i * j] = 0
            j += 2
    return rawPrimes

n = 10000
rawPrimes = primeSieve(n)

odd = 9
while(1):
    if not rawPrimes[odd]: # odd composite
        root = 1
        found = 1
        while (2 * root**2 < odd):
            if rawPrimes[odd - 2 * root**2]:
                # print("{} = {} + 2 x {}^2".format(odd, odd - 2 * root**2, root))
                found = 0
                break
            root += 1
        if found:
            print("{} cannot be written as the sum of a prime and twice a square.".format(odd))
            break
    odd += 2

# runtime = 0.01 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

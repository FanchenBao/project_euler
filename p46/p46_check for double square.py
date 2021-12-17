#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Loop through odd composite, check each prime number to see whether the difference is a double square.
'''

from math import sqrt

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

def getPrimeList(n, rawPrimes):
    primeList = []
    for i in range(n):
        if rawPrimes[i]:
            primeList.append(i)
    return primeList[1:] # no need to include 2 in primeList

n = 10000
rawPrimes = primeSieve(n)
primeList = getPrimeList(n, rawPrimes)

odd = 9
found = 0
while(not found):
    if not rawPrimes[odd]: # odd composite
        for prime in primeList:
            if prime < odd:
                root = sqrt((odd - prime) // 2)
                if root == int(root):
                    # print("{} = {} + 2 x {}^2".format(odd, prime, int(root)))
                    break
            else:
                print("{} cannot be written as the sum of a prime and twice a square.".format(odd))
                found = 1
                break
    odd += 2

# runtime = 0.09 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

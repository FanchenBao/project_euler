#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from math import log, sqrt

def isPrime(n, primeNumbers):
    for pNum in primeNumbers:
        if pNum < sqrt(n) + 1: # plus one to deal with squares of prime number
            if not (n % pNum):
                return 0
    primeNumbers.append(n)
    return 1

product = 2
primeNumbers = [2]
maxVal = 20 # change this value for other application
for i in range(3, maxVal + 1):
    if isPrime(i, primeNumbers): # create prime number list until 20
        product *= i # product of all prime numbers

for pNum in primeNumbers:
    extraFactor = int(log(maxVal, pNum)) # deal with extra factors from powers of prime number (e.g. 4, 8, 9, 16). 
    if extraFactor > 1:
        product *= pNum ** (extraFactor - 1)
    else:
        break

print(product)


logging.debug('End of program.\n\n\n')

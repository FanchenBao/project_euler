#! /usr/bin/env python3
import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Author: Fanchen Bao
Date: 11/04/2018

Project Euler: Problem 70

Solution: 
    The Euler Totient Function states that phi = n(1-1/p1)(1-1/p2)...(1-1/pr), in which n = p1*p2*...*pr
Thus, n/phi = p1*p2*...*pr / ((p1-1)(p2-1)...(pr-1)). (see http://mathworld.wolfram.com/TotientFunction.html)
    In order for n/phi to reach min, there must be as few prime factors as possible (the more prime factors,
the more p/(p-1) item to multiply. And since this item is larger than one, it means n/phi gets bigger if n 
has too many prime factors). Therefore, n should have only one factor to minimize n/phi, or in other words, 
n should be prime itself. However, if n is prime, phi = n - 1, which can never be a digit-permutation of n. 
Consequently, the next best option is to let n have two prime factors.
    Next thing to note is that for item p/(p-1), it gets smaller as p gets bigger. Thus, to minimize n/phi
where n has only two prime factors, the prime factors must be as big as possible. This indicates that n must
satisfy the following expression:

n = p1 * p2, where p1 and p2 are big prime themselves.

    Thus, we create a prime list consisting of all primes from 1000 to 100000 (the biggest p1 and p2 can be
with their product smaller than 10^7). Then, we try all combinations of the 4-digit prime pairs (p1, p2) that
satisfy two requirement: 1. p1 * p2 < 10^7 and 2. n = p1 * p2 and phi = (p1 - 1)(p2 - 1) are digit-permutation.
The pair that produce the smallest n/phi is the answer.

'''
from math import sqrt

def isPermutation(n, m):
    ''' determine whether m is a digit-permutation of n'''
    return sorted(list(str(n))) == sorted(list(str(m)))

def primeSieve(lowerLimit, upperLimit, primeList):
    ''' create a primeList up to upperlimit'''
    rawPrime = [1] * upperLimit
    rawPrime[0] = 0
    rawPrime[1] = 0
    for i in range(4, upperLimit, 2):
        rawPrime[i] = 0
    for i in range(3, int(sqrt(upperLimit)), 2):
        j = i
        while (j * i < upperLimit):
            rawPrime[i * j] = 0
            j += 2

    for i in range(lowerLimit, upperLimit):
        if rawPrime[i]:
            primeList.append(i)


# driver
primeList = []
primeSieve(1000, 10000, primeList)
minRatio = 10
for i, p1 in enumerate(primeList): # try all two-prime combinations and find the pair that makes n/phi the smallest
    for p2 in primeList[i+1:]:
        n = p1 * p2
        phi = (p1 - 1) * (p2 - 1)
        if n < 10000000:
            if isPermutation(n, phi) and n / phi < minRatio:
                minRatio = n / phi
                ans = (n, phi)
        else:
            break

print(ans)

# runtime = 0.4 s


print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

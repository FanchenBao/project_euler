#! /usr/bin/env python3
import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Author: Fanchen Bao
Date: 11/24/2018

Project Euler: Problem 72

Solution: 
    Use totient function phi() to calculate the number of relative primes to each denominator from 2 to 1 million.
Add all phi() values up and we have the answer.
    In order to calculate phi(), we need to find the prime factors of each composite number.
'''
from math import sqrt

def primeSieve(upperLimit, primeList):
    ''' create a rawPrime up to upperLimit, and also populate the primeList '''
    rawPrime = [1] * upperLimit
    rawPrime[0] = 0
    rawPrime[1] = 0
    for i in range(4, upperLimit, 2):
        rawPrime[i] = 0
    for i in range(3, int(sqrt(upperLimit)) + 1, 2):
        j = i
        while (j * i < upperLimit):
            rawPrime[i * j] = 0
            j += 2
    for i in range(upperLimit):
        if rawPrime[i]:
            primeList.append(i)
    return rawPrime
    

def findPrimeFactor(n, rawPrime, primeList, upperLimit):
    ''' find the prime factors of the given number n, return the factors in a set. 
        Each factor's power is not considered
    '''
    pFactors = []
    for p in primeList:
        if not n % p: # find a factor p
            while not n % p: # remove all factor p from n
                n //= p
            pFactors.append(p)
            if rawPrime[n]: # if after removal of factor p, n becomes prime already, end search
                pFactors.append(n)
                return pFactors
            if n == 1:
                return pFactors
    
def phi(pFactors, d):
    ''' use totient function (see http://mathworld.wolfram.com/TotientFunction.html)
    '''
    nom = d
    den = 1
    for pF in pFactors:
        nom *= (pF - 1)
        den *= pF
    return nom // den

# driver
primeList = [] # list of prime numbers
upperLimit = 1000000
ans = 0
rawPrime = primeSieve(upperLimit + 1, primeList) # rawPrime is the direct result of the erathosthenes sieve, which will serve as buckets for prime number
for d in range(2, upperLimit + 1):
    if rawPrime[d]: # d is prime, the number of reduced proper fraction from 1/d to (d-1)/d is d - 1
        ans += d - 1
        # print(d, d - 1)
    else:
        pFactors = findPrimeFactor(d, rawPrime, primeList, upperLimit) # guarantee that prime factors in ascending order
        ans += phi(pFactors, d) # totient function
        # print(d, pFactors, phi(pFactors, d))


print(ans)

# runtime = 3.1 s


print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

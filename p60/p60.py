#! /usr/bin/env python3
import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Author: Fanchen Bao
Date: 09/26/2018

Project Euler: Problem 60

Solution: 
  The original idea of keeping looking for the next number to fit in the given four-prime is WRONG,
because there is no guarantee that the smallest five-prime must start with the smallest four-prime.
Thus, one must search each individual starting prime and find all possible prime groups that fit the requirement,
until a five-member gruop is encountered.

  One trick is to determine how large the search should be. I guess the largest of the five-prime shouldn't be too big,
thus, setting the upper limit to 10000. Luckily, I got the hit. If not, I will have to increase the range.
'''
from millerRabin import MillerRabin
from math import sqrt

def makePrimeList(upperLimit):
    ''' make a prime number list upto upperLimit'''
    rawPrime = [1] * upperLimit # prime sieve
    rawPrime[0] = 0
    rawPrime[1] = 0
    for i in range(4, upperLimit, 2):
        rawPrime[i] = 0
    for i in range(3, int(sqrt(upperLimit)), 2):
        j = i
        while j * i < upperLimit:
            rawPrime[i * j] = 0
            j += 2
    
    primeList = []
    size = 0
    for i in range(upperLimit):
        if rawPrime[i]:
            primeList.append(i)
            size += 1
    return primeList, size

def findPrimes(prePrimes, primeList, start, size, primeTest):
    ''' recursively find primes to form the list that satisfies the requirement. Stops when the first 5-element list is found '''
    if len(prePrimes) == 5:
        print("Primes are:", prePrimes, "And their sum is:", sum(prePrimes))
        return 1
    for i in range(start, size):
        fail = 0 # flag
        for target in prePrimes:
            # check two ways of concatenating
            if not primeTest.isPrime(int(str(target) + str(primeList[i]))) or not primeTest.isPrime(int(str(primeList[i]) + str(target))):
                fail = 1
                break
        if not fail and findPrimes(prePrimes + [primeList[i]], primeList, i + 1, size, primeTest): # find the current prime, and also find the remaining primes
            return 1
    return 0


# driver
upperLimit = 10000
primeList, size = makePrimeList(upperLimit)
primeTest = MillerRabin()

for i in range(1, size): # testing different starting case, but not 2 or 5
    if findPrimes([primeList[i]], primeList, i + 1, size, primeTest):
        break

# runtime = 16.5 s


print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

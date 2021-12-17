#! /usr/bin/env python3
import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Author: Fanchen Bao
Date: 09/21/2018

Project Euler: Problem 58

Solution: 
  Brute force with insight in the spiral.
  For each layer, the lenght of side = layer * 2 + 1
  For each layer, let start be the end of the previous layer (i.e. the lower right corner of previous layer),
Then the four corner values are: 

  upperRight = start + layer - 1
  upperLeft = upperRight + layer - 1
  lowerLeft = upperLeft + layer - 1
  lowerRight = lowerLeft + layer - 1

  All we need then is to find each corner value, check whether it is prime and record the total number of prime,
and at the end of each layer, check the prime rate.
  The initial method tries to use sieve to generate all necessary primes, but fails terribly because the required prime is too big.
  Second attempt is to use pre-calculated prime and put them in a dict to check whether a number is prime.
But that requires the program to read in 4 giant files of prime number (see http://www.primos.mat.br/2T_en.html) and is way to slow.
  Third attempt is going to test prime for each numebr use the method of division by prime up till sqrt(n)
'''
from math import sqrt

class Spiral:
    def __init__(self, start, layer):
        ''' a spiral class modeling the spiraling numbers'''
        self.start = start
        self.layer = layer
        self.side = 0
        self.corners = [0] * 4 # corners[0] = upperRight, corners[1] = upperLeft, corners[2] = lowrLeft, corners[3] = lowerRight,   

    def addNewLayer(self):
        self.layer += 1
        self.side = self.layer * 2 + 1
        # update the corner values
        self.corners[0] = self.start + (self.side - 1)
        for i in range(3):
            self.corners[i + 1] = self.corners[i] + (self.side - 1)
        self.start = self.corners[3]


def getRawPrime(upperLimit):
    ''' generate a sieve of rawPrime up till upperLimit'''
    rawPrime = [1] * upperLimit
    rawPrime[0] = 0
    rawPrime[1] = 0
    for i in range (4, upperLimit, 2):
        rawPrime[i] = 0
    for i in range (3, int(sqrt(upperLimit)), 2):
        j = i
        while (i * j < upperLimit):
            rawPrime[i * j] = 0
            j += 2
    return rawPrime

def isPrime(primeList, rawPrime, n, upperLimit):
    ''' check whether n is prime'''
    if n < upperLimit:
        return rawPrime[n]
    for prime in primeList:
        if not n % prime :
            return 0
        if prime > int(sqrt(n)):
            return 1

# driver
upperLimit = 100000
rawPrime = getRawPrime(upperLimit)
primeList = []
for i in range(upperLimit):
    if rawPrime[i]:
        primeList.append(i)

spiral = Spiral(1, 0)
numPrime = 0
found = 0
while(True):
    spiral.addNewLayer()
    for i in range(4):
        if isPrime(primeList, rawPrime, spiral.corners[i], upperLimit):
            numPrime += 1
    if numPrime / (2 * spiral.side - 1) < 0.1:
        print(spiral.side)
        break


# runtime = 5.3 s


print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

#! /usr/bin/env python3
import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Author: Fanchen Bao
Date: 10/06/2018

Project Euler: Problem 64

Solution: 
	For each number n, to get from sqrt(n) + a0 / c to a1 + (sqrt(n) - b) / c, it must satisfiy that b < sqrt(n).
Otherwise, n - b^2 would be negative. Therefore, this provides the anchor case for recursion.
We will brute force through all possible a1 >= 1, and check whether the corresponding b < sqrt(n).
Since as a1 gets bigger, b also gets bigger (because c * a1 - b = a0, in which a0 and c does not change),
once for a certain a1 b does not work, no more a1 needs to be tested. For those cases where b works, 
keep going down each calling tree until the desired squred root period is found. 
'''
from math import sqrt

def gcd(a, b):
    ''' find the gcd of number a and b, bot positive integers'''
    if a < b: # make sure a > b
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def findFraction(n, b, c, maxB, period, coeffDict):
    ''' n is the target number. b and c is the current coefficient to be dealt with. maxB = int(sqrt(n)).
        period records all period values. iniB and iniC is the first fraction to be transformed.
        If any subsequent coefficient b and c exists already in coeffDict, then the full period is found.
    '''
    # if gcd(n - b**2, c) != c: 
    #     coeffDict[(b, c)] = False # current b, c pair fails
    #     return False

    nextC = (n - b**2) // c # a big assumption that the coefficient in front of sqrt(n) is always 1
    nextA = 1
    while True:
        if nextA * nextC - b <= maxB:# find new a
            if nextA * nextC - b > 0: 
                nextB = nextA * nextC - b
                if (nextB, nextC) in coeffDict: # coefficient ecountered before
                    if coeffDict[(nextB, nextC)]: # previous encounter is valid, full period found
                        period.append(nextA)
                        return True
                    # else: previous encounter is invalid, increment nextA and try again
                
                else: # coefficient not encountered before
                    coeffDict[(b, c)] = True
                    if findFraction(n, nextB, nextC, maxB, period, coeffDict):
                        period.append(nextA)
                        return True
        else: # once 'nextA' cannot produce a positive 'nextB' smaller than maxB, no need to continue
            coeffDict[(b, c)] = False # current b, c pair fails
            return False
        nextA += 1


''' suppose each level of fraction can be expressed as a + (sqrt(n) - b) / c
    maxB represents the upper bound for coefficient b
'''
period = [] # record the repeated period
coeffDict = {} # record all coefficients that have occurred, and whether they can produce valid outcome (true) or not (false)
count = 0
for n in range(2, 10001):
    maxB = int(sqrt(n))
    period.clear()
    coeffDict.clear()
    if maxB**2 != n: # if n is perfect square, skip it
        for a0 in range(1, maxB + 1): # a0 is the first integer for the fraction representation
            coeffDict[(a0, 1)] = True # default to true, if it doesn't work, revert back to false
            if findFraction(n, a0, 1, maxB, period, coeffDict): # fraction period found
                break
            else:
                period.clear()
        # print("sqrt({})=[{}; {}], period = {}".format(n, a0, period, len(period)))
        if len(period) % 2:
            count += 1
print(count)


# runtime = 2.6 s


print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

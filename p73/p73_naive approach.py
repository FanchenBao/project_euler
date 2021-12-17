#! /usr/bin/env python3
import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Author: Fanchen Bao
Date: 12/02/2018

Project Euler: Problem 73

Solution: 
    Calculate first the lower and higher bound of n (minN and maxN) that allows for n/d be between 1/3 and 1/2 for any
given d. Then check for d. If it is a prime number, then all n from minN to maxN are suitable. If d is an even, then
check for only odd n for whether it is prime itself or coprime with n. If d is an odd, then check every single n
from minN to maxN for it being prime or coprime with n.
    Add all the suitable n together and one has the result.
'''

def gcd(a, b):
    if a > b: # make sure b is always the bigger number
        a, b = b, a
    if not b % a:
        return a
    else:
        return gcd(b % a, a)

def primeSieve(rawPrime, limit):
    ''' create rawPrime with index being the prime number'''
    rawPrime[0] = 0
    rawPrime[1] = 0
    for i in range(4, limit + 1, 2):
        rawPrime[i] = 0
    i = 3
    while i * i <= limit:
        j = i
        while j * i <= limit:
            rawPrime[i * j] = 0
            j += 2
        i += 2


res = 0
limit = 12000
rawPrime = [1] * (limit + 1)
primeSieve(rawPrime, limit)

for d in range(4, limit + 1):
    maxN = d // 2 if d % 2 else d // 2 - 1 # maxN/d is the biggest that is smaller than 1/2
    minN = d // 3 + 1 # minN/d is the smallest that is bigger than 1/3
    if rawPrime[d]: # d is prime
        res += maxN - minN + 1
        continue

    if not d % 2: # d is even, all even n cannot be chosen, 
        minN = minN if minN % 2 else minN + 1 # start minN as odd
        for n in range(minN, maxN + 1, 2):
            if rawPrime[n] or gcd(n, d) == 1: # n is prime or coprime with d
                res += 1
    else: # d is odd
        for n in range(minN, maxN + 1):
            if rawPrime[n] or gcd(n, d) == 1: # n is prime or coprime with d
                res += 1




print(res)

# runtime = 14 s


print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

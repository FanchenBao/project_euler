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
    Using the sieve method to generate a list of sets contatining each index number's prime factors (prime index number
set is left blank). This allows for faster check on coprime situations. The basic algorithm is the same as p73_naive approach.py,
but performance has improved by more than 3 folds.
'''


def primeFactorGenerator(pFactor, limit):
    ''' create rawPrime with index being the prime number'''
    for i in range(4, limit + 1, 2):
        pFactor[i].add(2)
    i = 3
    while i <= limit // 3:
        if not pFactor[i]: # i is a prime
            j = 2
            while j * i <= limit:
                pFactor[j * i].add(i)
                j += 1
        i += 2


res = 0
limit = 12000
pFactor = [set() for i in range(limit + 1)]
primeFactorGenerator(pFactor, limit)

for d in range(4, limit + 1):
    maxN = d // 2 if d % 2 else d // 2 - 1 # maxN/d is the biggest that is smaller than 1/2
    minN = d // 3 + 1 # minN/d is the smallest that is bigger than 1/3
    if not pFactor[d]: # d is prime
        res += maxN - minN + 1
        continue

    if not d % 2: # d is even, all even n cannot be chosen, 
        minN = minN if minN % 2 else minN + 1 # start minN as odd
        for n in range(minN, maxN + 1, 2):
            if not pFactor[n] or not pFactor[n].intersection(pFactor[d]): # n is prime or coprime with d
                res += 1
    else: # d is odd
        for n in range(minN, maxN + 1):
            if not pFactor[n] or not pFactor[n].intersection(pFactor[d]): # n is prime or coprime with d
                res += 1




print(res)

# runtime = 4 s


print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

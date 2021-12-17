#! /usr/bin/env python3
import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Author: Fanchen Bao
Date: 01/31/2018

Project Euler: Problem 77

Solution:
    Same solution as Problem 76. Use an array (calling it dp) of dictionaries to 
record the number of sum expressions starting at each prime number. 
E.g. dp[8] = {2:2, 3:1}, because 8 = 2+3+5, 2+2+2+2, 3+5
    For each new number n, for each prime number p in a prime number list, find 
whether n-p is prime (if it is, that would be a legitimate sum expression). Then
find out how many ways n-p can be expressed by prime number ≥ p, which is to say
sum(dp[n-p][p1], dp[n-p][p2], dp[n-p][p3], ...), where p1 = p, p2 = prime next to p1,
p3 = prime next to p2, etc. Repeat this for each p until p > n // 2
    Total number of expressions is checked for each number n. If the target
total has been reached, the program ends. This algorithm is able to compute the 
first number expressable in 10^18 ways in 1.4 s (set primeBound to 10000 and 
sumExpressionLimit to 1000000000000000000).
 
'''
from math import sqrt

def sieve(limit):
    primeSieve = [1] * (limit + 1)
    primeSieve[0] = 0
    primeSieve[1] = 0
    for i in range(4, limit + 1, 2):
        primeSieve[i] = 0
    for i in range(3, int(sqrt(limit)) + 1, 2):
        j = i
        while (i * j < limit):
            primeSieve[i * j] = 0
            j += 2
    return primeSieve

def getPrimes(primeSieve):
    primes = []
    for i, r in enumerate(primeSieve):
        if r:
            primes.append(i)
    return primes    

primeBound = 100 # upper limit for prime number. This number is guessed
primeSieve = sieve(primeBound)
primes = getPrimes(primeSieve)
sumExpressionLimit = 5000

# dp records the number of prime sum expressions for each number.
# Each element of dp is a dictionary, with key a prime number, 
# value the number of prime sum expressions for the index of the element
# that can begin with the key.
# E.g. dp[4] = {2 : 1}, because 4 can be expressed in only one way starting with
# prime number 2 (4 = 2+2)
# E.g. dp[8] = {2:2, 3:1}, because 8 = 2+3+5, 2+2+2+2, 3+5 
dp = [{}, {}, {}, {}, {2:1}] 

for n in range(5, primeBound + 1):
    sumCount = dict()
    total = 0
    for i, p in enumerate(primes):
        if p > n // 2:
            break
        sumCount[p] = 0
        if primeSieve[n - p]: # n = p + (n - p) satisfies the requirement
            sumCount[p] += 1
        j = i # note that primes[j] = p
        while primes[j] in dp[n - p]: # add up all number of expressions for n - p when the starting number ≥ primes[j]
            sumCount[p] += dp[n - p][primes[j]]
            j += 1
        total += sumCount[p]
    if total > sumExpressionLimit:
        print(n, total)
        break
    dp.append(sumCount)

# runtime = 0.002s


print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

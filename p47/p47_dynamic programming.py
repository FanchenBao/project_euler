#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Use dynamic programming to find the numbr of distinct prime factor of a given number.
Important lesson learned is that when passing list as argument, be very careful when using splice, because splicing is to copy the whole list
'''

def primeSieve(n):
    ''' create a prime sieve up to number n - 1'''
    primeFactorSieve = [1] * n
    primeFactorSieve[0] = 0
    primeFactorSieve[1] = 0
    for i in range(4, n, 2):
        primeFactorSieve[i] = 0
    i = 3
    while(i * i < n):
        j = i
        while(i * j < n):
            primeFactorSieve[i * j] = 0
            j += 2
        i += 2
    return primeFactorSieve

def makePrimeList(primeFactorSieve, n):
    ''' produce a prime number list based on rawPrime'''
    primeList = []
    count = 0
    for i in range(n):
        if primeFactorSieve[i]:
            primeList.append(i)
            count += 1
    return primeList, count

def countPrimeFactor(num, primeList, primeFactorSieve, start, plSize):
    ''' calcualte the number of distinct prime factors in num'''
    if num == 1:
        return 0
    elif primeFactorSieve[num]:
        return primeFactorSieve[num]
    else:
        n = num
        for i in range(start, plSize):
            if not n % primeList[i]:
                while not n % primeList[i]: # remove the same prime factor
                    n //= primeList[i]
                
                # primeFactorSieve[num] = 1 + primeFactor(n, primeList[i+1:], primeFactorSieve) # this line is crucial to avoid. Every time a splice is done to a list, it makes a copy. When the original list is millions in length, making copy takes a LONG time.
                primeFactorSieve[num] = 1 + countPrimeFactor(n, primeList, primeFactorSieve, i + 1, plSize)
                return primeFactorSieve[num]



# create a prime number list
n = 1000000
primeFactorSieve = primeSieve(n) # not only indicate prime, but also store the number of distinct prime factors for each number
primeList, plSize = makePrimeList(primeFactorSieve, n)

targetValue = 4 # 4 consecutive numbers with 4 distinct prime numbers
i = 647
while(1):
    if not primeFactorSieve[i] and countPrimeFactor(i, primeList, primeFactorSieve, 0, plSize) == targetValue: # i must not be prime and its prime factors number has the target value
        i += 1
        count = 1
        while(countPrimeFactor(i, primeList, primeFactorSieve, 0, plSize) == targetValue):
            count += 1
            i += 1
        if count == targetValue:
            print(i - 4)
            break
    else:
        i += 1

# runtime = 0.8 s

print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
First check sum of digits (SOD). If it is divisible by 3, then the number cannot be prime.

9-digit: SOD = 45 nope
8-digit: SOD = 36 nope
7-digit: SOD = 28 maybe
6-digit: SOD = 21 nope
5-digit: SOD = 15 nope
4-digit: SOD = 10 maybe

So the only possiblities are 7-digit or 4-digit numbers. 
The following method creates a prime number list to 4321. 
It then creates all permutations of the 7-digit and 4-digit number (with last digit only being 1, 3, or 7).
Then the numbers are checked for whether it being prime.
'''
from itertools import permutations

def eratosthenesSieve(upperLimit):
    ''' produce prime numbers from 2 to 4321'''
    size = upperLimit + 1
    rawPrime = [1] * size
    rawPrime[0] = 0
    rawPrime[1] = 0
    primeList = []

    for i in range(4, size, 2):
        rawPrime[i] = 0

    for i in range(3, size, 2):
        if rawPrime[i]:
            for j in range(3, size // i + 1, 2):
                rawPrime[i * j] = 0

    for i in range(size):
        if rawPrime[i]:
            primeList.append(i)

    return primeList

upperLimit = 4321
primeList = eratosthenesSieve(upperLimit)
found = 0

# check 7-digit
sevenDigits = [int(''.join(numList)) if numList[-1] == '1' or numList[-1] == '3' or numList[-1] == '7' else 0 for numList in list(permutations("1234567"))]
for num in sorted(sevenDigits, reverse = True):
    if num:
        isPrime = 1
        # check whether num is prime
        for prime in primeList:
            if prime < num ** 1/2:
                if not num % prime: # num is NOT prime
                    isPrime = 0
                    break
            else:
                break
        if isPrime:
            print(num)
            found = 1
            break

if not found:
    # check 4-digit, if necessary
    fourDigits = [int(''.join(numList)) if numList[-1] == '1' or numList[-1] == '3' else 0 for numList in list(permutations("1234"))]
    for num in sorted(fourDigits, reverse = True):
        if num and rawPrime[num]:
            print(num)
            break



# runtime = 0.006 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

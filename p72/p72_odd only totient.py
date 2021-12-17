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
    Using the formula from 72.6 (read the overview pdf), we will sieve the toteint for all odd numbers. Then use
odd numbers to generate the sum of totients for all the rest even numbers.
'''
from math import log10

def oddTotientSieve(upperLimit):
    ''' Using the sieving method to calculate totients for all odd numbers up to upperLimit '''
    oddTotient = [i - 1 for i in range(upperLimit + 1)]
    oddTotient[1] = 1 # for the sake of this calculation, phi(1) is defined as 1
    i = 3
    while 3 * i <= upperLimit: # note the difference in the boundary condition from an Erathosthenese sieve. 
                                # We have to check for all multiples of i starting from 3 to not miss i as 
                                # prime factor for small odd composite numbers
        if oddTotient[i] == i - 1: # i is prime
            j = 3 # start from 3 each time to not miss i as prime factors for small odd composite numbers
            while j * i <= upperLimit:
                if oddTotient[j * i] == j * i - 1: # this odd composite number is visited the first time, restore its initial value
                    oddTotient[j * i] = j * i
                oddTotient[j * i] = oddTotient[j * i] * (i - 1) // i # i is one prime factor of current number j * i
                j += 2
        i += 2

    return oddTotient
    
# driver
upperLimit = 1000000
ans = 0
oddTotient = oddTotientSieve(upperLimit)
for n in range(1, upperLimit + 1, 2): # loop through each even number
    m = int(log10(upperLimit / n) / log10(2)) # for each even number, calculate the maximum power m that can satisfy 2^m * n <= upperLimit
    ans += 2**m * oddTotient[n]     # include the totient sums of phi(n) + phi(2*n) + phi(2^2 * n) + ... + phi(2^m * n)
    # print(n, m, oddTotient[n])
ans -= 1 # remove phi(1) since 1 cannot be a denominator

print(ans)

# runtime = 1.6 s


print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

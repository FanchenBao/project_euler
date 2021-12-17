#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
from math import sqrt

def printMaxPrime(numbers, list_lim):
    ''' print out the maximum prime number after the Eratosthenes sieve'''
    i = -1
    while (1):
        if not numbers[i]:
            print(2 * (list_lim + i) + 3)
            return
        i -= 1

def printSum(numbers, list_lim):
    ''' print out the sum of all prime numbers before limit'''
    result = 2
    for i in range(list_lim):
        if not numbers[i]:
           result += 2 * i + 3
    print(result)

'''
This is the optimized Eratosthenes sieve. Basic concept is the same as regular Erastosthenes sieve, but the list size is cut in half since even numbers are not even considered.
There needs to be index arithmetic to determine how an index corresponds to an odd number. If odd number starts from 3, and the index starts from 0,
then the correspondence is odd = 2 * index + 3. Using this arithmetic, the original sieve code can be adapted to the optimized one.
As expected, since even numbers are not even considered, the program takes half the time to complete.
'''
s = time()

limit = 2000000
list_lim = (limit % 2) and (int((limit - 2) / 2) + 1) or (int((limit - 2) / 2)) # size of list only fit all odd numbers from 3 to the largest odd number.
numbers = [0] * list_lim

for i in range(int((sqrt(limit) -3) / 2) + 1): # for the iterator i, its corresponding prime candidate is 2i+3, thus (2i+3)^2 < limit --> i < (sqrt(limit) -3)/2
    if not (numbers[i]):
        j = 2 * i**2 + 6 * i + 3    # start marking multiples of the prime number 2i+3 from (2i+3)^2. Because any composite number smaller than a prime number squared would have been marked by multiples of smaller prime numbers.
                                    # 2j+3 = (2i+3)^2 --> j=2i^2+6i+3
        while (j < list_lim):
            numbers[j] = 1 # mark the composite position 1
            j += 2 * i + 3  # j increases 2 times of the prime number (p) at a time because p^2 + p is even and not considered. Only p^2 + 2p is odd and potential prime candidate
                            # 2j+3 = 2j+3+2(2i+3) --> j = j+2i+3


printSum(numbers, list_lim)
# printMaxPrime(numbers, list_lim)

# time to finish is about 2 seconds.



print("Time: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

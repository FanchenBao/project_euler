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
The following method creates a prime number list all the way up to 7654321. 
Then check from 7654321 down to look for the first prime number that also satisfies the pandigit requirement.
It avoids the hassel of creating permutations of numbers, but does take a long time to finish.
'''
def eratosthenesSieve(upperLimit):
    ''' produce prime numbers from 2 to 4321'''
    size = upperLimit + 1
    rawPrime = [1] * size
    rawPrime[0] = 0
    rawPrime[1] = 0
    for i in range(4, size, 2):
        rawPrime[i] = 0
    for i in range(3, size, 2):
        if rawPrime[i]:
            for j in range(i * 3, size, i):
                rawPrime[j] = 0

    return rawPrime

upperLimit = 7654321
rawPrime = eratosthenesSieve(upperLimit)
found = 0

for i in range(7654321, 1234566, -1): # check 7-digit first
    if rawPrime[i]:
        strNum = str(i)
        if ''.join(sorted(strNum)) == "1234567":
            print(i)
            found = 1
            break

if not found: # if nothing found in 7-digit, look in 4-digit
    for i in range(4321, 1242, -1):
        if rawPrime[i]:
            strNum = str(i)
            if ''.join(sorted(strNum)) == "1234":
                print(i)
                break



# runtime = 2.7 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

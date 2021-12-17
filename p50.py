#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
First identify that the first 546 prime numbers' sum is the largest that is under 1 million.
The answer must be within the sequence of the first 546 prime numbers, because venturing any further would cost significant loss in the length of the final sequence.
In other words, keep as many small primes as possible to maximize the length of the resulting sequence.

Then check length from 546 down and try every combination of consecutive sequence that fits that length along the way.
The first match is the longest sequence.
'''

def primeSieve(n):
    ''' return raw prime after the sieve, up to n - 1'''
    rawPrime = [1] * n
    rawPrime[0] = 0
    rawPrime[1] = 0
    for i in range(4, n , 2):
        rawPrime[i] = 0
    i = 3
    while i * i < n:
        j = i
        while i * j < n:
            rawPrime[i * j] = 0
            j += 2
        i += 2
    return rawPrime

n = 1000000
rawPrime = primeSieve(n)

# get the prime list
primeList = []
sigma = 0 # after the following loop, sigma goes to max
for i in range(n):
    if rawPrime[i]:
        sigma += i
        if sigma < n:
            primeList.append(i)
        else:
            break

maxLength = len(primeList) # length set to max length
length = maxLength

while(length >= 0):
    start = 0
    end = length - 1
    while start <= maxLength - length and rawPrime[sum(primeList[start:end+1])] != 1:
        # each iteration, move start and end forward
        start += 1
        end += 1
    if start <= maxLength - length: # found it
        break
    length -= 1

print("Start index: {}, end index: {}, length of sequence: {}, sum of sequence: {}".format(start, end, length, sum(primeList[start:end+1])))



# runtime = 0.4 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

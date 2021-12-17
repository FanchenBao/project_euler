#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Make a prime list up to 10000. Loop through them and decide whether the two other numbers are prime and permutations of the first one.
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


rawPrime = primeSieve(10000)

for i in range(1000, 3340):
    if rawPrime[i]: # i must be prime
        if i == 1487:
            continue
        sortedI = ''.join(sorted(str(i)))
        j = i + 3330
        if rawPrime[j] and sortedI == ''.join(sorted(str(j))): # j is prime and permutation of i
            k = j + 3330
            if rawPrime[k] and sortedI == ''.join(sorted(str(k))): # k is prime and permutatio of i
                print(str(i)+str(j)+str(k))
                rawPrime[j] = 0 # do not consider j and k again
                rawPrime[k] = 0


# runtime = 0.003 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

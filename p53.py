#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Use dynamic programming to calculate factorial.
Use Pascal triangle's symmetry to save iteration of r.
And since it's python, we don't have to worry about big number, and can brute force calculate each combination number.
'''
def factorial(n, factDict):
    '''dynamically calculating n!'''
    if n in factDict:
        return factDict[n]
    else:
        factDict[n] =  n * factorial(n - 1, factDict)
        return factDict[n]


def C(n, r):
    ''' calculate combination num'''
    return factorial(n, factDict) // (factorial(r, factDict) * factorial(n - r, factDict))

factDict = {1:1}
count = 0
for n in range(23, 101):
    for r in range(2, n // 2 + 1):
        if C(n, r) > 1000000:
            count += 2 if n % 2 else 1 if r == n // 2 else 2

            # if n % 2: # n is odd
            #     count += 2
            # else: # n is even
            #     if r != n // 2:
            #         count += 2
            #     else
            #         count += 1

print(count)


# runtime = 0.006 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

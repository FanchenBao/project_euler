#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
From mathematic analysis, we know that the only possible numbers must have fewer than 6 digits, then brute force all of them
'''
def findMatch(digits, power, n):
    ''' check whether a number can be expressed as the sum of power of its digits'''
    sigma = 0
    num = n
    for i in range(digits):
        sigma += (num % 10)**power
        num //= 10
    if sigma == n:
        return sigma
    else:
        return 0

def findSum(digits, power):
    res = 0
    for num in range(10**(digits - 1), 10**(digits)):
        sigma = findMatch(digits, power, num)
        if sigma:
            print(sigma)
            res += sigma
    return res

res = 0
for digits in range(2, 7):
    res += findSum(digits, 5)
print("The total sum is {}".format(res))


# runtime = 3.4 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

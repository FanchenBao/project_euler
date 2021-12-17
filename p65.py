#! /usr/bin/env python3
import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Author: Fanchen Bao
Date: 10/11/2018

Project Euler: Problem 65

Solution: 
	Brute force. But have to pay attention to the edge situation. Use tuples to represent fractions.
And note that the nature of continued fraction guarantee that the each convergent's numerator and denominator
are prime to each other.
'''

a = b = 1 # this is the last component (100th) of the fraction sequence; a is numerator, b denominator
for i in range(99, 1, -1): # from 99 to 2. Cannot go to the first component because it does not follow the regularity of other components
    if i % 3: # not multiple of 3, the sequence is 1
        a, b = b, a + b
    else: # is multiple of 3, the sequence is i // 3 * 2
        a, b = b, b * (i // 3 * 2) + a

a, b = 2 * b + a, b # the first sequence
sumOfDigit = sum([int(digit) for digit in list(str(a))])
# print(a, b)
print(sumOfDigit)

# runtime = 0.001 s


print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

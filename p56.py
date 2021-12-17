#! /usr/bin/env python3
import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Author: Fanchen Bao
Date: 09/16/2018

Project Euler: Problem 56

Solution: 
  Brute force it first of course. 
  Optimization is to search only 90 above for base and power, 
because as their value drops, the expected SOD decreases significantly 
(expected SOD can be estimated by 5 * number_of_digits).
'''

def calSOD(n):
    ''' calculate sum of digits of the given number n'''
    sigma = 0
    for digit in str(n):
        sigma += int(digit)
    return sigma

maxSOD = 0
for i in range(90, 100):
    for j in range(90, 100):
        sod = calSOD(i**j)
        maxSOD = sod if sod > maxSOD else maxSOD

print(maxSOD)

# runtime = 0.005 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

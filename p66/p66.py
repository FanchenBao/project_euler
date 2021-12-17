#! /usr/bin/env python3
import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Author: Fanchen Bao
Date: 10/13/2018

Project Euler: Problem 66

Solution: read Pell Equation on http://mathworld.wolfram.com/PellEquation.html
continuedFraction module is uploaded to my GitHub
	
'''
from math import sqrt
from continuedFraction import ContinuedFraction

maxx = 0
resD = 2
for D in range(2, 1001):
    if sqrt(D) != int(sqrt(D)): # skip perfect squares
        CF = ContinuedFraction(D)
        
        # Use the solution from Pell Equation to get the depth of convergent (http://mathworld.wolfram.com/PellEquation.html)
        # The minimal solution to the quadratic Diophantine Equation is the numerator and denominator of Rth convergent
        if CF.periodLen % 2:
            R = 2 * (CF.periodLen - 1) + 1
        else:
            R = CF.periodLen - 1
        
        x, y = CF.getConvergent(R + 1) # note that the convergent numbering system on the Wolfram websit starts at the beginning of the period. But here we start at the first integer outide the period.
        (maxx, resD) = (x, D) if x > maxx else (maxx, resD)

print(maxx, resD)


n = 23
R = 9
CF = ContinuedFraction(n)
num, den = CF.getConvergent(R)
print("The {}th convergent is: {}/{}".format(R, num, den))
# runtime = 0.02 s


print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

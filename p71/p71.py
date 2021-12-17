#! /usr/bin/env python3
import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Author: Fanchen Bao
Date: 11/09/2018

Project Euler: Problem 71

Solution:
    The target fraction is 3/7, the task is to find the largest reduced proper fraction with denominator 
smaller than 1,000,000. So I transform 3/7 into a fraction with denominator being each integer from 1 to 
1,000,000. The corresponding numerator would be a fraction to make the transformed version equal to 3/7.
Thus, if I take only the integer part of the fraction on the numerator, the new fraction must be smaller
than 3/7,  but also very close to 3/7. In fact, that fraction would be the largest fraction smaller than 3/7
with the specific denominator. Loop through each possibility of denominator and the largests such fraction
should be the answer.
    After reading the overview of problem 71, there appears to be a faster way to solve this problem by
first searching the denominator from 1,000,000 down and then break out the search when a condition is reached.
The condition is as follows:
    Suppose we currently have found a max fraction n/d smaller than targetN/targetD. The distance between
n/d and targetN/targetD is 

(n * targetD - d * targetN) / (d * targetD)

Suppose the next fraction we are trying to find is p/q, then the distance between p/q and targetN/targetD is 

(p * targetD - q * targetN) / (q * targetD) >= 1 / (q * targetD) 

The above expression gives the smallest distance bewteen p/q and targetN/targetD. In order for p/q to be a viable solution
we must have the current distance between n/d and targetN/targetD bigger than the smallest distance of the
potential p/q 

(n * targetD - d * targetN) / (d * targetD) > 1 / (q * targetD)
=> q > d / (n * targetD - d * targetN)

Observing this expression, we notice that if n * targetD - d * targetN <= 1, then q doesn't exist. In other
words, n * targetD - d * targetN <= 1 is the condition to check for breaking the loop.
'''

targetD = 7
targetN = 3
maxD = 1000000
maxAns = 0 # the max value of the fraction that is smaller than 3/7
for d in range(maxD, 0, -1):
    if d % targetD:
        n = targetN * d // targetD
        if (n / d > maxAns):
            ans = (n, d)
            maxAns = n / d
        if targetN * d - targetD * n <= 1: # determine when the search shall end
            break
print(ans)


# runtime < 0.01 s


print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Reverse checking the numbers d, find the first that has recurring period equal to d - 1.
User dict to greatly facilitate efficiency
'''

def oneOverN(n):
    ''' return the length of recurring period of 1 / n'''
    divisors = {}
    divisor = 1
    order = 0
    while(1):
        res = divisors.get(divisor, -1) # check whether divisor already in divisors.
                                        # if not return -1, if yes return the initial divisor's order
        if res < 0: # not recurring yet
            divisors[divisor] = order
            divisor = (divisor % n) * 10
            order += 1
        else: # divisor occurred before
            return (len(divisors) - res)
            


for d in range(999, 0, -1):
    length = oneOverN(d)
    if(length == d - 1): # the max recurring period is d - 1, because the max number of divisors possible for d (10 * remainder) in a long division is d - 1
        print(d)
        break

# runtime = 0.0032 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

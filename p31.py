#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Recursive
'''

def make(pennies, amount, startPenny, res):
    ''' calculate how many different coin combinations exist to make a certain amount'''
    if startPenny == pennies[-1]: # smallest penny, direct check by divisibility of the remaining amount
        if amount % startPenny == 0: return res + 1
    else:
        if amount == 0: return res + 1
        else:
            for penny in pennies:
                if penny <= startPenny: # each time the search starts with the penny not bigger than the penny of the previous round
                    if amount >= penny:
                        res = make(pennies, amount - penny, penny, res)
            return res



pennies = [200, 100, 50, 20, 10, 5, 2, 1]
print(make(pennies, 200, 200, 0))

# runtime = 0.08 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

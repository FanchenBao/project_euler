#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

from math import log10

''' direct calculation'''
power = 1000

results = [int(i) for i in str(2**power)]
print("The sum of digits is: {}".format(sum(results)))
print(2**power)


# runtime = 0.00079 s


print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

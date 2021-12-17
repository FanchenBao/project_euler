#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

from math import factorial

''' 
THis is the lazy method, yet not slow.
'''

print(sum([int(a) for a in str(factorial(100))]))

# print(factorial(23))

# runtime = 0.006 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

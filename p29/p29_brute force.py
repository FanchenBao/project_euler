#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
For this specific problem, mathematic analysis comes first. 
This brute force is inspired by other people's answers and the fact that python can handle unlimited precision numbers
'''

numsDict = {}
for a in range(2, 101):
    for b in range(2, 101):
        num = a**b
        if not num in numsDict:
            numsDict[num] = True

print(len(numsDict))

# runtime = 0.01 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

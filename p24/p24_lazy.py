#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

import itertools

''' take advantage of the permutation function in python library'''

def intoNum(aTuple):
    ''' turn the elements within a tuple into a num'''
    length = len(aTuple)
    num = 0
    for digit in aTuple:
        num += (10 ** (length - 1)) * digit
        length -= 1

    return num

permutationList = list(itertools.permutations(range(10)));
print(intoNum(permutationList[1000000 - 1]))


# runtime = 0.8 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

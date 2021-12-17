#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Let triangular = hexagonal:
    t^2 + t = 2h(2h - 1) --> t = 2h - 1
Thus hexagonal is included in triangular. No comparison needed.

Then compare pentagonal and hexagonal, starting from the very next index after the previous equality point.
If one number is bigger, increment the index of the other number, until a match is found.
'''

def pent(n):
    ''' return the nth pentagonal number'''
    return n * (3 * n - 1) // 2

def hex(n):
    ''' return the nth hexagonal number'''
    return n * (2 * n - 1)

p = 166
h = 144
while(1):
    if (pent(p) > hex(h)):
        h += 1
    elif (pent(p) < hex(h)):
        p += 1
    else:
        print("t = {}, p = {}, h = {}".format(2 * h - 1, p, h))
        print("T = P = H = {}".format(pent(p)))
        break


# runtime = 0.06 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

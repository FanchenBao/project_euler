#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

from math import sqrt

def situation(unitA, unitB):
    for i in range(0, 100):
        for j in range(0, 100):
            a = 10 * i + unitA
            b = 10 * j + unitB
            c = sqrt(a**2 + b**2)
            if (a + b + c == 1000) & (a < c) & (b < c): # check for both c is int and the sum is 1000
                print(a, b, int(c))
                print(a * b * int(c))
                return 1
    return 0

def find():
    for i in range(0, 10):
        if situation(0, i):
            return # since only one pair of (a, b, c) exists, once found we are done
    for i in range(2, 10, 2):
        if situation(i, 5):
            return

find()







print("Time: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

#! /usr/bin/env python3
import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Author: Fanchen Bao
Date: 12/16/2018

Project Euler: Problem 73

Solution: 
    The Stern-Brocot method uses a lot of stack memory. With python3, the maximum limit I can go to before
stack overflow is 1998, which is actually not good enough to solve problem 73.
'''


def sternBrocot(limit, beginN, beginD, endN, endD):
    medN = beginN + endN
    medD = beginD + endD
    if medD > limit:
        return 0
    else:
        count = 1
        count += sternBrocot(limit, beginN, beginD, medN, medD)
        count += sternBrocot(limit, medN, medD, endN, endD)
        return count




print(sternBrocot(1998, 1, 3, 1, 2))

# runtime = N/A


print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

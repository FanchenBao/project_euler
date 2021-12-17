#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()


def chainCollatz(n, isMax):
    count = 1
    while(n > 1):
        if isMax:
            print("{} --> ".format(n), end = '')
        if (n % 2):
            n = 3 * n +1
        else:
            n //= 2
        count += 1
    if isMax:
        print(1)
    return count


# brute force.
currentMax = 0
desiredNum = 0

for n in range(500000, 1000000, 2) : # optimized the starting point
    count = chainCollatz(n + 1, 0)
    if count > currentMax:
        currentMax = count
        desiredNum = n + 1

print("The starting number is {} to create max chain length {}".format(desiredNum, currentMax))

# runtime = 7.3 s

print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

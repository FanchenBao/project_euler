#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

# def countCollatz(startNum, counts):
# ''' this is the non-recursive version of the same solution. It's a bit slower than recursive'''
#     n = startNum
#     passerby = []
#     flag = 1
#     if n in counts.keys():
#         return

#     count = 1
#     while(n > 1):
#         if (n % 2):
#             n = 3 * n +1
#             if str(n) in counts.keys():
#                 counts[str(startNum)] = count + counts[str(n)]
#                 flag = 0
#                 break
#             passerby.append(n)
#         else:
#             n //= 2
#             if str(n) in counts.keys():
#                 counts[str(startNum)] = count + counts[str(n)]
#                 flag = 0
#                 break
#             passerby.append(n)
#         count += 1
    
#     if flag:
#         counts[str(startNum)] = count
#     for i in range(len(passerby)):
#         counts[str(passerby[i])] = counts[str(startNum)] - i - 1



def countCollatz(n, counts):
    ''' recursive solution. Each time a number's chain count is acquired, record it, 
    so that when the same number is encountered again, its chain count can be acquired directly instead of calculating all over again.
    Use python's dictionary to easily achieve this. Do not use a list and try to hash the target number,
    because the size of the list can become so gigantic that it actually takes much much more time'''
    if n in counts.keys():
        return counts[n]
    else:
        if n % 2:
            counts[n] = 2 + countCollatz((3 * n +1) // 2, counts) # optimization: when n is odd, (3n+1) must be even, and start looking there
        else:
            counts[n] = 1 + countCollatz((n // 2), counts)
        
        return counts[n]

LIMIT = 1000000
counts = {1 : 1} # optimization: instead of using str as key, use int directly
currentMax = 0
desiredNum = 0
n = 500001 # optimization, start from 500001, because any n smaller than this would have its chain included in 2n. And the chain of 2n is always bigger.

while (n < LIMIT):
    countCollatz(n, counts)
    if counts[n] > currentMax:
        currentMax = counts[n]
        desiredNum = n
    n += 1 # even numbers shall not be skipped as when LIMIT gets higher, even number could be the answer.


print("The starting number is {} to create max chain length {}".format(desiredNum, currentMax))

# recursive runtime = 1.7 s


print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

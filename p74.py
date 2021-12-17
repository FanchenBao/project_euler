#! /usr/bin/env python3
import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Author: Fanchen Bao
Date: 12/28/2018

Project Euler: Problem 74

Solution: 
    Brute force. Check each number's loop from 3 to 1 million. Two key points to make the brute force manageable:
1. Dynamic programming: use a dictionary to record the number of steps starting from any number that has been
encountered already (either as a starting number or an intermediate step). This can save computation next time
the same number is encountered.

2. There are more numbers that can self-point. 169 is not the only one. Other examples are 1, 2, and 40585 within
1 million.
'''
# def factorial(n):
#     res = 1
#     if n != 0:
#         for i in range(n, 1, -1):
#             res *= i
#     return res

def factSum(n, factorials):
    ''' calculate the sum of the factorial of each digit in the given number n'''
    res = 0
    while n:
        res += factorials[n % 10]
        n //= 10
    return res

# anchors is a dict recording the number of steps starting with the number in the key
anchors = {1 : 1, 2 : 1, 145 : 1, 169 : 3, 363601 : 3, 1454 : 3, 871 : 2, 45361 : 2, 872 : 2, 45362 : 2}
factorials = [1,1,2,6,24,120,720,5040,40320,362880]
limit = 1000000
ans = 0
intermediates = [] # record the steps inside the loop that have not been included in the anchors yet
for i in range(3, limit):
    step = 0
    n = i
    intermediates.clear()
    while n not in anchors: # keep searching for next step if it is not in the anchors
        intermediates.append(n)
        nextN = factSum(n, factorials)
        if n == nextN: # enters self-pointing loop (similar to the situation as 169) not previously encountered
            anchors[n] = 1
            break
        else: # n is not self-pointing, update n and step and go for next step
            n = nextN
            step += 1
    step += anchors[n] # n has been encountered before or is self-pointing, no need to keep searching. Calculate total number of steps starting from i directly
    for index, j in enumerate(intermediates): # add the intermediate steps to anchors
        anchors[j] = step - index
    if step == 60:
        ans += 1


print(ans)
# runtime = 3.2 s


print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

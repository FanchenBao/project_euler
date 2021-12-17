#! /usr/bin/env python3
import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Author: Fanchen Bao
Date: 09/13/2018

Project Euler: Problem 55

Solution: 
  Brute force every number to locate the Lychrels. 
  And also note the bad implementation of reverseNum().
  And and, initially I also had a separate function to check for palindrome, by way of comparing the symmetrical digit of a number, 
while forgetting that the easiest way to check for palindrome is to reverse it and check whether the reverse is equivalent to the original.
  This is a pure demonstration that after a few days off project euler, the problem solving capabilities have decined.
'''

# def reverseNum(n):
#     ''' reverse the digits in n, and return the reversed number.
#         Note that one cannot use reverse sort because sort is based on digit value, not its position
#     '''
#     reverseNum = 0
#     while n:
#         reverseNum = reverseNum * 10 + n % 10
#         n //= 10
#     return reverseNum

def reverseNum(n):
    return int(str(n)[::-1])

def isLychrel(n):
    ''' determine whether n is Lychrel'''
    maxIter = 50
    it = 0
    while it < maxIter:
        n = n + reverseNum(n)
        if n == reverseNum(n): # not Lychrel number
            return 0
        it += 1
    return 1 # over 50 iteration still no palindrome, is Lychrel number


# driver
count = 0
for i in range(10, 10000):
    if isLychrel(i):
        count += 1
        # print(i)
print(count)


# runtime = 0.09 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

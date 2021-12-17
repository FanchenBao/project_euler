#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

def intoBinary(n):
    ''' turn a base-10 number into binary, return the string form'''
    if n == 1:
        return '1'
    else:
        return intoBinary(n // 2) + str(n % 2)

def isPalindrome(strN):
    ''' check whether a given number (turned into string already) is palindromic'''
    return 1 if strN == strN[::-1] else 0

sigma = 0
for i in range(1, 1000000, 2): # check only odd numbers, since even ones have 0 as LSB in binary
    if isPalindrome(str(i)) and isPalindrome(intoBinary(i)):
        print(i)
        sigma += i


print("The sum is {}".format(sigma))

# runtime = 0.4 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

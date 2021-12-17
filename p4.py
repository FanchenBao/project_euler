#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

def isPalindrome(n):
    digits = str(n)
    if digits == digits[::-1]: # determine whether digits are the same in reverse
        return 1
    return 0

currentMax = 0
upper_j = 990 # the product is a multiple of 11, so one of the factor must be multiple of 11
for i in range(999, 99, -1): # loop from 999 down 1 at a time
    for j in range(upper_j, 109, -11): # loop down 11 at a time
        product = i * j
        if product > 100000: # guess the answer is 6 digit 
            if isPalindrome(product):
                currentMax = (product > currentMax) and product or currentMax
        else:
            upper_j -= 11 # prevent repeating the multiplication from last loop
            break

print(currentMax)


logging.debug('End of program.\n\n\n')

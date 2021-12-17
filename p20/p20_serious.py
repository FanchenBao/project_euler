#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

from math import factorial

''' 
A serious solution.
'''

factorial_100 = [0] * 200 # result of 100! cannot be more than 200 digits long
factorial_100[-1] = 1 # initialize at 1
lenDigits = 1 # len of the digits of each new product

for i in range(2, 101):
    carry = 0
    j = -1
    while(1):
        sigma = factorial_100[j] * i + carry # product of each digit
        factorial_100[j] = sigma % 10 # unit digit value
        carry = sigma // 10
        if carry == 0 and lenDigits < (-j): # when current digit size surpass the previous and carry reduced to 0, break the current multiplication
            break
        j -= 1
    lenDigits = -j

print(sum(factorial_100))



# runtime = 0.006 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

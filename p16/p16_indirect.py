#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

from math import log10

''' This is the solution before I knew Python has no limit in the size of integer. I am pleasantly surprised.'''
power = 1000

length = int(power * log10(2) + 1)
results = [0] * length # record the result of each multiplication
results[-1] = 2
carry = 0 # the carry after the multiplication of each digit

for i in range(2, power + 1):
    for j in range(-1, -length - 1, -1):
        sigma = results[j] * 2 + carry
        results[j] = sigma % 10
        carry = sigma // 10
    carry = 0

print("The result is:")
for digit in results:
    print(digit, end = '')
print('')
print("The sum of digits is: {}".format(sum(results)))



# runtime = 0.2 s


print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

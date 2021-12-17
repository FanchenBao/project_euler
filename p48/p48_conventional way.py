#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Relying on the multiplication of Python because 10 digit multiplying 2 or 3 digits is wel within Python's capability
'''

def firstTenDigits(num):
    ''' calculate the first 10 digits of n to the power of n'''
    res = num
    for i in range(num - 1):
        res *= num
        if res > 10000000000:
            res %= 10000000000

    return res

ans = 0
for i in range(1, 1001):
    if i % 10:
        ans += firstTenDigits(i)

print(str(ans)[-10:])

# runtime = 0.14 s

print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

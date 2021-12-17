#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Manually calculat the first ten digits of n^n without relying on repeated multiplicaton of n onto itself.
Not sure why I did it this way, because a program can definitely handle 10 digit multiplication.
There is no need to break down the multiplication process.
'''

def firstTenDigits(num):
    ''' calculate the first 10 digits of n to the power of n'''
    res = num
    for i in range(num - 1):
        count = 0
        currentRes = 0
        n = num
        while(n):
            digit = n % 10
            temp = digit * res # multiply each digit to the previous product
            strTemp = str(temp)
            size = len(strTemp)
            # take only the first 10 digits
            if size > 10 - count:
                temp = int(strTemp[-(10-count):]) * 10**count
            else:
                temp *= 10**count
            currentRes += temp # increment the current result with the product from each digit
            count += 1
            n //= 10
        res = currentRes

    return res

ans = 0
for i in range(1, 1001):
    if i % 10:
        if i < 10:
            ans += i ** i
        else:
            ans += firstTenDigits(i)

print(str(ans)[-10:])




# runtime = 2.02 s

print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

import math

''' 
Faster brute force. Take advantage of the bucket method to make checking whether a number is in the list of the abundant numbers much faster
'''
def sumDivisor(num):
    ''' calculate the sum of the proper divisors of number n'''
    n = num
    res = 1
    current_term = 1
    current_sum = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        while (n % i == 0):
            current_term *= i
            current_sum += current_term
            n //= i
        res *= current_sum
        current_term = 1
        current_sum = 1

    # upon exit the previous for loop, n must be a prime number or 1
    if n >= 2:
        # num is prime
        res *= (1 + n)
    return (res - num)

abundantNums = []
abundantNumsBuckets = [0] * 28124
res = 0

for i in range(1, 28124):
    if sumDivisor(i) > i:
        abundantNums.append(i)
        abundantNumsBuckets[i] = 1 # create the bucket

for i in range(1, 28124): # check every number to see if it can be expressed as the sum of two abundant numbers
    j = 0
    while((i // 2) >= abundantNums[j]): 
        if (abundantNumsBuckets[(i - abundantNums[j])]): # number i can be expressed
            break
        else:
            j += 1
    if ((i // 2) < abundantNums[j]): # number i cannot be expressed
        res += i

print(res)




# runtime = 2.4 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

''' wihtout using the permutation function from itertools'''
import math

nums = list(range(10))
target = 1000000
res = []

while(1):
    perm = math.factorial(len(nums) - 1)
    if target >= perm:
        quotient = target // perm
        remainder = target % perm
        if remainder > 0:
            res.append(nums[quotient])
            del nums[quotient]
        else:
            res.append(nums.pop(quotient - 1))
            nums.reverse()
            for num in nums:
                res.append(num)
            break
        target = remainder

    else:
        res.append(nums.pop(0))

length = len(res)
result = 0
for i in range(length):
    result += res[i] * (10 ** (length - 1))
    length -= 1

print(result)

# runtime = 0.001 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

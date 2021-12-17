#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

from math import sqrt

''' 
THE NATURAL LOOPING ALGORITHM
Utilize the fact that prime number candidates can be expressed as 6k + 1 or 6k - 1 (basically not divisible by 2 and 3).
In the main loop, start from 5, which is 6 * 1 - 1. Then check the next number 5 + 2 which is 6 * 1 + 1.
Then check the next candidate 6 * 2 - 1, which is the previous one plus 4. After this, repeat.
This strategy is used also in the isPrime() function where a candidate is divided by all the other candidates, rather than just odd numbers.
'''

def isPrime(n):
    i = 5
    while (i < sqrt(n) + 1):
        if not (n % i):
            return 0
        if not (n % (i + 2)):
            return 0
        i += 6
    return 1

result = 5
i = 5
limit = 2000000

while(i < limit):
    if isPrime(i):
        result += i
    i += 2
    if (i < limit) & (isPrime(i)):
        result += i
    i += 4

print(result)

# time to finish is about 12 seconds when the laptop is fresh. Quite slow



print("Time: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

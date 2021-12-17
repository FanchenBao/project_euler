#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
The problem itself is not complex, but the tricky part is to set the range for searching optimally.
We know that the first digit cannot be 2, otherwise 6x would lead to a higher digit-length number.
So the upper limit for each group of numbers with certain digit-length is:
    10^(digit) // 6
And since 3x the number has the same digit as the original number, the original number must also be divisible by 3 (sum of digits divisible by 3).
Thus the lower limit must be the smallest multiple of 3 in the group of numbers with certain digit-length:
    10^(digit-1) // 3 * 3 + 3
Finally, the stepping should be 3.

This can cut searching space much smaller.
'''

digit = 3
maxMultiple = 6
while(1):
    found = 0
    # for each given digit-length of number, give range for search
    for n in range(10**(digit - 1) // 3 * 3 + 3, 10**(digit) // maxMultiple, 3):
        standard = ''.join(sorted(list(str(n))))
        for multiples in range(2, maxMultiple + 1):
            if ''.join(sorted(list(str(multiples * n)))) != standard:
                break
        else:
            found = 1
            print(n)
            break
    if found:
        break
    digit += 1

# runtime = 0.08 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

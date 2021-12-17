#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Solution by hand is as follows.
d1 = 1
d10: quotient = (10 - 9) // 2 = 0, remainder = 1. So the number right before the digit is 9 + 0 = 9. Remainder 1 means the digit is right after 9, which is 1. So d10 = 1.
d100: quotient = (100 - 9) // 2 = 45, r = 1. The number right before is 9 + 45 = 54. So d100 = 5.
d1000: q = (1000 - 9 - 90 * 2) // 3 = 270, r = 1. The number right before is 99 + 270 = 369, so d1000 = 3
d10000: q = (10000 - 9 - 90 * 2 - 900 * 3) // 4 = 1777, r = 3. Number right before: 999 + 1777 = 2776, so d10000 = 7
d100000: q = (100000 - 9 - 90 * 2 - 900 * 3 - 9000 * 4) //  5 = 12222, r = 1. Number right before: 9999 + 12222 = 22221, so d100000 = 2
d1000000: q = (1000000 - 9 - 90 * 2 - 900 * 3 - 9000 * 4 - 90000 * 5) // 6 = 85185, r = 1. Number right before: 99999 + 85185 = 185184, so d1000000 = 1.

Result = 1 * 1 * 5 * 3 * 7 * 2 * 1 = 210

Now trying to do it with brute force. Mininum space but with potential sacrifice in performance
'''

ans = 1
count = 0
n = 1
targets = {1, 10, 100, 1000, 10000, 100000, 1000000}

while(1):
    strNum = str(n)
    for i in range(len(strNum)):
        count += 1 # count each digit
        if count in targets:
            ans *= int(strNum[i])
    if count >= 1000000:
        break
    n += 1

print(ans)





# runtime = 0.4 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

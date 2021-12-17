#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Let the current spiral size by n, then the previous spiral size is n - 2.
It is easy to notice that the top right number is n^2.
The bottom right number is (n - 2)^2 + (n - 1) = n^2 -3n + 3
The bottom left number is (n - 2)^2 + 2(n - 1) = n^2 -2n + 2
And the top left number is (n - 2)^2 + 3(n - 1) = n^2 - n + 1
Thus the sum of four corners of a spiral size n is S(n) = 4n^2 -6n + 6
The diagonal sum D(n) = S(3) + S(5) + ... + S(1001) + 1

This can be solved by a loop or by hand.
'''

# loop method
D = 1
for i in range(3, 1002, 2):
    D += 4 * i * i - 6 * i + 6

print(D)

# runtime = 0.5 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

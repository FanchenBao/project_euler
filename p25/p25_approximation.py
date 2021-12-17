#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

''' using the approximation method of Binet's formula to calculate Fibonacci number quickly, then check its digits.
    Decimal module is used to prevent float precision overflow

    reference: http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibFormula.html
'''

import math
from decimal import *

getcontext().prec = 1000

Phi = Decimal((math.sqrt(5) + 1) / 2)
i = 1

while(1):
    fibo = round((Phi ** i) / Decimal(math.sqrt(5)))
    if (int(math.log10(fibo)) + 1) == 1000:
        print("The {}th Fibonacci number {} has 1000 digits".format(i, int(fibo)))
        break
    i += 1



# runtime = 0.97 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

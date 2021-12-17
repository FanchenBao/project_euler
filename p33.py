#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
There are in total 4 situations for a fraction of a1a2/b1b2 after eliminatiing one digit from both numerator and denominator.
situation1: a2 = b2 and eliminated, thus a1a2/b1b2 = a1/b1 --> a1 = b1. However, since a1/b1 < 1, contradiction
situation2: a1 = b1 and eliminated, thus a1a2/b1b2 = a2/b2 --> a2 = b2. However, since a2/b2 < 1, contradiction
situation3: a2 = b1 and eliminated, thus a1a2/b1b2 = a1/b2 --> a2 = b1 = 9a1b2/(10a1-b2). Brute force this to find a1, b2 pair that makes the equation value to integer.
situation3: a1 = b2 and eliminated, thus a1a2/b1b2 = a2/b1 --> a2 = b1 = 9a2b1/(10b1-a2). Brute force this to find a2, b1 pair that makes the equation value to integer.
'''
from fractions import Fraction

def situation3():
    ''' a1a2/b1b2 = a1/b2 '''
    productNum = 1
    productDen = 1
    for a in range(1, 9):
        for b in range(2, 10):
            if (a < b):
                c = 9 * a * b / (10 * a - b)
                if c < 10 and c == int(c):
                    numerator = 10 * a + int(c)
                    denominator = 10 * int(c) + b
                    productNum *= numerator
                    productDen *= denominator
    if productNum != 1 and productDen != 1:
        return (productNum, productDen)
    else:
        return 0
                
def situation4():
    ''' a1a2/b1b2 = a2/b1 '''
    productNum = 1
    productDen = 1
    for a in range(1, 9):
        for b in range(2, 10):
            if (a < b):
                c = 9 * a * b / (10 * b - a)
                if c < 10 and c == int(c):
                    numerator = 10 * int(c) + a
                    denominator = 10 * b + int(c)
                    productNum *= numerator
                    productDen *= denominator
    if productNum != 1 and productDen != 1:
        return (productNum, productDen)
    else:
        return 0

res3 = situation3()
res4 = situation4()

if res3 == 0 and res4:
    resNum = res4[0]
    resDen = res4[1]
elif res4 == 0 and res3:
    resNum = res3[0]
    resDen = res3[1]
elif res3 and res4:
    resNum = res3[0] * res4[0]
    resDen = res3[1] * res4[1]
else:
    print("Error!")

print(Fraction(resNum, resDen).denominator)

# runtime = 0.02 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

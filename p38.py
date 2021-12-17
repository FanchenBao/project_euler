#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
From mathematic analysis, we can make the following conclusions:

integer is 1-digit, max of n is 9. We can deduce the results as:
  1 and (1-9) = 123456789
  9 and (1-5) = 918273645
integer is 2-digit, n can only be 4, and the digits of each product is 2, 2, 2, 3
integer is 3-digit, n can only be 3, and the digits of each product is 3, 3, 3
integer is 4-digit, n can only be 2, and the digits of each product is 4, 5

Furthermore, the number to beat is 918273645. Thus any integer times 1 must result in at least a 9 in the first digit of the product.
Thus, for 2-, 3-, and 4-digit situation, search should start with 90, 900, and 9000, respectively.
'''

def getPandigits(digit, maxPandigits):
    ''' deal with the 2-, 3- and 4-digit situation'''
    for i in range(10**(digit - 1) * 9, 10**digit):
        product = ""
        if digit == 2:
            if i * 4 >= 100 and i * 2 < 100:
                for j in range(4):
                    product += str(i * (j + 1))

        elif digit == 3:
            if i * 3 < 1000 and i * 2 < 1000:
                for j in range(3):
                    product += str(i * (j + 1))
        else:
            if i * 2 >= 10000:
                for j in range(2):
                    product += str(i * (j + 1))
        sortedProduct = ''.join(sorted(product))
        if sortedProduct == "123456789":
            print("{} x (1-{}) = {}".format(i, digit, product))
            if product > maxPandigits:
                maxPandigits = product
    return maxPandigits

maxPandigits = "918273645"
for i in range(2, 5):
    maxPandigits = getPandigits(i, maxPandigits)    


print("Largest pandigital multiples is: {}".format(maxPandigits))




# runtime = 0.003 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
The only possibilities are 1-digit x 4-digit = 4-digit and 2-digit x 3-digit = 4-digit.
So run the function twice with different digit requirements. All possible multiplications are:
4 x 1738 = 6952
4 x 1963 = 7852
12 x 483 = 5796
18 x 297 = 5346
27 x 198 = 5346
28 x 157 = 4396
39 x 186 = 7254
42 x 138 = 5796
48 x 159 = 7632
'''

def findSum(digit1, digit2, productDict):
    ''' find the sum of all target numbers given the number of digits of the multiplicand and multiplier'''
    sigma = 0
    for i in range(10**(digit1 - 1), 10**digit1):
        for j in range(10**(digit2 - 1), 10**digit2):
            product = i * j
            if product < 10000:
                candidate = ""
                # combine multiplicant, multiplier and product into one string with all digits in order
                for ele in sorted(str(i) + str(j) + str(product)):
                    candidate += ele
                # compare with a string containing 1-9. If match, then we have found a target number
                if candidate == '123456789':
                    print("{} x {} = {}".format(i, j, product))
                    if product not in productDict:
                        productDict[product] = True
                        sigma += product
            else:
                break
    return sigma

productDict = {}
print(findSum(1, 4, productDict) + findSum(2, 3, productDict))


# runtime = 0.11 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

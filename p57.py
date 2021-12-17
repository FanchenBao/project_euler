#! /usr/bin/env python3
import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Author: Fanchen Bao
Date: 09/19/2018

Project Euler: Problem 57

Solution: 
  Brute force. But have to implement my own fraction number representation class
'''
import math

class FractionNum:
    ''' represent number in its fraction form '''
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def add(self, addend):
        ''' addend is another FractionNum object'''
        newDen = self.den * addend.den // math.gcd(self.den, addend.den)
        newNum = newDen // self.den * self.num + newDen // addend.den * addend.num
        return FractionNum(newNum, newDen)

    def inverse(self):
        ''' return a FractionNum that is inversed'''
        return FractionNum(self.den, self.num)

    def display(self):
        print('{}/{}'.format(self.num, self.den))

    def intoStr(self):
        ''' turn the resulting fraction into str form'''
        return str(self.num) + '/' + str(self.den)

# driver
count = 0
resDeci = FractionNum(1, 2) # store the decimal portion of the estimate
for i in range(2, 1001):
    resDeci = resDeci.add(FractionNum(2, 1)).inverse()
    if not len(resDeci.add(FractionNum(1, 1)).intoStr()) % 2: # add one to get the actual result
    # and check whether the length of output string is odd or even
        count += 1 

print(count)

# runtime = 0.01 s


print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

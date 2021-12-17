#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

from math import log10

NumLetters = {
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10 : 'ten',
    11 : 'eleven',
    12 : 'twelve',
    13 : 'thirteen',
    14 : 'fourteen',
    15 : 'fifteen',
    16 : 'sixteen',
    17 : 'seventeen',
    18 : 'eighteen',
    19 : 'nineteen',
    20 : 'twenty',
    30 : 'thirty',
    40 : 'forty',
    50 : 'fifty',
    60 : 'sixty',
    70 : 'seventy',
    80 : 'eighty',
    90 : 'ninety',
    100 : 'hundred',
    1000 : 'thousand'
}

def numToLetters(num, NumLetters, numDigits):
    n = num
    if n in NumLetters.keys():
        result = len(NumLetters[n])
        if (n == 100 or n == 1000):
            result += 3
        return result
    
    result = 0
    digits = [0] * numDigits

    for i in range(-1, -numDigits - 1, -1):
        digits[i] = n % 10
        n //= 10

    for i in range(numDigits):
        if digits[i]: # when a digit is 0, e.g. 205, the 0 is not considered
            powerTen = int(10**(numDigits - i - 1))
            temp = digits[i] * powerTen
            if temp == 10: # dealing with last two digits 10-19, since they have different word rules compared to other two digit numbers
                result += len(NumLetters[temp + digits[i + 1]])
                break
            if temp in NumLetters.keys():
                result += len(NumLetters[temp])
                if (temp == 100): # dealing with the 100 in numbers 101 to 199
                    result += 3
            else:
                result += len(NumLetters[digits[i]]) + len(NumLetters[powerTen])

    if ((numDigits == 3) and (num % 100)): # deal with "and" in three digit number
        result += 3
    return result

    
sigma = 0

for n in range(1000):
    numDigits = int(log10(n + 1)) + 1
    sigma += numToLetters(n + 1, NumLetters, numDigits)
        
print(sigma)

# print(numToLetters(114, NumLetters, 3))

# runtime = 0.2 s


print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

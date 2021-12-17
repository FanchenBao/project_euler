#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

from math import log10

NumLetters = {
    0 : '',
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
    100 : 'hundred'
}

def numToLetters(num, NumLetters, numDigits):
    n = num
    result = 0
    digits = [0] * 3

    for i in range(-1, -numDigits - 1, -1):
        digits[i] = n % 10
        n //= 10

    if digits[0]: # deal with three digit number
        result += len(NumLetters[digits[0]]) + len(NumLetters[100])
        if num % 100: # add 3 letters of "and" if num is not divisible by 100
            result += 3
    if digits[1]: # deal with the remaining two digit number
        if digits[1] == 1: # teens are delt with separatedly
            result += len(NumLetters[num - 100 * digits[0]])
        else:
            result += len(NumLetters[10 * digits[1]]) + len(NumLetters[digits[2]])
    elif digits[2]: # deal with single digit number
        result += len(NumLetters[digits[2]])

    return result

    
sigma = 11 # for one thousand

for n in range(999):
    numDigits = int(log10(n + 1)) + 1
    sigma += numToLetters(n + 1, NumLetters, numDigits)
        
print(sigma)


# runtime = 0.005 s


print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

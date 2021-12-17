#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

from math import log10

'''
0! = 1
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
6! = 720
7! = 5040
8! = 40320
9! = 362880

The possible number of digits for the curious number:
1-digit: DNE
2-digit: digit must come from 0-4
3-digit: digit must contain either one 6 and the rest 0-5, or all of them 0-5
4-digit: digit must contain either one 7 and the rest 0-6, or all of them 0-6
5-digit: digit must contain either one or two 8 and the rest 0-7, or all of them 0-7
6-digit: digit must contain either one or two 9 and the rest 0-8, or all of them 0-8
7-digit: digit must contain at least three 9, and the rest 0-8
8-digit or above: DNE. Thus the upperboundary is 9! * 7 = 2540160

The first attempt is to include all the digit boundary checks. The second attempt is brute force all numbers (inspired by Begoner). The two methods yield similar run time.
It is worth noting that in order to do boundary check, the first attempt requires ordering of the digits. 
The time spent on creating the ordered list cancels out the time saved by doing boundary checks. Thus the two attempts have similar run time.
'''

def getDigits(n, numDigit):
    ''' get each digit from a number n'''
    digits = [0] * numDigit
    for i in range(numDigit):
        digits[i] = n % 10
        n //= 10
    return digits

def attempt1(facts):
    sigma = 0
    for i in range(10, facts[9] * 7):
        numDigit = int(log10(i)) + 1
        digits = sorted(getDigits(i, numDigit))
        if numDigit <= 2:
            if digits[-1] > 4:
                continue
        elif numDigit < 5:
            if numDigit == 3 and digits[-2] == 6:
                continue
            if numDigit == 4 and digits[-2] == 7:
                continue
        elif numDigit < 7:
            if numDigit == 5 and digits[-3] == 8:
                continue
            if numDigit == 6 and digits[-3] == 9:
                continue
        else:
            if digits[-3] != 9:
                continue
        sumFact = sum(facts[d] for d in digits)
        if sumFact == i:
            print(i)
            sigma += i

    return sigma

def attempt2(facts):
    sigma = 0
    for i in range(10, facts[9] * 7):
        strDigits = str(i)
        sumFact = sum(facts[int(d)] for d in strDigits)
        if sumFact == i:
            print(i)
            sigma += i

    return sigma

facts = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]



print("The sum is {}".format(attempt2(facts)))

# runtime = 8 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

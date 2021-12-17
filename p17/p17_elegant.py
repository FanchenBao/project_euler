#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''This is more elegant method fully taking advantage of the dictionary structure.'''

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
}

for n in range(1000):
    if not (n + 1) in NumLetters.keys():
        if (n + 1) < 100:
            NumLetters[n + 1] = NumLetters[(n + 1) - (n + 1) % 10] + NumLetters[(n + 1) % 10]
        elif (n + 1) < 1000:
            if (n + 1) % 100:
                NumLetters[n + 1] = NumLetters[(n + 1) // 100] + 'hundredand'+ NumLetters[(n + 1) % 100]
            else:
                NumLetters[n + 1] = NumLetters[(n + 1) // 100] + 'hundred'
        else:
            NumLetters[n + 1] = 'onethousand'


print(sum([len(text) for text in NumLetters.values()]))


# runtime = 0.002 s


print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

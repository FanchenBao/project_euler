#! /usr/bin/env python3
import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Author: Fanchen Bao
Date: 09/24/2018

Project Euler: Problem 59

Solution: 
  Brute force. Set up all possible key combinations. Try each one.
Guess that if some weird character shows up, that key must not be correct.
Once a full decryption does not return any weird character, check whether space and 'the' is in the text.

'''

def XOR(x, y):
    ''' return the value after integer x XOR integer y.
        x | y returns a value with only one situation not correct: when the bit in x and y are both set
        ~x | ~y returns a value with all bits set except for those where both x and y are set (these bits are now 0)
        The AND value of these two reset the 1 in original x | y where both x and y are set
    '''
    return (x | y) & (~x | ~y)

# prepare the encrypted characters
with open("p059_cipher.txt") as file_obj:
    contents = file_obj.read()
encryptChars = contents.rstrip().split(',')

# set up all combinations of keys
keys = [[first, second, third] for first in range(97, 123) for second in range(97, 123) for third in range(97, 123)]

for key in keys:
    res = []
    i = 0
    badKey = 0
    sigma = 0
    for char in encryptChars:
        decipher = int(char)^key[i] # decipher each character
        if (decipher >= 0 and decipher <= 31) or (decipher > 122) or (decipher in {35, 36, 37, 38, 94, 64, 91, 92, 93, 96}):
            # guess that these characters won't appear in the text
            badKey = 1
            break
        res.append(chr(decipher))
        sigma += decipher
        i = (i + 1) % 3 # loop over the three values in the key
    if not badKey:
        strRes = ''.join(res)
        if "the" in strRes and " " in strRes:
            print(strRes)
            print("key is:", key)
            print("sum is {}".format(sigma))
            break # there is only one encrypted text


# runtime = 0.05 s


print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

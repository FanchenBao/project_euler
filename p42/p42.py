#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Create a dict for the number representation of each letter.
Create another dict for triangle numbers up to 15 * 26 = 390 (guess that the largest value a common word can have would be smaller than 15 Z)
'''

with open ("p042_words.txt") as file_obj:
    contents = file_obj.read()
lines = contents.split(',')

# note that the double quotatioin mark is also made into letterNums but assigned the value of 0
letterNums = {}
for i in range(26):
    letterNums[chr(65 + i)] = i + 1 # chr() turns an ascii decimal to its character. ord() turns a char into ascii decimal
letterNums['"'] = 0

triangleNums = {}
for i in range(1, 29):
    triangleNums[i * (i + 1) // 2] = True

count = 0
for word in lines:
    if sum([letterNums[le] for le in word]) in triangleNums:
        print(word)
        count += 1

print(count)


# runtime = 0.006 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

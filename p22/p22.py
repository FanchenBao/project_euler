#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

''' 
key is to use string.ascii_uppercase and ord() function to construct a dict for alphabetical value
'''

import string

# read in the file
filename = "p022_names.txt"
with open(filename) as f_obj:
    content = f_obj.read()

names = sorted([name.strip('"') for name in content.split(',')])

# ord() returns a char's ascii number. mod32 gets a letter's alphabetical value
letter2Num = dict(list(zip(string.ascii_uppercase, [ord(letter) % 32 for letter in string.ascii_uppercase])))

res = sum([(i + 1) * sum([letter2Num[let] for let in names[i]]) for i in range(len(names))])
print(res)

# runtime = 



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

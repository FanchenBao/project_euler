#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

result = 0
for i in range(100):
    result += (i + 1)**3 - (i + 1)**2 # recognize that square of sum equals sum of cubes

print(result)


logging.debug('End of program.\n\n\n')

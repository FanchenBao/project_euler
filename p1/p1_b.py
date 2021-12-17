#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')




def calSum(n):
	return ((n < 3) and [0] or [(calSum(n - 1) + ((n % 3) and [((n % 5) and [0] or [n])[0]] or [n])[0])])[0]

print(calSum(1000 - 1))


logging.debug('End of program.\n\n\n')

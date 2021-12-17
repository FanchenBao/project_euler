#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')



f1 = 1; f2 = 2; currentF = 0; result = 2

while (currentF < 4000000):
	currentF = f1 + f2
	result += ((currentF % 2) and [0] or [currentF])[0]
	f1 = f2
	f2 = currentF

print(result)



logging.debug('End of program.\n\n\n')

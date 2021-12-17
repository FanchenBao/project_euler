#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')


def calSum(f1, f2):
	if f2 >= 4000000:
		return 2
	else:
		currentF = f1 + f2
		return (((currentF % 2) and [0] or [currentF])[0] + calSum(f2, currentF))

print(calSum(1, 2))



logging.debug('End of program.\n\n\n')

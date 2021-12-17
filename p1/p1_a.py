#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')



print(sum([(((i + 1) % 3) and [(((i + 1) % 5) and [0] or [i + 1])[0]] or [i + 1])[0] for i in range(1000 - 1)]))



logging.debug('End of program.\n\n\n')

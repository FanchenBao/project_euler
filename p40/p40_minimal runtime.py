#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Try this one with minimal runtime
'''

champ = ""
for i in range(1, 185185 + 1): # 185185 is the upperbound number for the 1 millionth digit. 
                            # it's calculated as (1000000 - 488889) // 6 + 99999 + 1, where 488889 is the number of digits till number 99999
    champ += str(i)

ans = int(champ[0]) * int(champ[9]) * int(champ[99]) * int(champ[999]) * int(champ[9999]) * int(champ[99999]) * int(champ[999999])
print(ans)

# runtime = 0.1 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

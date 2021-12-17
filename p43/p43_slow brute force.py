#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
User permutation and two sets of restricting conditions (d4 has to be even and d6 has to be 5) to create a pool of candidates.
Then screen the divisibility of the candidates with the primeList.
The creation and looping through candidate pool is very time consuming. Not a good method
'''
from itertools import permutations

primeList = [17, 13, 11, 7, 5, 3, 2]
ans = 0

for digitList in list(permutations("0123456789")):
    if digitList[3] in {'0', '2', '4', '6', '8'} and digitList[5] == '5':
        candidate = ''.join(digitList)
        start = 7
        isGood = 1
        for i in range(7):
            if not int(candidate[start:start + 3]) % primeList[i]:
                start -= 1
            else:
                isGood = 0
                break
        if isGood:
            print(candidate)
            ans += int(candidate)

print(ans)


# runtime = 1.8 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

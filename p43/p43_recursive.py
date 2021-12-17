#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Use recursive to build the number up from LSB to MSB.
Restricting conditions: d6 = 5, d4 = even
'''
def isTarget(primeList, i, usedDigit, candidate, candidates):
    ''' decide whether a number is one of the target pandigital number'''
    if i == 7:
        for d in range(10):
            if not usedDigit[d]:
                candidates.append(int(str(d) + candidate))
        return candidates

    else:
        for d in range(10):
            # digit available and the substring divisible
            if not usedDigit[d] and not int(str(d) + candidate[:2]) % primeList[i]:
                usedDigit[d] = 1
                # candidate and i CANNOT be changed in the loop, but in the function invocation
                isTarget(primeList, i + 1, usedDigit[:], str(d) + candidate, candidates)
                # set the digit used back to FALSE because for the next loop iteration, the current digit should be available 
                usedDigit[d] = 0
        return candidates
        

primeList = [17, 13, 11, 7, 5, 3, 2]
candidates = []

for i in range(6, 59):
    candidate = str(17 * i)
    # no repeats, no coexistence of 0 and 5 in the last three digits
    if candidate[0] == candidate[1] or candidate[0] == candidate[2] or candidate[1] == candidate[2] or '5' in candidate:
        continue
    else:
        # initialize current usedDigit
        usedDigit = [0] * 10
        for digit in candidate:
            usedDigit[int(digit)] = 1

        candidates = isTarget(primeList, 1, usedDigit, candidate, candidates)

for can in candidates:
    print(can)
        
print("The sum is {}".format(sum(candidates)))


# runtime = 0.001 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

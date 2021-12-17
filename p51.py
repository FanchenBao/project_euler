#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
No proof yet, but I would like to bet the answer must be a 6- or more digit prime with replacement of 3 digits
On the other hand, since the requirement is to have 8 prime value, so the smallest one contain either 0, 1, or 2 for the digits to be replaced.
Thus, we will look for candidates with 3 repeats of 0, 1, or 2 in all the digits but thee last one.
'''

from itertools import combinations

def primeSieve(n):
    ''' return raw prime after the sieve, up to n - 1'''
    rawPrime = [1] * n
    rawPrime[0] = 0
    rawPrime[1] = 0
    for i in range(4, n , 2):
        rawPrime[i] = 0
    i = 3
    while i * i < n:
        j = i
        while i * j < n:
            rawPrime[i * j] = 0
            j += 2
        i += 2
    return rawPrime

def findRepeats(n, numPrime):
    ''' find which one of first 10 - numPrime digits (e.g. if numPrime = 7, the repeated digits are 0, 1, 2, or the first 3 digits) in n that repeats.'''
    strNum = str(n)
    repeatPosDict = {}
    for i in range(10 - numPrime + 1):
        repeatPosDict[i] = []
    for i in range(len(strNum)):
        for j in range(10 - numPrime + 1):
            if strNum[i] == str(j):
                repeatPosDict[j].append(i)
    return repeatPosDict # repeatPosDict records the positions of repated digits

def replaceNum(replacePos, prime, replacement):
    '''replacePos is a tuple containing the positions for replacement.
        prime is the current prime to be replaced.
        replacement is the number to swap in at the replacePos.
    '''
    numList = list(str(prime))
    for pos in replacePos:
        numList[pos] = str(replacement)
    return int(''.join(numList))

def findTargetFirstPrime(rawPrime, primeList, repeatTime, numPrime):
    ''' given the range for prime, the number of repeats in digit, and legnth of the prime number sequence,
        find the first prime of the prime value family
    '''
    for prime in primeList:
        target = prime // 10 # last digit cannot be changed
        repeatPosDict = findRepeats(target, numPrime)
        for k, v in repeatPosDict.items():
            if len(v) >= repeatTime: # candidate for digit replacement
                for replacePos in combinations(v, repeatTime): # all combinations of positions for change            
                    count = 1 # count already one because the current prime is the first one
                    for replacement in range(k+1, 10): # replace with the following digits
                        if rawPrime[replaceNum(replacePos, prime, replacement)]:
                            count += 1
                    if count == numPrime: # found it
                        print(prime)
                        return 1
    return 0  


n = 1000000 # guess the prime is betweeen n/10 and n. Starting guess is 6 digit number
repeatTime = 3 # number of digits to replace (i.e. repeat digits). Starting guess is 3 repeats
numPrime = 8 # length of the prime sequence

while(1):
    found = 0
    while(repeatTime < len(str(n))):
        rawPrime = primeSieve(n)
        primeList = []
        for i in range(n//10, n):
            if rawPrime[i]:
                primeList.append(i)
        if findTargetFirstPrime(rawPrime, primeList, repeatTime, numPrime):
            found = 1
            break
        else:
            repeatTime += 1
    if found:
        break
    else:
        n *= 10
       



# runtime = 0.5 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Let j <= k, and the sum Pl = Pj + Pk. Let l = k + m, then Pl = (k + m)(3k + 3m - 1)/2
Pj = Pl - Pk = (k + m)(3k + 3m - 1)/2 - m(3m - 1)/2 = 3mk + m(3m - 1)/2
Thus, for each Pk, Pj can be the value for m = 1, 2, 3... as long as Pj <= Pk.
Then check whether each Pj is pentagonal and whether Pk - Pj is pentagonal. 
The first such Pj, Pk pair should be the answer, because Pk - Pj seems to increase as k gets bigger.
(I can only prove that for a certain m, Pk - Pj increases with k; but for different m as k increases, I have no proof that Pk - Pj also increases)
'''

def p44():
    pentagonalDict = {}
    k = 1
    while(k < 5000):
        Pk = k * (3 * k - 1) // 2
        pentagonalDict[Pk] = True
        m = 1
        while(1):
            Pj = 3 * m * k + m * (3 * m - 1) // 2
            if Pj > Pk: break
            if Pj in pentagonalDict and (Pk - Pj) in pentagonalDict:
                print("k = {}, Pk = {}, Pj = {}, Pk + Pj = {}, Pk - Pj = {}".format(k, Pk, Pj, Pk + Pj, Pk - Pj))
                return # believe that the first pair found has the smallest difference
            m += 1
        k += 1


p44()

# runtime = 0.4 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

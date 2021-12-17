#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

''' Using the quick brute force method (by Prof. Edsgar W Dijkstra) to calculate each Fibo number.
    reference: http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibFormula.html
'''
import math

def calFibo(i, Fibos):
    ''' calculate the ith fibo'''
    if (Fibos[i] >= 0):
        return Fibos[i]
    else:
        if (i % 2 == 1):
            FNmin1 = calFibo((i + 1) // 2 - 1, Fibos)
            FN = calFibo((i + 1) // 2, Fibos)
            Fibos[i] = (FNmin1)**2 + (FN)**2
        else:
            FNmin1 = calFibo(i // 2 - 1, Fibos)
            FN = calFibo(i // 2, Fibos)
            Fibos[i] = (2 * FNmin1 + FN) * FN

upperLim = 10000
Fibos = [-1] * upperLim
Fibos[0] = 0
Fibos[1] = 1
for i in range(1, upperLim):
    calFibo(i, Fibos) # calculate each fibo
    if (int(math.log10(Fibos[i])) + 1) == 1000:
        break

print(i)

# runtime = 0.025 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

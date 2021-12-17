#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Create the 1001 by 1001 spiral, find all the diagonal numbers along the way, and calculate the sum. Straightforward brute force
'''

side = 1001
spiral = [[0] * side for i in range(side)]
# i and j are indices for spiral, set them to the center
i = (side - 1) // 2
j = i
num = 1
spiral[i][j] = num

sumDiagonal = 1

# spiral size increase from 3 to target side, all odd number
for spiralSize in range(3, side + 1, 2):
    # current top right indices are based on the previous top right coordinates
    topRightI = i - 1
    topRightJ = j + 1
    while(j < topRightJ):
        num += 1
        j += 1
        spiral[i][j] = num
    while(i < topRightI + spiralSize - 1):
        num += 1
        i += 1
        spiral[i][j] = num
    sumDiagonal += num # diagonal
    while(j > topRightJ - spiralSize + 1):
        num += 1
        j -= 1
        spiral[i][j] = num
    sumDiagonal += num # diagonal
    while(i > topRightI):
        num += 1
        i -= 1
        spiral[i][j] = num
    sumDiagonal += num # diagonal
    while(j < topRightJ):
        num += 1
        j += 1
        spiral[i][j] = num
    sumDiagonal += num # diagonal


print(sumDiagonal)

# runtime = 0.5 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

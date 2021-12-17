#! /usr/bin/env python3
import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Author: Fanchen Bao
Date: 09/28/2018

Project Euler: Problem 61

Solution: 
  range of n for each polygonal number that is 4-digit
Oct:    [19, 57]
Hept:   [21, 63]
Hex:    [23, 70]
Pen:    [26, 81]
Square:  [32, 99]
Tri:    [45, 140]
  Start with Oct number, each one can grow to the right (last two digits being the first two digit of other polygonal number).
Search for all other polygonal numbers, if there is any fit, keep going down that route. If not, return back and find again.
  This is a typical recursion.
'''

def findCycNums(currGroup, currNum, uncheckedPoly, polygonals):
    ''' recursively find all six cyclic numbers among the polygonals that satisfies the requirement
        The function looks to the right of currNum, i.e. find other polygonal numbers that have the same first two digits as the last two digits of currNum
    '''
    if len(currGroup) == 6: # get 6 elements
        if currNum[-2:] == currGroup[0][:2]: # check whether the last number added can cycle back to the first
            print(currGroup, sum([int(num) for num in currGroup]))
            return 1
        else:
            return 0
    else:
        for poly in uncheckedPoly: # uncheckedPoly stores the index of the polygonals that haven't been checked yet
            for num in polygonals[poly]:
                if currNum[-2:] == num[:2]: # if the next cycled number found, remove the current poly index and call the function again
                    temp = uncheckedPoly[:]
                    temp.remove(poly)
                    if findCycNums(currGroup + [num], num, temp, polygonals):
                        return 1
        return 0


polygonals = [0] * 9 # array of array, storing each group of polygonal numbers, in string form
polygonals[8] = [str(n * (3 * n - 2)) for n in range(19, 58)] # oct
polygonals[7] = [str(n * (5 * n  - 3) // 2) for n in range(21, 64)] # hept
polygonals[6] = [str(n * (2 * n - 1)) for n in range(23, 71)] # hex
polygonals[5] = [str(n * (3 * n - 1) // 2) for n in range(26, 82)] # pen
polygonals[4] = [str(n * n) for n in range(32, 100)] # square
polygonals[3] = [str(n * (n + 1) // 2) for n in range(45, 141)] # tri

for num in polygonals[8]: # start from oct
    if findCycNums([num], num, [3, 4, 5, 6, 7], polygonals):
        break

# runtime = 0.004 s


print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

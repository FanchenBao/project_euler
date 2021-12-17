#! /usr/bin/env python3
import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Author: Fanchen Bao
Date: 10/22/2018

Project Euler: Problem 68
    Major change to the algorithm by fully taking advantage of the recursive power, 
and using the fact that the last number of a m-gon side is the second number of the next m-gon side. 
The new algorithm also allows for computation of the maximum solution for any odd-sided m-gon.	
'''
def findNextSide(num2, inRing, outRing, solution, sumSide, inRingStart):
    ''' recursively find the solution based on sum of the side (sumSide),
        the currently available inRing1, inRing2, and outRing;
        and the third number of previous side, which is the second number of the current side
    '''
    if not inRing: # inRing empty, that means we are on the final side:
        if outRing[0] + num2 + inRingStart == sumSide: # only one outRing remains
            solution.append((outRing[0], num2, inRingStart))
            return True
        else:
            return False
    else:   #inRing not empty, search for the current side
        temp = outRing[:]

        for i, outNum in enumerate(outRing):
            num3 = sumSide - outNum - num2 # get current num3
            if num3 in inRing: # if num3 hasn't been used yet, keep searching for next side
                solution.append((outNum, num2, num3))
                pos = inRing.index(num3)
                del inRing[pos]
                del temp[i] # need to pass the outRing list with the current outNum removed
                if findNextSide(num3, inRing, temp, solution, sumSide, inRingStart):
                    return True
                else: # current attempt failed, put num3 and outNum back (in their original order) and try next outNum
                    inRing.insert(pos, num3)
                    temp.insert(i, outNum)
                    solution.pop()
            # else, if num3 has been used or does not exist in inRing, look for the next outNum
        return False # loop through all outNum options but no solution found. Return false


def solveMagCon(inRing, outRing, outRingStart):
    ''' the program to solve the magic-con and find the maximum solution '''
    solution = []
    size = len(inRing)
    for i in range(size): # num2 and num3 represents the second and third number on the first side
        num2 = inRing[i]
        for j in range(i+1, size):
            num3 = inRing[j]
            if num2 > num3: # in order to search for the largest solution, num2 must be bigger than num3
                sumSide = outRingStart + num2 + num3
                solution.append((outRingStart, num2, num3))
                inRing.remove(num2)
                inRing.remove(num3)
                if findNextSide(num3, inRing, outRing, solution, sumSide, num2):
                    return solution
                else:
                    inRing.insert(i, num2)
                    inRing.insert(j, num3)
                    solution.pop()

# driver
numSide = 5
n = 2 * numSide
outRingStart = n - numSide + 1
inRing = [x for x in range(outRingStart - 1, 0, -1)] # inRing numbers
outRing = [x for x in range(n, outRingStart, -1)] # outRing number excluding the outRingStart
solution = solveMagCon(inRing, outRing, outRingStart)

print(solution)

# runtime = 0.001 s


print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

#! /usr/bin/env python3
import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Author: Fanchen Bao
Date: 10/02/2018

Project Euler: Problem 62

Solution: 
  All the cubes of the five permutation must have the same number of digits, and the smallest such cube must be bigger than 345^3.
Therefore, we can guess the answer can be 8, 9, or 10 digit in length
  
  base range for 8-digit cube: 346-464
  base range for 9-digit cube: 465-999
  base range for 10-digit cube: 1000-2154

  For each digit number, calculate all cubes. For each cube, sort it in ascending order and store it as key in a map. The value is an array storing the original cube associated with the key.
Once a repeated key occurs, add the original number to the array. Eventually find the key corresponding to its array with 5 entries.
  Try these three options first and see if an answer can be found.

Update: The guess was not correct. I need to keep searching further down with more digits. 
The algorithm is changed accordingly to automatically produce the range of base for each digit number.
The answer has 12 digits.
'''

limitDigits = 20 # guess the answer won't be more than 20 digits

begin = 346 # the problem specifies that 345^3 is the smallest that contains three permutated cubes
cubeMap = {}
for numDigit in range(8, limitDigits + 1): 
    end = int((10**numDigit - 1)**(1/3)) # the end range for the base whose cube's number of digit equals numDigit
    found = 0 # flag
    cubeMap.clear()
    for base in range(begin, end + 1):
        cube = base**3
        orderedCube = ''.join(sorted(list(str(cube)))) # turn cube into a stirng with all digits in ascending order
        if orderedCube in cubeMap: # find permutated cube
            cubeMap[orderedCube].append(cube)
            if len(cubeMap[orderedCube]) == 5:
                print(cubeMap[orderedCube])
                found = 1
                break
        else:
            cubeMap[orderedCube] = [cube]

    if found:
        break
    else:
        print("Target cube not found with {} digits".format(numDigit))

    begin = end + 1 # get ready for calculating next round of range


# runtime = 0.03 s


print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

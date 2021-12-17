#! /usr/bin/env python3
import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Author: Fanchen Bao
Date: 10/18/2018

Project Euler: Problem 68

Solution: Did not notice that the target is a 16-digit string. So I did it the most generic way.
The main thought is as follows: 
1. Find all 3-number groups that have the same sum, group them together into a groupList, put
in a dict under the sum as key. I call this dict rawSpace.
2. Check each groupList in rawSpace, but only process those that have more than 5 groups and
the elements in all groups span the entire range from 1 to 10.
3. Within the selected groupList, find the max solution space, which has 6-10 as outRing elements
and serve as keys to the maxSolutionSpace dict. Their values are the remaining elements of the group
where the outRing element comes from, sorted into decsending order. One outRing element can have
multiple 2-number subgroups associated with it.
4. From the maxSolutionSpace, find the solutionDict which contain 6-10 as outRing elements and keys
to the solutionDict. But here only one 2-number subgroup is associated with each outRing element.
And in total, all elements in the 2-number subgroup occurs exactly twice. For each maxSolutionSpace,
there might be multiple solutionDict that can be found.
5. Generate solution list from each solutionDict.
6. Turn solution list into string, find the largest string.
	
'''

from itertools import combinations
import copy # deepcopy()

def checkValid(groupList, numList):
    ''' determine whether groupList uses all elements in numList.
        If it does, the groupList is valid (return True). Otherwise, invalid (return False)
    '''
    combined = []
    for group in groupList:
        combined += list(group)
    return not (set(numList) - set(combined))



def findMaxSolutionSpace(groupList, n, m):
    ''' find a solutionSpace, where all groups in groupList is organized in a dictionary.
        The dictionary has outRing ele as key, Its value is the remaining 2 values (in a list sorted descendingly) of the group where the key resides.
        Each outRing key can be associated with multiple 2-number lists.
        In order to find max solutionSpace, assume the the outRing members start with n - m + 1 all the way to n
    '''
    outRingStart = n - m + 1
    outRings = list(range(outRingStart, n + 1))
    tempGL = groupList[:]
    for group in groupList:
        if len(set(outRings).intersection(set(group))) != 1: # a valid group has only ONE outRing ele
            tempGL.remove(group) # failed group gets removed
    groupList = tempGL
    
    maxSolutionSpace = {}
    if len(groupList) >= m: # valid groupList must contain more than m groups, otherwise no solutionSpace can be generated
        for outRingEle in outRings:
            for group in groupList:
                if outRingEle in group:
                    tempG = group[:] # make a copy of group since it is going to be modified
                    tempG.remove(outRingEle) # get the remaining elements
                    tempG.sort(reverse = True) # sort in descending order
                    if outRingEle in maxSolutionSpace:
                        maxSolutionSpace[outRingEle].append(tempG)
                    else:
                        maxSolutionSpace[outRingEle] = [tempG]
            if outRingEle not in maxSolutionSpace: # outRing element not found among the groups, unable to generate solutionSpace
                maxSolutionSpace = {}
                break
    return outRingStart, maxSolutionSpace


def findsolutionDict(solutionSpace, solutionDictList, solutionDict, outRing, n, eleFrequency):
    ''' find solutionDict recursively from solutionSpace. A valid solutionDict has outRing members
        as key and only one pair of members associated with it. All outRing members are unique, while
        their members appear exactly twice among themselve.
        If multiple solutionDict can be found, append them in the solutionDictList
    '''
    if outRing > n:
        solutionDictList.append(copy.deepcopy(solutionDict)) # successfully find a solutionDict
        return True

    outRingGood = False # flag, whether any of the current outRing group can be added to solutionDict
    for group in solutionSpace[outRing]:
        matchGroup = True # flag, whetehr the current group can be added to solutionDict
        for ele in group:
            if eleFrequency[ele] >= 2: # non-outRing ele already appears twice, failed attempt
                matchGroup = False
                break
            else:
                eleFrequency[ele] += 1
        if matchGroup: # the current group can be added to solutionDict
            solutionDict[outRing] = group
            if not findsolutionDict(maxSolutionSpace, solutionDictList, solutionDict, outRing + 1, n, eleFrequency):
                del solutionDict[outRing] # if further finding fails, remove the current addition
            else:
                outRingGood = True
    return outRingGood


def constructSol(outRingStart, solutionDict, m):
    ''' using solutionDict to construct the current solution '''
    sol = []
    side = [outRingStart] + solutionDict[outRingStart] # first polygon side done
    sol += side
    for i in range(m - 1): # construct the remaining sides
        target = side[-1] # each side's last element is the middle element of the next side
        for k, v in solutionDict.items():
            if target in v and k != side[0]: # find the next side (overlap in the target but different outRing element)
                temp = v[:]
                temp.remove(target) # get the last element in the next side
                side = [k, target, temp[0]]
                sol += side
                break
    return sol        



# DRIVER
n = 22
m = 11 # number of sides of the polygon
numList = list(range(1, n + 1))

rawSpace = {} # list all sums possible for 3-number groups, group the 3-number groups of the same sum together
# construct raw space
for group in combinations(numList, 3):
    sumGroup = sum(group)
    if sumGroup in rawSpace:
        rawSpace[sumGroup].append(list(group))
    else:
        rawSpace[sumGroup] = [list(group)]

ans = ""
for k, v in rawSpace.items():
    if len(v) >= m and checkValid(v, numList): # for each sum, it can be used as a possible solution iff there are more than m different groups within
                                               # And a possible solution must contain all element in numList
        outRingStart, maxSolutionSpace = findMaxSolutionSpace(v, n, m) # get maxSolutionSpace
        if maxSolutionSpace: # some maxSolutionSpace is empty, ignore them
            solutionDictList = [] # store a list of solutionDict, if any
            solutionDict = {} 
            eleFrequency = [0] * (n + 1) # record the frequency of non-outRing ele. The frequency of valid non-outRing ele should be 2.
            if findsolutionDict(maxSolutionSpace, solutionDictList, solutionDict, outRingStart, n, eleFrequency):
                # solutionDict found
                for sd in solutionDictList:
                    sol = constructSol(outRingStart, sd, m)
                    print(sol)
                    print('')
                    solStr = "".join([str(x) for x in sol])
                    ans = solStr if solStr > ans else ans

print(ans)

# runtime = 0.001 s


print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

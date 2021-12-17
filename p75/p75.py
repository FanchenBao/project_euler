#! /usr/bin/env python3
import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Author: Fanchen Bao
Date: 01/07/2019

Project Euler: Problem 75

Solution: 
    Basic idea is to produce all primitive Pythagorean triples with perimeter smaller than the given limit. 
Then from each primitive Pythagorean triples, produce new triples that are multiples of the primitive until 
the new triples' perimeter reaches the limit. Each time a perimeter is calculated, use the bucket method to 
record how many times such perimeter has occurred. At the end, count the number of perimeters that have value 
1 in its corresponding bucket.

    There are two ways to generate primitive Pythagorean triples. 
    Method one: (2uv, u^2 - v^2, u^2 + v^2), in which u and v are co-prime and different in parity (u and v 
cannot be both even or odd) (see http://mathworld.wolfram.com/PythagoreanTriple.html). 
    Method two: (uv, (u^2 - v^2)/2, (u^2 + v^2)/2), in which u and v are co-prime and both are odd (see 
http://www.friesian.com/pythag.htm).

    The two methods are basically the same, but the number of (u, v) pairs to be checked are slightly 
different. For method one, boundary for u is sqrt(limit / 2), but u has to go from 2 to the boundary without 
skipping any in between. Thus the total number of u to be checked is ~sqrt(limit / 2).
    For method two, boundary for u is sqrt(limit), but u can only be odd, so when it goes from 3 to the boundary,
the total number of u to be checked is ~sqrt(limit) / 2.
    Apparently, method two checks fewer u than method one (both check the same amount of v's). This slight 
advantage seems to pay off when limit gets high. In my machine, with limit = 1,500,000, method two is 0.5s 
faster; with limit = 15,000,000, method two is 5s faster. That said, when limit is smaller, method one seems 
to be a bit faster.
'''
from math import sqrt
from fractions import gcd

limit = 1500000
allLs = [0] * (limit + 1)
for u in range(2, int(sqrt(limit / 2))):
    uParity = u % 2
    for v in range(1, u):
        # only way to produce primititve Pythagorean triples is to have u and v coprime and with opposite parity
        if gcd(u, v) == 1 and uParity != v % 2:
            multL = L = 2*u*v + 2*u*u
            i = 1
            while multL <= limit:
                allLs[multL] += 1
                i += 1
                multL = L * i

count = 0
for c in allLs:
    if c == 1:
        count += 1
print('method one: ' + str(count))

print("\nTime: {}".format(time() - s))



s = time()

limit = 1500000
allLs = [0] * (limit + 1)

for u in range(3, int(sqrt(limit)), 2):
    for v in range(1, u, 2):
        # to generate primitive Pythagorean triples, u and v must be co-prime and both odd number
        if gcd(u, v) == 1:
            i = 1
            multL = L = u*v + u*u
            while multL <= limit:
                allLs[multL] += 1
                i += 1
                multL = L * i
count = 0
for c in allLs:
    if c == 1:
        count += 1
print('method two: ' + str(count))

# runtime = 1.2 s


print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

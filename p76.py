#! /usr/bin/env python3
import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Author: Fanchen Bao
Date: 01/23/2018

Project Euler: Problem 76

Solution: 
    NOTE this is NOT my solution. It is solution by Chaozy_Z on the forum, published on 01/21/2019. This is a
very succint solution, same time complexity as mine (see my solution in Java) but much cheaper and clearner
space wise. Chaozy_Z didn't give any comment, so it took me a while to comprehend what this algorithm is doing.
Here is my explanation for this method.
    At each iteration of i, elements in lis records the number of sum expressions that involve numbers smaller
or equal to i. In this sense, at certain iteration of i, lis[j] means the total number of sum expressions that
involve numbers smaller or equal to i. To compute lis[j], we can write j = i + (j - i). So we only need to know
tht total number of sum expressions that involve number smaller or equal to i for j - i (which is essentially 
lis[j - i] of the current iteration i, and it has been computed already ahead of lis[j]), and add that to what
is already in lis[j] (what is already in lis[j] is the total number of sum expressions that involve numbers
strictly smaller than i, which have been computed from previous iterations of i). Therefore, at each iteration
of i, lis[j] = lis[j] + lis[j - i].
    In other words, for any number j, the iterations give all possible sum expressions from 1 + (j - 1), 2 + (j - 2),
3 + (j - 3), ..., and each iteration, the total number of sum expressions that can be expressed in the form of
i + (j - i) (with numbers <= i) is added to the total numbers of previous expressions. 
    Note that lis[0] is set to 1. The importance of this setting can be illustrated with an example. Say we want
to compute lis[4] when i = 2. According to the formula, lis[4] += lis[4-2], i.e. lis[4] += lis[2]. In other words,
the values of total number of sum expressions for 2 when the number involved <= 2 need to be added to the value
already in lis[4]. So what is all the expressions for 4 when i = 2? 4 = 2+2 and 4 = 2+1+1. This implies that
lis[2] = 2 when i = 2. This means 2 can be expressed as 2 = 1+1 and 2 = 2. Wait a minute, isn't 2 = 2 not allowed
in the question? No it is not. But here in the process of computation, we must consider the situation of 2 = 2,
because for any other number larger than 2 that uses 2 itself to construct an expression (e.g. 4 = 2 + 2, 5 = 3 + 2,
etc. note that the first number is the i value, while the second is one of the expressions that has to make up 2),
we must make sure 2 = 2 is allowed. Otherwise, we would be losing expressions in the exact form of (j - 2) + 2.
    In conclusion, the algorithm is very neat. It takes advantage of dp perfectly and condenses all computation
in only one array. 
'''

def summation(n):
    lis = [0 for i in range(n + 1)]
    lis[0] = 1

    for i in range(1, n):
        for j in range(i, n + 1):
            lis[j] += lis[j - i]
        print(lis)

    # print(lis[n])


summation(10)

print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')

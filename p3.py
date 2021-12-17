#! /usr/bin/env python3



import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')


''' the key is that no matter what, the first factor found searching from 2 onwards MUST be a prime number.
Thus, no need to test whether a number is prime. Then use the same method for the remaininng bigger factor, until eventually the bigger factor itself is prime
'''


'''general idea: factor out all the small prime numbers, then the last prime facotr must be the biggest.'''
# NUM = 600851475143
NUM = 2739
flag = 0

while (1):
    i = 2
    while(i < int(NUM ** (1/2))): # first prime factor of a composite NUM is smaller than sqrt(NUM)     
        if not (NUM % i):
            flag = 1 # NUM is not prime
            NUM = int(NUM / i) # factor out the prime factor and check for the remaining NUM
            break
        i += 1
    if flag:
        flag = 0 # reset flag
    else: # NUM is prime, then it is the biggest prime factor
        print(NUM)
        break

logging.debug('End of program.\n\n\n')

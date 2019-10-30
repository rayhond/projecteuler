#!/usr/bin/env python2.7

from itertools import permutations
import numpy as np

def GeneratePrimes(top_number, list_of_primes=[2]):
    for i in xrange(list_of_primes[-1], top_number+1, 2):
        prime = True
        max_prime = int(np.sqrt(i))+1
        for k in list_of_primes:
            if k > max_prime:
                break
            if (i%k==0):
                prime = False
                break
        if prime:
            list_of_primes.append(i)
    return list_of_primes

n = 11

digits = []
list_of_primes = [2,3]

#for i in xrange(100):
#    print i, i*(i+1)/2, i*(i+1)/2%3
max_number = 0

for i in xrange(1,n):
    digits.append(str(i))
    all_divisible = 1
    perm_list = permutations(digits)
    number = int(''.join(digits))
    if sum([int(d) for d in str(number)])%3==0:
        all_divisible=0
    
    if all_divisible:
        for j in perm_list:
            number = int(''.join(j))
            list_of_primes = GeneratePrimes(number, list_of_primes=list_of_primes)
            if number in list_of_primes:
                if number > max_number:
                    max_number = number
                    print max_number
    

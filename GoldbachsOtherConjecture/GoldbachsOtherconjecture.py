#!/usr/bin/env python2.7

import numpy as np

def GeneratePrimes(top_number, list_of_primes=[2,3]):
    for i in xrange(list_of_primes[-1]+2, top_number+1, 2):
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

max_number = 10000

list_of_primes = GeneratePrimes(max_number)

for i in xrange(3,max_number,2):
    if i in list_of_primes:
        continue
    no_exist = 1
    for j in list_of_primes:
        k = 1
        while k:
            test_number = j + 2*k**2
            if test_number > i:
                break
            elif test_number == i:
                no_exist=0
                break

            k = k+1
        if j > i:
            break
    if no_exist:
        print i

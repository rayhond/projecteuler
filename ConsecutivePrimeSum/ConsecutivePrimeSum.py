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

list_of_primes = GeneratePrimes(1000000)

for i in xrange(2,len(list_of_primes)):
    for start in xrange(len(list_of_primes)-i):
        test_number = sum(list_of_primes[start:start+i])
        if i%2==0:
            if list_of_primes[start] != 2:
                break
        if test_number in list_of_primes:
            print i, list_of_primes[start:start+i], test_number
            break

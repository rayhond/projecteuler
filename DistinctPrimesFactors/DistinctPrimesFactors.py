#!/usr/bin/env python2
import numpy as np
import time

def GeneratePrimes(top_number):
    list_of_primes = [2]
    for i in xrange(3, top_number+1, 2):
        prime = True
        max_prime = int(np.sqrt(i))+1
        for k in list_of_primes:
            if k > max_prime:
                break
            if (i%k==0):
                prime = False
        if prime:
            list_of_primes.append(i)
    return list_of_primes

def primeFactors(number, list_of_primes):
    prime_factors = []
    while number>1:
        for i in list_of_primes:
            if number % i ==0:
                prime_factors.append(i)
                number=number/i
                break

    return prime_factors

start = time.time()
max_N = 200000
list_of_primes = GeneratePrimes(max_N)
target_distinct = 4

distinct_count = 0
for i in xrange(2,max_N):
    if len(np.unique(primeFactors(i, list_of_primes)))==target_distinct:
        distinct_count = distinct_count + 1
    else:
        distinct_count = 0

    if target_distinct == distinct_count:
        print i
        break
end = time.time()
print end-start

#!/usr/bin/env python2
import decimal
import numpy as np

i = 3
list_of_primes = [2]

for i in xrange(3,1000000,2):
    prime = True
    for k in list_of_primes:
        if k**2>i:
            break
        if (i%k==0):
            prime=False
            break
    if prime:
        list_of_primes.append(i)

primes_to_remove = []
for i in list_of_primes:
    str_rep = str(i)
    if set(['4','6','8','0']).intersection(set(str_rep)):
        primes_to_remove.append(i)
    elif len(str_rep) > 2:
        if set(['2','5']).intersection(set(str_rep[1:-1])):
            primes_to_remove.append(i)

for i in primes_to_remove:
    list_of_primes.remove(i)

truncatable_primes = []
for prime in list_of_primes:
    str_rep = str(prime)
    correct = 0
    for j in xrange(1,len(str_rep)):
        if int(str_rep[:j]) in list_of_primes and int(str_rep[-j:]) in list_of_primes:
            correct = correct+1
        if correct == len(str_rep)-1:
            truncatable_primes.append(prime)
            print prime
print list_of_primes
print truncatable_primes, sum(truncatable_primes)

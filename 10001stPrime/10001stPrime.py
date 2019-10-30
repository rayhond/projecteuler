#!/usr/bin/env python2

i = 3
list_of_primes = [2]

while i:
    prime = True
    for k in list_of_primes:
        if (i%k==0):
            prime=False
    if prime:
        list_of_primes.append(i)
        print i, len(list_of_primes)
    if len(list_of_primes)==10001:
        print i
        break
    i = i +1

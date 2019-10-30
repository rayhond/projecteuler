#!/usr/bin/env python2

i = 3
list_of_primes = [2]

while i<2000000:
    prime = True
    for k in list_of_primes:
        if k**2>i:
            break
        if (i%k==0):
            prime=False
            break
    if prime:
        list_of_primes.append(i)
    i = i +1
print sum(list_of_primes)

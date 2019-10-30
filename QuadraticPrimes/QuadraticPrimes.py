#!/usr/bin/env python2

import math

def PrimeCheck(number):
    if number > 2:
        if number%2==0:
            return False
        else:
            for i in xrange(3,int(math.sqrt(number))+1, 2):
                if number%i==0:
                    return False
            return True
    elif number < 1:
        return False
    else:
        return True

max_number_of_primes = 0
max_a = None
max_b = None

for a in xrange(2001):
    for b in xrange(2001):
        n = 0
        while True:
            if not PrimeCheck(n**2+(a-1000)*n+(b-1000)):
                break
            else:
                n = n+1
        if n > max_number_of_primes:
            max_number_of_primes = n
            max_a = a-1000
            max_b = b-1000
print max_a, max_b, max_a*max_b

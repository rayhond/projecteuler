#!/usr/bin/env python2.7

import math

def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

counter = 0

for n in xrange(101):
    for r in xrange(n+1):
        if factorial(n)/(factorial(r)*factorial(n-r)) > 1000000:
            counter = counter + 1

print counter

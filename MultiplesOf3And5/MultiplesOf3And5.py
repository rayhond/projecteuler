#!/usr/bin/env python2

#Find the sum of all the multiples of 3 or 5 below 1000
# - Find multiples of 3 or 5 below 1000

sum = 0

for i in xrange(1000):
    if ((i % 3)==0) or ((i % 5)==0):
        print i
        sum = sum + i

print sum

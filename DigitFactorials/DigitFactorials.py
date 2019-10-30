#!/usr/bin/env python2

import math

total_sum = 0

for i in xrange(10, 1000000):
    total = 0
    for j in list(str(i)):
        total = total + math.factorial(int(j))

    if i == total:
        total_sum = total_sum + i
        print i

print total_sum

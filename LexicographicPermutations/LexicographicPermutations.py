#!/usr/bin/env python2

import math

number = 999999

sequence = [0,1,2,3,4,5,6,7,8,9]

for i in xrange(9, 0, -1):
    leftover = number/math.factorial(i)
    number = number%math.factorial(i)
    print number, leftover, math.factorial(i), leftover*math.factorial(i), sequence.pop(leftover)


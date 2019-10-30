#!/usr/bin/env python2
import numpy as np

triangular_number = 1
j = 2
divisor_number = 0
while divisor_number<500:
    divisor_number = 0
    for i in xrange(1,int(np.sqrt(triangular_number))):
        if triangular_number%i==0:
            divisor_number = divisor_number + 1
    divisor_number = divisor_number*2
    triangular_number = triangular_number+j
    j = j+1
print triangular_number-j+1

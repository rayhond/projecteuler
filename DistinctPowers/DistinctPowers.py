#!/usr/bin/env python2

import numpy as np

powers_list = np.zeros([99,99])

for i in xrange(2,101):
    for j in xrange(2,101):
        powers_list[i-2,j-2] = i**j

print np.unique(powers_list).shape

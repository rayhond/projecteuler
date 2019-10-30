#!/usr/bin/env python2

import math

x = math.factorial(100)
x = list(str(x))

total = sum([int(i) for i in x])

print total

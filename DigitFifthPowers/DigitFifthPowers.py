#!/usr/bin/env python 2

total2 = 0

for i in xrange(10,1000000):
    total = 0
    for j in list(str(i)):
        total = total + int(j)**5
    if i == total:
        total2 = total2+ total
        print i
print total2

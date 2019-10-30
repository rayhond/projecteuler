#!/usr/bin/env python2

j = 20
while j:
    divisible = True
    for i in xrange(2,21):
        if (j%i):
            divisible = False
            break
    if divisible:
        print j
        break
    j = j + 20

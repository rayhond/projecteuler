#!/usr/bin/env python2

for a in xrange(1000):
    for b in xrange(a,1000-a):
        c = 1000-a-b
        if a**2+b**2==c**2:
            print a,b,c,a*b*c

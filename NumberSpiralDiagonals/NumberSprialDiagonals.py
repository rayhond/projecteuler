#!/usr/bin/env python2

diagonal = 1

total = 1

for i in xrange(500):
    for j in xrange(4):
        diagonal = diagonal + (i+1)*2
        total = total+diagonal

print total

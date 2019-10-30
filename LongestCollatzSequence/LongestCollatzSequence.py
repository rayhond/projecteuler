#!/usr/bin/env python2

maxLength = 0
for i in xrange(1000000):
    startingNumber = i
    length = 1
    while i:
        if i==1:
            break
        if i%2==0:
            i = i/2
        else:
            i = 3*i + 1
        length = length+1
    if length>maxLength:
        maxLength = length
        maxNumber = startingNumber
print maxLength, maxNumber

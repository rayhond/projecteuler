#!/usr/bin/env python2.7
import math


max_counter = 0

for p in xrange(3,1001):
    list_of_triples= []
    counter = 0
    for a in xrange(1,int(math.ceil((p+1)/3.))):
        for b in xrange(a,int(math.ceil((p-a)/2.))+1):
            c = p - a - b
            triple = (a,b,c)
            list_of_triples.append(triple)
    for a,b,c in list_of_triples:
        if a**2 + b**2 == c**2:
            counter = counter + 1
    if counter > max_counter:
        max_perimeter = p
        max_counter = counter
print max_perimeter

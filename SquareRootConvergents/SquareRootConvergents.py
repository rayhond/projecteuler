#!/usr/bin/env python2

numerator = 1
denominator = 1
counter = 0

for i in xrange(1000):
    new_denominator = numerator+denominator
    new_numerator = new_denominator+denominator

    denominator=new_denominator
    numerator=new_numerator
#    print denominator, numerator
    if len(str(numerator))>len(str(denominator)):
        counter = counter + 1
print counter

#!/usr/bin/env python2

counter = 0
integer_list = []
for power in xrange(100):
    number=0
    base = 1
    while len(str(number)) < power+1:
        number = base**power
        if len(str(number))==power:
            counter=counter+1
            integer_list.append((base, power, number))
        base=base+1

print counter, integer_list

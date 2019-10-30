#!/usr/bin/env python2.7


maximum_sum = 0
max_a = 0
max_b = 0

for a in xrange(100):
    for b in xrange(100):
        number = a**b
        number_sum = sum([int(i) for i in str(number)])

        if number_sum > maximum_sum:
            maximum_sum=number_sum
            max_a = a
            max_b = b

print max_a, max_b, maximum_sum

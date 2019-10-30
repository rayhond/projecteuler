#!/usr/bin/env python2.7

max_number = 0
base_list = ['1', '2', '3', '4', '5', '6', '7', '8','9']
test_list = []

for i in xrange(1,int(1e5)):
    for j in xrange(2,10):
        multiples = [str(i*k) for k in xrange(1,j+1)]
        number = int(''.join(multiples))
        if number > 1e10:
            break
        test_list = sorted([k for k in str(number)])
        if test_list == base_list:
            if max_number < number:
                max_number = number
print max_number

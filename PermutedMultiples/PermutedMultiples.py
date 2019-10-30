#!/usr/bin/env python2.7

i = 1
no_match = 1

while no_match:
    base_list = sorted([j for j in str(i)])
    for j in xrange(1,7):
        test_list = sorted([k for k in str(i*j)])
        if base_list!=test_list:
            break
        if j==6:
            print i
            no_match=0
    i = i + 1


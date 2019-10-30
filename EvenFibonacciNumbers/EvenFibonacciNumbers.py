#!/usr/bin/env python2

term1 = 1
term2 = 2

sum = 0

while term1<4000000 or term2 < 4000000:
    if term2%2==0:
        sum = sum + term2
    term3 = term1 + term2
    term1 = term2
    term2 = term3

print sum

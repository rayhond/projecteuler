#!/usr/bin/env python2

term1 = 1
term2 = 2

index = 2

while len(str(term2))<3:
    term3 = term1 + term2
    term1 = term2
    term2 = term3
    index = index+1

print index

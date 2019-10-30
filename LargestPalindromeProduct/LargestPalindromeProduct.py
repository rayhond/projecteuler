#!/usr/bin/env python2

max_number = 0
for i in xrange(100,1000):
    for j in xrange(100,1000):
        number = i*j
        str_rep = str(number)
        palindrome = True
        for k in xrange(len(str_rep)/2):
            if str_rep[k]==str_rep[(-1-k)]:
                continue
            else:
                palindrome=False
                break
        if palindrome:
            max_number = max(max_number,number)

print max_number

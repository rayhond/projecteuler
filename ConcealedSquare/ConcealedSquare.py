#!/usr/bin/env python2
import numpy as np

#def incrementDigits(insert_digits):

insert_digits = ['0']*9
i = [str((i+1)%10) for i in xrange(10)]
test = int(''.join([val for pair in zip(i, insert_digits) for val in pair]+['0']))
#print insert_digits, i, test

print np.sqrt(test) % 1

while True:
    test = int(''.join([val for pair in zip(i, insert_digits) for val in pair]+['0']))
    if np.sqrt(test) % 1 ==0:
        print np.sqrt(test)
        break
    for j in xrange(8, -1, -1):
        digit = int(insert_digits[j])
        if digit==9:
            insert_digits[j-1]=str(int(insert_digits[j-1]))
            insert_digits[j]='0'
        else:
            insert_digits[j]=str(int(insert_digits[j])+1)
            break

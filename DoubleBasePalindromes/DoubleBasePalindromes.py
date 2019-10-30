#!/usr/bin/env python2

import numpy as np

def CheckPalindrome(number):
    digits = list(str(number))
    for i in xrange(len(digits)):
        if digits[i] == digits[-i-1]:
            continue
        else:
            return False
    return True

def BinaryConversion(number):
    i = 0
    largest_i = 0
    series = np.zeros(1, dtype = int)
    while number > 0:
        if number/2**i > 1:
            i = i+1
        else:
            if not largest_i:
                largest_i = i
                series = np.zeros(i+1, dtype=int)
            number = number - 2**i
            series[i] = 1
            i = 0
    
    rep = ''
    for i in series[::-1]:
        rep = rep + str(i)

    return int(rep)
number = 6

total = 0
for i in xrange(1000001):
    if CheckPalindrome(BinaryConversion(i)) and CheckPalindrome(i):
        total = total + i
        print i, BinaryConversion(i)

print total

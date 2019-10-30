#!/usr/bin/env python2

#A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

#A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import math
import numpy as np

def SumOfProperDivisors(number):
    total = 1
    for i in xrange(2, int(math.sqrt(number))+1):
        if number%i==0:
            if i == number/i:
                total = total + i
            else:
                total = total + i + number/i
    return total

list_of_abundant_numbers = []

for i in xrange(1,28124):
    if i < SumOfProperDivisors(i):
        list_of_abundant_numbers.append(i)

sorted_list = np.array(sorted(list_of_abundant_numbers))

sum_list = np.zeros([len(sorted_list), len(sorted_list)], dtype=int)

for i in xrange(len(sorted_list)):
    for j in xrange(i,len(sorted_list)):
        sum_list[i,j] = sorted_list[i] + sorted_list[j]

unique_list = np.unique(sum_list)[np.unique(sum_list)<28124][1:]

total = 0
counter = 0

for i in xrange(28124):
    if unique_list[counter]==i:
        counter = counter + 1
    else:
        total = total + i

print total

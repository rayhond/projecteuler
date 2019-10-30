#!/usr/bin/env python2
#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#Evaluate the sum of all the amicable numbers under 10000.

import math
def SumOfProperDivisors(number):
    total = 1
    for i in xrange(2, int(math.sqrt(number))+1):
        if number%i==0:
            if i == number/i:
                total = total + i
            else:
                total = total + i + number/i
    return total

limit = 10000
sum_list = [None]*limit
for i in xrange(limit):
    sum_list[i] = SumOfProperDivisors(i+1)

sum_total = 0
for j,i in enumerate(sum_list):
    try:
        x = sum_list[i-1]
        if j+1 == x and j+1 != i:
            sum_total = sum_total + j+1
            print j+1, x, i
    except:
        continue

print sum_total

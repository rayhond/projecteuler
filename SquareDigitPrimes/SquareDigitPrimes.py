#!/usr/bin/env python2
import numpy as np
import time


def SquareSum(n):
    k = 0
    while n:
        m = n %10
        n = n/10
        k = k + m*m
    return k

counter=0

running_1_list = []
running_89_list = []



for number in xrange(1,10000000):
    temp_number = number
    if number > 567:
        running_list=[]
    else:
        running_list = [temp_number]
    while True:
        temp_number = SquareSum(number)
        if temp_number in running_1_list:
            running_1_list = running_1_list + running_list
            break
        if temp_number in running_89_list:
            counter = counter+1
            running_89_list = running_89_list + running_list
            break
        running_list.append(temp_number)

#        print running_list
        if temp_number==1:
            running_1_list = running_1_list + running_list
            break
        if temp_number==89:
            counter = counter + 1
            running_89_list = running_89_list + running_list
            break
#        running_list.append(temp_number)
#        print number, temp_number

#    print number

#print running_89_list, running_1_list, sorted(running_89_list + running_1_list), len(sorted(np.unique(running_89_list+ running_1_list)))
print len(np.unique(running_89_list))
print counter

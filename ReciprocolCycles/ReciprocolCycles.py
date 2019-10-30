#!/usr/bin/env python2
import decimal
import numpy as np

i = 3
list_of_primes = [2]

while i<1000:
    prime = True
    for k in list_of_primes:
        if k**2>i:
            break
        if (i%k==0):
            prime=False
            break
    if prime:
        list_of_primes.append(i)
    i = i +1

max_length = 0
list_of_matches = []
decimal.getcontext().prec = 1000
#for j in xrange(20):

for i in xrange(1,1001):
#    before_decimal, after_decimal = '{:.9f}'.format(decimal.Decimal(1.*10**11)/decimal.Decimal(i)).split('.')
#    print i, '{:.9f}'.format(1.*10**11/i), before_decimal, after_decimal 
#    if before_decimal[0]==after_decimal[0]:
#        print i, before_decimal, after_decimal
    before_decimal, after_decimal = '{:.21f}'.format(decimal.Decimal(1.*10**23)/decimal.Decimal(i)).split('.')
#    print before_decimal, after_decimal
    for k in xrange(len(before_decimal)-1,-1,-1):
        test_string = before_decimal[k:]
#        print i,1./i, before_decimal, after_decimal #test_string, after_decimal[:len(test_string)]
        if test_string == after_decimal[:len(test_string)]:
            if len(test_string)>max_length:
                max_length=len(test_string)
#                list_of_matches.append((i,1./i, test_string, after_decimal[:len(test_string)], len(test_string)))
#                print i,1./i, before_decimal, test_string, after_decimal[:len(test_string)]
            list_of_matches.append((i,1./i, test_string, after_decimal[:len(test_string)], len(test_string)))
#            break

dtype= [('i',int),('divide',float),('test_string','S20'),('after_decimal','S20'),('length',int)]
#print np.sort(np.array(list_of_matches,dtype=dtype),order='length')[-100:]


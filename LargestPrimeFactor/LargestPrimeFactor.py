#!/usr/bin/env python2
#Find prime factors
#Find largest prime factors


def largestPrime(number):
    if number == 1:
        return number
    largePrime = 1
    for i in xrange(2,number+1):
        if number%i==0:
            largePrime = largestPrime(number/i)
            break

    return max(i, largePrime)

print largestPrime(600851475143)

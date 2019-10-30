#!/usr/bin/env python2
import numpy as np
from itertools import permutations

def PermuteDigits(number):
    list_of_rotated_numbers = [number]
    digit_list = set(permutations(list(str(number))))
    permuted_number_list = []
    for permuted_number in digit_list:
        temp_number = permuted_number[0]
        for digit in permuted_number[1:]:
            temp_number = temp_number + digit
        permuted_number_list.append(temp_number)

#    if len(rotated_number) == 1:
#        return number
#    for i in xrange(len(list(str(number)))-1):
#        temp = rotated_number[1:]
#        temp:q.append(rotated_number[0])
#        rotated_number = temp
#        if rotated_number[0] == '0':
#            continue
#
#        new_number = ''
#        for j in rotated_number:
#            new_number = new_number+j
#        new_number = int(new_number)
#        list_of_rotated_numbers.append(new_number)
    return permuted_number_list

def GeneratePrimes(top_number):
    list_of_primes = [2]
    for i in xrange(3, top_number+1, 2):
        prime = True
        max_prime = int(np.sqrt(i))+1
        for k in list_of_primes:
            if k > max_prime:
                break
            if (i%k==0):
                prime = False
        if prime:
            list_of_primes.append(i)
    return list_of_primes

prime_list = GeneratePrimes(10000)

for i in prime_list:
    counter = 0
    prime_permutation=[]
    for j in PermuteDigits(i):
        if j[0]=='0':
            continue
        if int(j) in prime_list:
            counter = counter + 1
            prime_permutation.append(int(j))
#            print int(j)
    prime_permutation = sorted(prime_permutation)
    for j in xrange(len(prime_permutation)):
        for k in xrange(j+1, len(prime_permutation)):
            if 2*prime_permutation[k]-prime_permutation[j] in prime_permutation:
                print prime_permutation, prime_permutation[j], prime_permutation[k],2*prime_permutation[k]-prime_permutation[j] 

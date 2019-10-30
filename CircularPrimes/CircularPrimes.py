#!/usr/bin/env python2
import numpy as np

def RotateDigits(number):
    list_of_rotated_numbers = [number]
    rotated_number = list(str(number))
    if len(rotated_number) == 1:
        return number
    for i in xrange(len(list(str(number)))-1):
        temp = rotated_number[1:]
        temp.append(rotated_number[0])
        rotated_number = temp
        if rotated_number[0] == '0':
            continue

        new_number = ''
        for j in rotated_number:
            new_number = new_number+j
        new_number = int(new_number)
        list_of_rotated_numbers.append(new_number)
    return list_of_rotated_numbers

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

list_of_primes = GeneratePrimes(1000000)
total=1
non_prime_digits = ['2','4', '6','8', '5','0']

for i in xrange(3,1000000, 2):
    all_prime = True
    digits = list(str(i))
    if len(list(str(i)))==1:
        if i not in list_of_primes:
            all_prime=False
        if all_prime:
            total = total+1
        continue
    for j in non_prime_digits:
        if j in digits:
            all_prime=False
            break
    if all_prime:
        for j in RotateDigits(i):
            if j not in list_of_primes:
                all_prime=False
                break
    if all_prime:
        total = total+1
#        print i
print total

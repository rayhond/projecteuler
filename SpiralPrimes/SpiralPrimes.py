#!/usr/bin/env python2
import numpy as np

def GeneratePrimes(top_number):
    list_of_primes = np.zeros(top_number, dtype=int)
    list_of_primes[0] = 2
    for i in xrange(3, top_number+1, 2):
        prime = True
        max_prime = int(np.sqrt(i))+1
        for j, k in enumerate(list_of_primes):
            if k > max_prime or j > i:
                break
            if k==0:
                continue
            if (i%k==0):
                prime = False
        if prime:
            list_of_primes[i]=i
    return list_of_primes[np.where(list_of_primes!=0)[0]]

def GeneratePrimes2(top_number):
    max_prime = (int(np.sqrt(top_number))+1)/2
    sieve = np.zeros((top_number-1)/2)
    
    for i in xrange(1, max_prime):
        if not sieve[i]:
            sieve[(2*i*(i+1))::(2*i+1)]=1
            sieve[i]=0
    return np.where(sieve==0)[0]

diagonal_list = [1]
prime_diagonal_list = []
prime_list = GeneratePrimes2(700000000)
prime_list = [2] + [2*i+1 for i in prime_list]
prime_list.pop(1)
prime_list = np.array(prime_list)
print prime_list

diagonal=1
i=2
prime_counter = 0
prime_diagonal_counter = 0

while True:
#    print len(prime_diagonal_list)/float(len(diagonal_list))
    if prime_diagonal_counter/float((2*(i-1)-1))<0.1:
        if prime_diagonal_counter !=0:
            break
    for j in xrange(4):
        diagonal = diagonal + i
#        print diagonal, i, i*2+1, prime_diagonal_counter,  prime_diagonal_counter/float(i*2+1)
#        diagonal_list.append(diagonal)
        try:
            while diagonal > prime_list[prime_counter]:
                prime_counter = prime_counter + 1
        except IndexError:
            continue
        if diagonal == prime_list[prime_counter]:
            prime_diagonal_counter = prime_diagonal_counter + 1
#            prime_diagonal_list.append(diagonal)
    i=i+2
#print prime_diagonal_list, diagonal_list, i, len(diagonal_list), len(prime_diagonal_list), diagonal_list[-1], prime_diagonal_list[-1], prime_list[-1]
print i-1, diagonal, 2*(i-1)-1

#!/usr/bin/env python2
import numpy as np
import time
from itertools import combinations

def GeneratePrimes2(top_number):
    max_prime = (int(np.sqrt(top_number))+1)/2
    sieve = np.zeros((top_number-1)/2)
    
    for i in xrange(1, max_prime):
        if not sieve[i]:
            sieve[(2*i*(i+1))::(2*i+1)]=1
            sieve[i]=0
    return np.where(sieve==0)[0]

def primeFactors(max_number, list_of_primes):
    prime_factors_list = [None]*max_number
    prime_counter = 0
    for number in xrange(2,max_number):
        if number in list_of_primes[prime_counter:prime_counter+2]:
            prime_counter = prime_counter+1
            prime_factors_list[number] = [number]
            continue
        for prime in list_of_primes:
            if number%prime==0:
                if prime in prime_factors_list[number/prime]:
                    prime_factors_list[number] = prime_factors_list[number/prime]
                else:
                    prime_factors_list[number] = prime_factors_list[number/prime] + [prime]

                break

    return prime_factors_list

def findRelativePrimes(number, factors, number_of_factors):
    relative_primes=number+2
    for i in xrange(1,number_of_factors):
        comb = combinations(factors, i)
        for j in list(comb):
            divisor = 1
            for k in j:
                divisor = divisor*k
            relative_primes = relative_primes + ((number+2)/divisor)*(-1)**(i)
#            print number, divisor, (number+2)/divisor, (-1)**(i)
    if number_of_factors%2==0:
        relative_primes=relative_primes+1
    else:
        relative_primes=relative_primes-1
#    print relative_primes
    return relative_primes



max_number = 1000000
prime_list = GeneratePrimes2(max_number)
prime_list = [2] + [2*i+1 for i in prime_list]
prime_list.pop(1)
prime_list = np.array(prime_list)

max_ratio = -np.inf

start = time.time()
prime_factors = primeFactors(max_number, prime_list)[2:]
#print prime_factors
end = time.time()
factor_time = end-start

totient_function = np.zeros(max_number-2)
max_factors = 0


start = time.time()
for number, factors in enumerate(prime_factors):
    number_of_factors = len(factors)
    print number+2, factors
    if number_of_factors < max_factors:
        continue
    if number_of_factors==1:
        totient_function[number] = number-(number+2)/factors[0]+2
    else:
        gcf = 1
        for i in factors:
            gcf = gcf * i
        if gcf == number+2:
            totient_function[number] = findRelativePrimes(number, factors, number_of_factors)
#            overlap=0
#            for i in xrange(number_of_factors):
##                print number+2, i, factors, factors[:i]+factors[i+1:]
#                overlap_multiple = 1
#                for j in factors[:i]+factors[i+1:]:
#                    overlap_multiple = overlap_multiple*j
#                overlap = overlap + (number+2)/(overlap_multiple)-1
#            if number_of_factors==2:
#                totient_function[number]=number-overlap+1
#            else:
#                totient_function[number]=number+overlap+1-sum([(number+2)/i-1 for i in factors])
#                print overlap, sum([(number+2)/i-1 for i in factors ] )
#            print number+2, factors
#            overlap = 0
#            for i in xrange(number_of_factors):
#                for j in xrange(i+1, number_of_factors):
#                    overlap = overlap + (number+2)/(factors[i]*factors[j])-1
        else:
            gcf_inc = gcf
            while factors!=prime_factors[number-gcf]:
#                print number+2, factors, gcf
                gcf = gcf+gcf_inc
            relative_prime_list = np.ones(gcf)
            for i in factors:
                relative_prime_list[::i]=0
#            print number+2, gcf, np.where(relative_prime_list==0)[0]+number+2-gcf, relative_prime_list
            totient_function[number]=totient_function[number-gcf] +sum(relative_prime_list)
    if (number+2)/totient_function[number] > max_ratio:
        max_ratio = (number+2)/totient_function[number]
        max_number = number+2
        max_factors = number_of_factors
        print max_number, max_ratio, factors
#print totient_function

end = time.time()
print max_number, max_ratio
print factor_time, end-start
#start = time.time()

#max_ratio = -np.inf
#totient_function2 = np.zeros(max_number-2)
#for number, factors in enumerate(prime_factors):
#    relative_prime_list = np.ones(number+2-1)
#    for i in factors:
#        relative_prime_list[i-1::i]=0
#    totient_function2[number]=sum(relative_prime_list)
#    max_ratio = max((number+2)/sum(relative_prime_list), max_ratio)
#end = time.time()
#for i, j in enumerate(totient_function):
#    if j!=totient_function2[i]:
#        print i+2, j, totient_function2[i]
#print max_ratio
#print end-start

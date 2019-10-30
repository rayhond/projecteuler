#!/usr/bin/env python2.7

from itertools import permutations

#permutation_list = list(permutations(str(range(1,10))))

digit_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
permutation_list = list(permutations(digit_list))
list_of_primes = [2,3,5,7,11,13,17]
list_of_correct = []

for combo in permutation_list[:]:
    if combo[0] == '0':
        break
    for i, prime in enumerate(list_of_primes):
        if int(''.join(combo[i+1:i+4]))%prime!=0:
            i=0
            break
    if i==6:
        print ''.join(combo)
        list_of_correct.append(int(''.join(combo)))
print sum(list_of_correct)

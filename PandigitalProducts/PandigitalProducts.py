#!/usr/bin/env python2.7

from itertools import permutations

#permutation_list = list(permutations(str(range(1,10))))

digit_list = ['1','2','3','4','5','6','7','8','9']
permutation_list = list(permutations(digit_list))

pandigital_number = []


for combo in permutation_list[:]:
    for i in xrange(1,9):
        for j in xrange(i+1,9):
            if int(''.join(combo[:i]))*int(''.join(combo[i:j])) ==int(''.join(combo[j:])):
#                print combo[j:]
                if int(''.join(combo[j:])) not in pandigital_number:
                    pandigital_number.append(int(''.join(combo[j:])))
print pandigital_number, sum(pandigital_number)

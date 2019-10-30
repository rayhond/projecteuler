#!/usr/bin/env python2.7
import numpy as np

def pentagon(n):
    return n*(3*n-1)/2

def triangle(n):
    return n*(n+1)/2

def check_pentagon(n):
    if (1 + np.sqrt(1+ 24*n)) % 6 ==0:
        return (1 + np.sqrt(1+ 24*n)) / 6
    return False
#
#list_of_numbers = [pentagon(n) for n in xrange(1,10000)]
#
#for i in xrange(len(list_of_numbers)):
#    for j in xrange(i,len(list_of_numbers)):
#        if list_of_numbers[i]+list_of_numbers[j] > list_of_numbers[-1]:
#            break
#        if list_of_numbers[i]+list_of_numbers[j] in list_of_numbers and (list_of_numbers[i]+2*list_of_numbers[j] in list_of_numbers or 2*list_of_numbers[i]+list_of_numbers[j] in list_of_numbers ):
#            print i+1, j+1

#print int(pentagon(35333)), int(pentagon(312102277)), int(pentagon(312102279)), int(pentagon(312102277)) - int(pentagon(35333))
#
#for i in xrange(312102270, 312102278):
#    print int(pentagon(i))

j = 2
found=False
smallest_diff = np.inf


#for i in xrange(1,5000):
#    for j in xrange(i,5000):
#        Pi = pentagon(i)
#        Pj = pentagon(j)
#
#        if check_pentagon(Pi+Pj) and check_pentagon(Pj-Pi):
#            print Pi, Pj, Pj-Pi


while not found:
    for i in xrange(1,j):
#        print i, j, -((-j*(3*j+1)/2)-(i*(3*i-1)/2)),-(3*i-3*j)
        if -((-j*(3*j+1)/2)-(i*(3*i-1)/2)) % -(3*i-3*j) == 0:
#            print 'inside', i, j, -((-j*(3*j+1)/2)-(i*(3*i-1)/2)),-(3*i-3*j)
            good_index =((-j*(3*j+1)/2)-(i*(3*i-1)/2)) / (3*i-3*j)
            if good_index > j:
                pentagonal_check = check_pentagon(pentagon(good_index) - pentagon(good_index-j))
                if pentagonal_check:
#                    if smallest_diff > pentagonal_check:
                    print i, j,good_index , pentagon(good_index), pentagon(good_index + i), pentagon(good_index -j), pentagon(good_index+i)-pentagon(good_index), pentagon(good_index) - pentagon(good_index - j), pentagonal_check, pentagon(pentagonal_check)
#                        smallest_diff = min(smallest_diff, pentagonal_check)

    j = j+1


#for i in xrange(2,10):
#    n = 35000
#    diff_index = 312102000
#    second_number = -1
#    print 'i = ', i
#
#    while n<100000:
#        if (pentagon(n)-pentagon(i))/(3.*i) % 1 ==0:
#            first_pentagonal = pentagon(n)
#            second_pentagonal_index =(pentagon(n)-pentagon(i))/(3*i)
#            second_pentagonal = int(pentagon(second_pentagonal_index))
#            pentagonal_sum = first_pentagonal + second_pentagonal
#            pentagonal_diff = second_pentagonal - first_pentagonal
#    #        print n, second_pentagonal_index, second_pentagonal_index+i, first_pentagonal, second_pentagonal, pentagon(second_pentagonal_index+i), pentagonal_sum, pentagonal_diff, 7*(second_number+1)+18*triangle(second_number)
#            second_number = second_number + 1
#            
#            while diff_index*(3*diff_index-1)/2. < pentagonal_diff:
#                diff_index = diff_index + 1
#    #            print diff_index*(3*diff_index-1)/2., pentagonal_diff 
#
#            if pentagon(diff_index) == pentagonal_diff:
#                print n, second_pentagonal_index, second_pentagonal_index+i, first_pentagonal, second_pentagonal, pentagonal_sum, int(pentagonal_diff), diff_index
#                break
#
#
#        n = n+1

#!/usr/bin/env python2.7

for i in xrange(10,100):
    str_rep_i = str(i)
    for j in xrange(i+1,100):
        str_rep_j = str(j)
        if str_rep_i[0]==str_rep_j[0]:
            if str_rep_j[1]=='0':
                continue
            if int(str_rep_i[1]) / float(str_rep_j[1]) == i/float(j):
                print i,j
        elif str_rep_i[0] == str_rep_j[1]:
            if str_rep_j[0]=='0':
                continue
            if int(str_rep_i[1]) / float(str_rep_j[0]) == i/float(j):
                print i,j
        elif str_rep_i[1] == str_rep_j[0]:
            if str_rep_j[1]=='0':
                continue
            if int(str_rep_i[0]) / float(str_rep_j[1]) == i/float(j):
                print i,j
        elif str_rep_i[1] == str_rep_j[1]:
            if str_rep_j[0]=='0':
                continue
            if int(str_rep_i[0]) / float(str_rep_j[0]) == i/float(j):
                print i,j
        else:
            continue

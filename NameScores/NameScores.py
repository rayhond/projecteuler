#!/usr/bin/env python2

letter_scores = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10,
        'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21,
        'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}

f = open('p022_names.txt', 'rb')
for line in f:
    name_list = line.strip('"').split(',')

for j,i in enumerate(name_list):
    name_list[j] = i.strip('"')
name_list = sorted(name_list)

name_score_array = [None]*len(name_list)

for j, i in enumerate(name_list):
    name_score = 0
    for k in list(i):
        name_score = name_score + letter_scores[k]
    name_score_array[j] = name_score

total_sum = 0

for j,i in enumerate(name_score_array):
    total_sum = total_sum + i*(j+1)

print total_sum

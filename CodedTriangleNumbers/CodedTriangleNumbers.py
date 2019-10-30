#!/usr/bin/env python2.7


def nth_triangle(n):
    return 1./2.*n*(n+1)

code = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

total_words = 0
n = 1
words = open('words.txt')
triangle_numbers = [nth_triangle(n)]

for line in words:
    for word in line.split(',')[:-1]:
        print word
        word_code = sum([code[i] for i in word.strip('"')])
        while triangle_numbers[-1]<word_code:
            n = n+1
            triangle_numbers.append(nth_triangle(n))
        if word_code in triangle_numbers:
            total_words = total_words+1

print total_words

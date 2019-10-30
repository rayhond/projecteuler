#!/usr/bin/env python2.7

def triangle(n):
    return n*(n+1)/2

def pentagon(n):
    return n*(3*n-1)/2

def hexagon(n):
    return n*(2*n-1)

i = 1
j = 0
k = 0

counter = 0

triangle_number = triangle(i)
pentagon_number = pentagon(j)
hexagon_number = hexagon(k)

while i:
    while triangle_number > pentagon_number:
        while pentagon_number > hexagon_number:
            hexagon_number = hexagon(k)
            k = k+1
        pentagon_number = pentagon(j)
        j = j+ 1
    if triangle_number == pentagon_number and triangle_number == hexagon_number:
        print triangle_number
        if counter:
            break
        counter = counter + 1
    triangle_number = triangle(i)
    i = i+1


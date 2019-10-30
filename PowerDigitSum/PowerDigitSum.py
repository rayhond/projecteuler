#!/usr/bin/env python2

number = 2**1000
number = list(str(number))
total = sum([int(x) for x in number])

print total

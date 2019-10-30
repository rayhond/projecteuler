#!/usr/bin/env python2.7

total = 0
i = 1
power=0
product = 1

while total < 1e6:
    total = total + len(str(i))
    if total >= 10**power:

        print total, i, total - 10**power
        if total-10**power !=0:
            product = product*int(str(i)[-(total-10**power+1)])
            print str(i)[-(total-10**power+1)]
        power = power + 1
    i = i+1

print product

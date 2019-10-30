#!/usr/bin/env python2

def one_or_89(n, cache={}):
    while (n != 89 and n != 1):
        n = sum(x*x for (x) in map(int, str(n)))
    return n

def main():
    last = {0:1}
    squares = [(x*x) for (x) in range(10)] # [0, 1, 4 .. 81]
    for (i) in range(7): # number of digits
        next = {}
        for (tot, cnt) in last.iteritems():
#            print last, tot, cnt
            for (v) in squares:
                ntot = tot + v
                try:
                    next[ntot] += cnt
                except KeyError:
                    next[ntot] = cnt
        last = next
    
#    print last
    fin = {1:0, 89:0}
    del last[0] # causes one_or_89 to infinite loop
    print last
    for (k, v) in last.iteritems():
        fin[one_or_89(k)] += v
    print fin

main()

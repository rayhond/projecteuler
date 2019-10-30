#!/usr/bin/env python2

#How many ways to make L2
#Using 1p, 2p, 5p, 10p, 20p, 50p, 100p, 200p

target = 200
running_sum = 0
total = 0

for i in xrange((target-running_sum)/200+1):
    running_sum = i*200
    for j in xrange((target-running_sum)/100+1):
        running_sum = i*200+ j*100
        for k in xrange((target-running_sum)/50+1):
            running_sum = i*200+ j*100 + 50*k
            for l in xrange((target-running_sum)/20+1):
                running_sum = i*200+ j*100 + 50*k + l*20
                for m in xrange((target-running_sum)/10+1):
                    running_sum = i*200+ j*100 + 50*k + l*20 + 10*m
                    for n in xrange((target-running_sum)/5+1):
                        running_sum = i*200+ j*100 + 50*k + l*20 + 10*m + 5*n
                        for o in xrange((target-running_sum)/2+1):
                            running_sum = i*200+ j*100 + 50*k + l*20 + 10*m + 5*n +2*o
                            for p in xrange((target-running_sum)/1+1):
                                running_sum = i*200+ j*100 + 50*k + l*20 + 10*m + 5*n +2*o + p
                                
                                if running_sum==target:
                                    total = total+1
                                    print i,j,k,l,m,n,o,p,"yes", total

#!/usr/bin/env python2

previous_num = 2
current_num = 3

counter = 3

while counter < 101:
    if counter%3==0:
        temp_num = previous_num
        previous_num = current_num
        current_num = current_num*counter/3*2+temp_num
#        continue
    else:
        temp_num = previous_num
        previous_num = current_num
        current_num = current_num+temp_num
#        continue
    counter = counter + 1
#    print current_num

print sum([int(i) for i in str(current_num)])


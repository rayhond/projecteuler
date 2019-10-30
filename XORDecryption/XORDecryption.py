#!/usr/bin/env python2
import numpy as np
import pandas as pd

def dec_to_bin(number):
    power = 0
    max_power = 0
    while True:
        if number<2**power:
            max_power = power-1
            break
        power=power+1
#    print max_power, 2**max_power
    bin_rep = np.zeros(max_power+1)
    for power in xrange(max_power,-1, -1):
        if number >= 2**power:
            bin_rep[power]=1
            number = number-2**power

    return bin_rep

def bin_to_dec(bin_number):
    output = 0
    for j, i in enumerate(bin_number):
        output = output + i*2**j

    return output


def xor(number_1, number_2):
    while len(number_1)!=len(number_2):
        if len(number_1)>len(number_2):
            number_2 = np.concatenate((number_2, [0]))
        else:
            number_1 = np.concatenate((number_1, [0]))
    
    output = np.zeros(len(number_1))
    for i in xrange(len(number_1)):
        if number_1[i]==number_2[i]:
            output[i]=0
        else:
            output[i]=1
    
    return output

ascii_table=pd.read_csv('ASCII_table_full.txt', delim_whitespace=True, header=None, engine='python')
dec_to_char = {}
char_to_dec = {}

for i in xrange(ascii_table.values.shape[0]):
    dec_to_char[ascii_table.values[i][2]]=ascii_table.values[i][4]
    char_to_dec[ascii_table.values[i][4]]=ascii_table.values[i][2]

encoded_text = pd.read_csv('p059_cipher.txt', header=None).values[0]
text_len = len(encoded_text)

print min(dec_to_char), max(dec_to_char)

a = 107
b = 42

print dec_to_bin(a), dec_to_bin(b), bin_to_dec(xor( dec_to_bin(b),dec_to_bin(a)))


#for i in xrange(97, 123):
#    for j in xrange(97, 123):
#        for k in xrange(97, 123):
#            encryption_key = [dec_to_bin(i), dec_to_bin(j), dec_to_bin(k)]
##            print encryption_key, dec_to_char[bin_to_dec(encryption_key[0])], dec_to_char[bin_to_dec(encryption_key[1])], dec_to_char[bin_to_dec(encryption_key[2])]
#            output = [None]*text_len
#            for index, char in enumerate(encoded_text):
#                try:
#                    output[index] = dec_to_char[bin_to_dec(xor(dec_to_bin(char), encryption_key[index%3]))]
#                except KeyError:
#                    break
#            if output[-1]!=None:
#                print str(output), i, j, k
#print "end"

i = 101 
j = 120 
k = 112

encryption_key = [dec_to_bin(i), dec_to_bin(j), dec_to_bin(k)]
total = 0
for index, char in enumerate(encoded_text):
    total = total + bin_to_dec(xor(dec_to_bin(char), encryption_key[index%3]))

print total

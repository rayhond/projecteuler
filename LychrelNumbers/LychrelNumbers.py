#!/usr/bin/env python2

def reverseNumber(number):
    return int(str(number)[::-1])

def checkPalindrome(number):
    palindrome=True
    str_rep = str(number)
    if len(str_rep)==1:
        palindrome=False
        return palindrome
    for i in xrange(len(str_rep)):
        if str_rep[i]!=str_rep[-i-1]:
            palindrome=False
            break
    return palindrome

def checkLychrel(number):
    lychrel=True
    for i in xrange(50):
        number = number + reverseNumber(number)
        if checkPalindrome(number):
            lychrel=False
            return lychrel
    return lychrel

counter = -1
for i in xrange(10000):
    if checkLychrel(i):
        counter = counter + 1

print counter

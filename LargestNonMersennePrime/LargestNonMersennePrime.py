def lastNDigits(number, n):
    return int(str(number)[-n:])

number=2
power=7830457

#power=10
for i in xrange(2,power+1):
    number = 2*lastNDigits(number, 10)
    if i > 7830437:
        print number
#    print i, number

print number
print 28433*number+1

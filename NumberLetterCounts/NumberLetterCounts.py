#!/usr/bin/env python2

#sum letters of numbers 1 - 1000

#one*9*10
#two*9*10
#three*9*10
#four
#five
#six
#seven
#eight
#nine
total = (3+3+5+4+4+3+5+5+4)*190

#
#ten
#eleven
#twelve
#thirteen
#fourteen
#fifteen
#sixteen
#seventeen
#eighteen
#nineteen
total = total + (3+6+6+8+8+7+7+9+8+8)*10

#twenty
#thirty
#forty
#fifty
#sixty
#seventy
#eighty
#ninety
total = total + (6+6+5+5+5+7+6+6)*10*10

#hundred*900
total = total + 7*900
#and*900-9
total = total + 3*(900-9)
#thousand*1
total = total + 8 + 3

print total

#!/usr/bin/env python2

weekday_of_first_day =3 
year = 1901 
Sunday_Count = 0

days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31, 13:29}

while year < 2001:
    for i in xrange(1,13):
        if weekday_of_first_day == 1:
            Sunday_Count = Sunday_Count + 1
        if i==2:
            if year % 4 == 0:
                if year % 100==0 and year % 400 != 0:
                    weekday_of_first_day = (weekday_of_first_day + days_in_month[i])%7
                else:
                    weekday_of_first_day = (weekday_of_first_day + days_in_month[13])%7
            else:
                weekday_of_first_day = (weekday_of_first_day + days_in_month[i])%7
        else:
             weekday_of_first_day = (weekday_of_first_day + days_in_month[i])%7

    year = year + 1

print Sunday_Count

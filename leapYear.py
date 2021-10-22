"""conditions for a leap year
The year is evenly divisible by 4;
If the year can be evenly divided by 100, it is NOT a leap year, unless;
The year is also evenly divisible by 400. Then it is a leap year.
"""
# we solve this by pyramid if-else
def is_leap(year):
    if year%4 == 0:
        leap = True
        if year%100 == 0:      
            if year%400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    return leap

year = int(input())
print (is_leap(year))
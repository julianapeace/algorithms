"""
The year can be evenly divided by 4, is a leap year, unless: #true
The year can be evenly divided by 100, it is NOT a leap year, unless: #false
The year is also evenly divisible by 400. Then it is a leap year. #true
#Hackerrank submitted 94,000 times
"""
def is_leap(year):
    leap = False

    # Write your logic here
    if year % 4 == 0 and year%100!=0:
        leap = True
    elif year % 400 == 0:
        leap = True

    return leap

year = 1992
print(is_leap(year))

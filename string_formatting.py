"""
https://www.hackerrank.com/challenges/python-string-formatting/problem
Submitted 17815 times
Print n lines where each line i (in the range 1<= i<=n) contains the respective decimal, octal, capitalized hexadecimal, and binary values of i. Each printed value must be formatted to the width of the binary value of n.
"""
n = 17
def print_formatted(number):
    width = len(bin(number)[2:])
    # your code goes here
    # r = "string".center(20, " ")
    for i in range(0,number+1):
        print(str(i).rjust(width,' '), (oct(i)[2:]).rjust(width, ' '), (hex(i).upper()[2:]).rjust(width,' '), (bin(i)[2:]).rjust(width, ' '))
print_formatted(n)

"""
    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001
"""

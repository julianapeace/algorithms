"""
https://www.hackerrank.com/challenges/designer-door-mat/problem
Submitted 18740 times
"""
N, M = map(int,input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
for i in range(1,N,2):
    print ((".|."*i).center(M,'-'))
print ("WELCOME".center(M,'-'))
for i in range(N-2,-1,-2):
    print ((".|."*i).center(M,'-'))

"""
9 27
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
"""

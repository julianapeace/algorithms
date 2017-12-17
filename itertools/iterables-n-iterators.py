"""
https://www.hackerrank.com/challenges/iterables-and-iterators/problem
Submitted 8244 times

input:
4
a a c d
2

output:
0.8333
"""
from itertools import combinations
N = int(input())
string = list(input().strip().split())
K = int(input())


pos = list(combinations(string[0:N], K))
num = len(['True' for i in pos if 'a' in i])
ans = num/len(pos)
print("%.4f" % ans)

"""
  >>> print("%.2f" % a)
  13.95
  >>> round(a,2)
  13.949999999999999
  >>> print("%.2f" % round(a,2))
  13.95
  >>> print("{0:.2f}".format(a))
  13.95
  >>> print("{0:.2f}".format(round(a,2)))
  13.95
  >>> print("{0:.15f}".format(round(a,2)))
  13.949999999999999
"""

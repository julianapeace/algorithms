"""
https://www.hackerrank.com/challenges/itertools-combinations/problem
Submitted 10693 times

input:
HACK 2
"""
from itertools import combinations

def make_combination(s,k):
    for i in range(1,k+1):
        print(list(combinations(s,i)))

if __name__ == "__main__":
    a = input().strip().split()
    s = sorted(list(a[0]))
    k = int(a[1])
    print(s,k)
    make_combination(s, k)

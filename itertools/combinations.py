"""
https://www.hackerrank.com/challenges/itertools-combinations/problem
Submitted 10693 times

input:
HACK 2
"""
from itertools import combinations

def make_combination(s,k):
    for i in range(1,k+1):
        ans = list(combinations(s,i))
        for i in range(0, len(ans)):
            print("".join(ans[i]))

def flat_combo(s,k):
    B = [list(combinations(s,i)) for i in range(1, k+1)]

if __name__ == "__main__":
    a = input().strip().split()
    s = sorted(list(a[0]))
    k = int(a[1])
    make_combination(s, k)
    flat_combo(s,k)

"""
https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
Submitted 9712 times
"""
import itertools
from itertools import combinations_with_replacement

def flat_ans(s,k):
    for c in combinations_with_replacement(sorted(s), int(k)):
        print("".join(c))

if __name__ == '__main__':
    s,k = input().strip().split()
    flat_ans(s,k)

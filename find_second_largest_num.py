"""
uRL:
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
Submitted 46006 times
"""


def solution():
    arr = list(arr_init)
    s_arr = sorted(arr)
    m = max(s_arr)
    p = 1
    while True:
        if m-p in s_arr:
            print (m-p)
            break
        else:
            p+=1


if __name__ == '__main__':
    n = int(input())
    arr_init = map(int, input().split())
    solution()

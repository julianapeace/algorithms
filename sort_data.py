"""
URL:https://www.hackerrank.com/challenges/python-sort-sort/problem
submiited:Submitted 6864 times

"""

# n = rows
# m = columns
# k = specific column

import sys

if __name__ == "__main__":
    n, m = input().strip().split(' ') #retrieving n and m
    n, m = [int(n), int(m)] #
    arr = []
    for arr_i in range(n):
       arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
       arr.append(arr_t)
    # print(arr)
    k = int(input().strip())
    # print("index: ", k)
    new_arr = []
    for i in range(0,len(arr)):
        new_arr.append([arr[i][k],i])
    s_arr = sorted(new_arr)
    # print("sorted list: ",s_arr)
    for i in range(n):
        arr_temp = arr[s_arr[i][1]]#[7, 1, 0]
        print (" ".join(map(lambda x: str(x),arr_temp)))

"""
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1
"""

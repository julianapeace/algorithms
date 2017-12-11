"""
https://www.hackerrank.com/challenges/swap-case/problem
Submitted 42497 times
"""

string = "hello"

def swap_case(s):
    old_arr = list(s)
    new_arr = []
    for i in range(0, len(old_arr)):
        if old_arr[i].isupper():
            new_arr += old_arr[i].lower()
        else:
            new_arr += old_arr[i].upper()
    return("".join(new_arr))


swap_case(string)

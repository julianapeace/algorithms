"""
https://www.hackerrank.com/challenges/text-wrap/problem
Submitted 26039 times
"""
import textwrap

def wrap(string, max_width):
    print (textwrap.fill(string,max_width))
    return textwrap.wrap(string, max_width)

if __name__ == '__main__':
    # string, max_width = input(), int(input())
    string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
    max_width = 4
    result = wrap(string, max_width)
    print(result)
"""
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
"""

"""
https://www.hackerrank.com/challenges/incorrect-regex/problem
"""
if __name__ == '__main__':
    t = int(input()) #num of test cases
    for _ in range(0, t):
        s = list(input())
        if s[0] == '.' and s[-1] == '+' and s[-2] != '\\':
            print("True")
        else:
            print("False")

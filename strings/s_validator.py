"""
https://www.hackerrank.com/challenges/string-validators/problem
Submitted 29456 times
"""
if __name__ == '__main__':
    s = input()
    # s = "aA2"
    function = ["isalnum()","isalpha()","isdigit()","islower()", "isupper()"]
    for i in function:
        cmd = s +'.'+i
        print(eval(cmd))

def solution():
    for test in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
        any(eval("c." + test + "()") for c in s)
# def solution():
#     s = "aA2"
#     print(s.isalnum())
#     print(s.isdigit())
# solution()

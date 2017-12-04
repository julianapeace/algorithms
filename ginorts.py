"""
url: https://www.hackerrank.com/challenges/ginorts/problem
Submitted 5328 times
"""
"""
# All sorted lowercase letters are ahead of uppercase  letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.

Pitfalls:
a) Using join, for or while anywhere in your code, even as substrings, will result in a score of 0.
b) You can only use  sorted function in your code. A 0 score will be awarded for using sorted more than once.

Hint: Success is not the key, but  is success.

Allowed only one sorted() function

hierarchy:
lowercase
uppercase
odd digits
even digits
"""
def sandbox():
    print("1: ",ord("1"))
    print("A: ",ord("A"))
    print("a: ",ord("a"))
sandbox()

def solution(x):
    num = ord(x)
    if num>100:
        print('over 100')

if __name__ == "__main__":
    arr = list(input())
    print(arr)
    s_arr = sorted(arr)
    print(s_arr)

    value = ""

    sol_arr = sorted((arr), key = solution)
    print(sol_arr)
    # print('value: ', value)
    print (list(map(lambda x: int(x),(s_arr))))

"""
Sorting1234
"""

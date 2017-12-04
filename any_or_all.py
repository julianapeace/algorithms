"""
URL:https://www.hackerrank.com/challenges/any-or-all/problem
Submitted 6366 times
"""
#use all()
#check if all int are positive
#use any()
#check if any are palindrome

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().strip().split()))
    # if (all([(lambda x: x > 0)(x) for x in arr])):
    #     print(any([(lambda x: str(x)[::-1] == str(x))(x) for x in arr]))
    # else:
    #     print("False")

    print("True" if all([(lambda x: x > 0)(x) for x in arr]) and any([(lambda x: str(x)[::-1] == str(x))(x) for x in arr]) else "False")
"""
5
12 9 61 5 14
"""
"""
6
1 2 3 4 5 -9
"""

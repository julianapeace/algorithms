"""
https://www.hackerrank.com/challenges/exceptions/problem
"""

if __name__ == '__main__':
    t = int(input()) #num of test cases
    for _ in range(0, t):
        this = input()
        a, b = this.split()
        try:
            print(int(a)/int(b))
        except ValueError as e:
            print("Error Code:", e)
        except ZeroDivisionError:
            print("Error Code: integer division or modulo by zero")



            """
            items = [1, 2, 3, 4, 5]
            squared = list(map(lambda x: x**2, items))
            """

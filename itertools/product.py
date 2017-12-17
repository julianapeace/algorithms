"""
https://www.hackerrank.com/challenges/itertools-product/problem
Submitted 13756 times

"""
from itertools import product

def make_product(a, b):
    ans = list(product(a,b))
    print(' '.join('({}, {})'.format(*el) for el in ans))


if __name__ == "__main__":
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    make_product(a,b)

"""
Sample Input

 1 2
 3 4

 OUTPUT:
 (1, 3) (1, 4) (2, 3) (2, 4) 
"""

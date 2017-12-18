"""
https://www.hackerrank.com/challenges/maximize-it/problem
Submitted 8290 times
INPUT:
3 1000
2 5 4
3 7 8 9
5 5 7 8 9 10
INPUT2:
7 588
7 3729019 6589533 9497010 1956867 4094190 1785314 9410145
7 6241592 9563118 4665482 3629252 418388 795859 816643
7 7924805 2362312 7324277 3672134 1005196 8234278 9131319
7 9978282 1999589 9658103 7451768 20958 1718778 3850870
7 4802255 5530524 3732809 8531273 2120056 3229818 488140
7 8730597 7531483 2414636 7488541 7094601 7080117 3634144
7 7512988 392327 4450786 7954145 2754638 4291414 1626278
OUTPUT:
206
OUTPUT2:
587

>>> a = [[1,2,3],[4,5,6],[7,8,9,10]]
>>> list(itertools.product(*a))
[(1, 4, 7), (1, 4, 8), (1, 4, 9), (1, 4, 10)
"""
from itertools import product
def make_modulo_max(items,m):
    pos = []
    combos = list(product(*items))
    #combos: [(5, 7, 5), (5, 7, 7), (5, 7, 8), (5, 7, 9), (5, 7, 10)]
    for combo in combos:
        total = 0
        for num in combo:
            total += num**2
        pos.append(total%m)
    print(max(pos))
    # print("True" if all([(lambda x: x > 0)(x) for x in arr]) and any([(lambda x: str(x)[::-1] == str(x))(x) for x in arr]) else "False")
        # print ['True' for x,y,z if (x**2+y**2+z**2 >2)]
    # answer = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if(i+j+k) != n]

K,M = input().strip().split()
k,m = int(K), int(M)

items = []
for _ in range(k):
     a = input().strip().split()
     b = list(map(int, a)) #convert into integers
     items.append(b[1:])
# print(items) #items: [[5, 4], [7, 8, 9], [5, 7, 8, 9, 10]]
make_modulo_max(items,m)

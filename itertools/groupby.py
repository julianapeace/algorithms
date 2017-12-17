"""
https://www.hackerrank.com/challenges/compress-the-string/problem
Submitted 9271 times

input:
1222311

output:
(1, 1) (3, 2) (1, 3) (2, 1)
"""
from itertools import groupby

s_list = list(input().strip()) #s_list: ['1', '2', '2', '2', '3', '1', '1']

ans = [] #ans: [[1, '1'], [3, '2'], [1, '3'], [2, '1']]
for key, group in groupby(s_list, lambda x: x):
    ans.append([len(list(group)), key])
    
print(' '.join('({}, {})'.format(*el) for el in ans))

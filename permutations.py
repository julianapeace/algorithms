"""
Write a program that takes two 11 integer array elements (one input per line) and gives output YES, if there's a permutation of the first array that is equal to the second array or gives output NO, if there's no such permutation.
Case1:
input:
1 2 5 3 7 0 7 3 5 2 1
7 3 1 2 5 0 5 2 1 3 7
output: YES
description: We can check that the first array can be changed to the following array: 7 3 1 2 5 0 5 2 1 3 7 so that makes the first array a permutation of the second array, giving answer YES. 
"""
import sys

input_str = sys.stdin.readlines()

string1 = input_str[0].split(' ')
string2 = input_str[1].split(' ')

string1 = map(int, string1)
string2 = map(int, string2)

string1 = sorted(string1)
string2 = sorted(string2)

if string1 == string2:
    print('YES')
else:
    print('NO')

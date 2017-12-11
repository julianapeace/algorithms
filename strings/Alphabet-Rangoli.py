"""
https://www.hackerrank.com/challenges/alphabet-rangoli/problem
Submitted 12014 times
"""
alphabet = []
for i in range(97,123):
    alphabet.append(chr(i))
def string_creator(size,index):
    string = []
    for i in range(size-1,index-1, -1):
        string.append(alphabet[i])
    for i in range(index-1, size):
        string.append(alphabet[i])
    nstring = "-".join(string)
    return nstring
"""
3 = 9
5 = 17
10 = 27
"""
def print_rangoli(size):
    # your code goes here
    width = size * 4 - 3
    for i in range(0,size-1):
        print(string_creator(size,size-i).center(width,"-"))
    for i in range(size-1,-1,-1):
        print(string_creator(size,size-i).center(width,"-"))

print_rangoli(10)

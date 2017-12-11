"""
Task

You are given two arrays ( & ) of dimensions X.
Your task is to perform the following operations:

Add ( + )
Subtract ( - )
Multiply ( * )
Divide ( / )
Mod ( % )
Power ( ** )
Input Format

The first line contains two space separated integers,  and .
The next  lines contains  space separated integers of array .
The following  lines contains  space separated integers of array .

Output Format

Print the result of each operation in the given order under Task.

Sample Input

1 4
1 2 3 4
5 6 7 8
Sample Output

[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]]
Use // for division in Python 3.
"""
import numpy

test_input = input()
value = test_input.split(" ")
n = int(value[0])
m = int(value[1])
a = []
b = []

for i in range(n, m+1):
    a.append(i)
for i in range(m+1, m+m+1):
    b.append(i)

a = numpy.array(a, int)
b = numpy.array(b, int)
# print(a)
# print(b)

out_list = [numpy.add(a, b), numpy.subtract(a, b), numpy.multiply(a, b), (a//b), numpy.mod(a, b), numpy.power(a, b)]


for x in range(0, len(out_list)):
    # print(out_list[x])
    new_list = "["
    # function = out_list[x]
    new_list += str(out_list[x])
    new_list += "]"
    # new_list.append(" ".join(str(out_list[x].tolist())))
    print(new_list)


# print (numpy.add(a, b))
# print (numpy.subtract(a, b))
# print(numpy.multiply(a, b))
# print(a//b)
# print (numpy.mod(a, b))
# print (numpy.power(a, b))

"""
Write a program that takes the center co-ordinates and radius of two circles and gives output YES< if they intersect each other, otherwise gives output NO. The input will be given in the following format.
x1 y1 c1
x2 y2 c2

One line for each circle, where xi, yi stands for the center coordinates of the i-th circle and ci for it's radius. Note that xi, yi, and ci are all integers.
]
Two circles intersect each other if it's not possible to find a line that separates them.

Case1:
0 0 1
0 0 2
Output: YES
Description: Since they share the same center coordinates, they intersect each other. 
"""

from math import sqrt
import sys

input_str = sys.stdin.readlines()

circle1 = input_str[0].split(' ')
circle2 = input_str[1].split(' ')

x1, y1, c1 = int(circle1[0]), int(circle1[1]), int(circle1[2])
x2, y2, c2 = int(circle2[0]), int(circle2[1]), int(circle2[2])

distance = sqrt((( x2 - x1 ) ** 2) + (( y2 - y1 ) ** 2 ))

if c1 + c2 >= distance:
    print('YES')
else:
    print('NO')

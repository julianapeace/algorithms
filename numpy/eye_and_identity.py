"""
URL:https://www.hackerrank.com/challenges/np-eye-and-identity/problem
identity

The identity tool returns an identity array. An identity array is a square matrix with all the main diagonal elements as  and the rest as . The default type of elements is float.

import numpy
print numpy.identity(3) #3 is for  dimension 3 X 3

#Output
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
eye

The eye tool returns a 2-D array with 's as the diagonal and 's elsewhere. The diagonal can be main, upper or lower depending on the optional parameter . A positive  is for the upper diagonal, a negative  is for the lower, and a   (default) is for the main diagonal.

import numpy
print numpy.eye(8, 7, k = 1)    # 8 X 7 Dimensional array with first upper diagonal 1.

#Output
[[ 0.  1.  0.  0.  0.  0.  0.]
 [ 0.  0.  1.  0.  0.  0.  0.]
 [ 0.  0.  0.  1.  0.  0.  0.]
 [ 0.  0.  0.  0.  1.  0.  0.]
 [ 0.  0.  0.  0.  0.  1.  0.]
 [ 0.  0.  0.  0.  0.  0.  1.]
 [ 0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.]]

print numpy.eye(8, 7, k = -2)   # 8 X 7 Dimensional array with second lower diagonal 1.
Task

Your task is to print an array of size X with its main diagonal elements as 's and 's everywhere else.

Input Format

A single line containing the space separated values of  and .
 denotes the rows.
 denotes the columns.

Output Format

Print the desired X array.

Sample Input

3 3
Sample Output

[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]

* Hackerrank Submitted 5962 times
"""
import numpy
# A single line containing the space separated values of N and M.

n = input()
value = n.split(" ")
if value[0] == value[1]:
    print(numpy.identity(int(value[0])))
else:
    print(numpy.eye(int(value[0]),int(value[1]), k=0))

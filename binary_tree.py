"""
Write a program that takes two integers N and D and a tree of exactly N vertices and N-1 edges. Your program should output the number of vertices that are at a distance of exactly D from the vertex 1.

Note: THe integer N and D wil be given in the first line (each separated by a space) and the tree will be given in the next N - 1 lines. Each of the next N - 1 lines will contain exactly two integers A and B (each separated by a single space), meaning that there's a bidirectional connection between vertex A and vertex B.

Note 2: A tree is a undirected acyclic graph in which any two vertices are connected by exactly one path.

Example:
Case 1:
4 1
1 2
1 3
1 4

Output of the program will be : 3
Description of the output: Vertices 2,3, and 4 are exactly one distance away from vertex 1.

Case 2:
4 2
1 2
2 3
3 4

Output of the program will be : 1
Description of the output: The only vertex which as distance two to vertex 1 is the vertex 3.
"""
#using the following line of code to fetch console input

import sys

input_str = sys.stdin.readlines()


string1 = input_str[0].split(' ')
string1 = map(int, string1)

stuff = []

for i in range(0, string1[0]):
 x = input_str[i].split(' ')
 x = map(int, x)
 stuff.append(x)


money = stuff[0][1]

#sort each list in a list
old_paths = stuff[1:]

paths = []
for i in old_paths:
   paths.append(sorted(i))

root = [1]
root_paths = []
for i in range(0, len(paths)):
   if 1 in paths[i]:
       root_paths.append(paths[i])
       for j in range(i, len(paths)-1):
           if paths[i][1] == paths[j+1][0]:
               temp = []
               temp.extend(paths[i])
               temp.extend([paths[j+1][1]])
               root_paths.append(temp)
count = 0

for x in root_paths:
   if (len(root) + len(x) - 2) == money:
       count += 1

print(count)

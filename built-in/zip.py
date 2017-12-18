"""
https://www.hackerrank.com/challenges/zipped/problem
Submitted 7339 times
iINPUT:
5 3
89 90 78 93 80
90 91 85 88 86
91 92 83 89 90.5
OUTPUT:
90.0
91.0
82.0
90.0
85.5
"""

N,X = input().strip().split() #N is number of students. X is number of tests
n,x = int(N), int(X)
grades = []
for _ in range(x):
    grades+=[map(float,input().strip().split())]
    #need to zip grades
# print(grades)#grades:[['89', '90', '78', '93', '80'], ['90', '91', '85', '88', '86'], ['91', '92', '83', '89', '90.5']]
student_grades = list(zip(*grades))
# print(student_grades)#[('89', '90', '91'), ('90', '91', '92'), ('78', '85', '83')]

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

for i in student_grades:
    print(mean(i))

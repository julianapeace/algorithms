"""
URL: https://www.hackerrank.com/challenges/finding-the-percentage/problem
submitted: Submitted 42339 times
"""

def findAvg(arr):
    answer = sum(arr) / len(arr)
    return ("%.2f" % answer)



if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    # print(student_marks)
    print(findAvg(student_marks[query_name]))
"""
example input:

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

"""

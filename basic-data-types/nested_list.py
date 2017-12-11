"""
URL:https://www.hackerrank.com/challenges/nested-list/problem
Submiited:Submitted 34193 times
"""
def solution():
    # print(arr) #arr is a global variable i guess
    #
    grades = []
    for i in range(0,len(arr)):
        grades.append(arr[i][1])
    # print("grades: ",grades)
    s_grades = sorted(grades)
    # print("sorted grades: ", s_grades)
    min_grade = min(s_grades)
    # print("minimum grade: ",min_grade)
    sec_min_grade = ""
    for i in s_grades:
        if i > min_grade:
            sec_min_grade = i
            break
    # print("Second lowest grade: ", sec_min_grade)
    value = []
    for i in range(0,len(arr)):
        if arr[i][1] == sec_min_grade:
            value.append(arr[i][0])
    for i in sorted(value):
        print(i)


if __name__ == '__main__':
    arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name,score])
        # print(name,score)
    solution()

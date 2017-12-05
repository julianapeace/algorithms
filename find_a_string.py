"""
https://www.hackerrank.com/challenges/find-a-string/problem
Submitted 35995 times
"""
# string = "ABcDCDC"
# substring = "CDC"

def count_substring(string, substring):
    count = 0
    for i in range(0,len(string)):
        ss = len(substring)
        if string[i:i+ss] == substring:
            count += 1
    print(count)
    return(count)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
# count_substring(string, substring)
"""
TestCaseTestCase
CaseT

1
"""

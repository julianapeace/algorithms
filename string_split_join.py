"""
URL:https://www.hackerrank.com/challenges/python-string-split-and-join/problem
Submitted 43679 times
"""
line = "this is a string"
def split_and_join(line):
    # write your code here
    print("-".join(line.split(" ")))
split_and_join(line)

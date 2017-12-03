"""
URL: https://www.hackerrank.com/challenges/python-tuples/problem
Task
Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of .

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

Input Format

The first line contains an integer, , denoting the number of elements in the tuple.
The second line contains  space-separated integers describing the elements in tuple .

Output Format

Print the result of hash(t).

Sample Input

2
1 2

Sample Output

3713081631934410656
"""
def testMap():
    def multiply(x):
        return (x*x)
    def add(x):
        return (x+x)

    funcs = [multiply, add]
    for i in range(5):
        value = list(map(lambda x: x(i), funcs))
        print(value)

def addDog(x):
    if x == 2:
        print("dog")
    print(x)

if __name__ == '__main__':
    # n = int(input()) #3
    # integer_list = map(int, input().split()) #3 2 1
    x_list = [2,4,6,7]
    print(x_list)
    value = list(map(lambda x: x**2, x_list))
    print(value)

    # t = (1,2,3)
    # print(t)
    # print(hash(t))

    # testMap()
































    # filler text at this line

"""
Read an integer .

Without using any string methods, try to print the following:


Note that "" represents the values in between.

Input Format
The first line contains an integer .

Output Format
Output the answer as explained in the task.

Sample Input

3
Sample Output

123\\*hackerrank Submitted 90857 times
"""

# def print_function(num):
#     num_list = []
#     for i in range(1, num+1):
#         num_list.append(i)
#     print (''.join(str(x) for x in num_list))
def print_function(num):
    num_list = []
    for i in range(1, num+1):
        num_list.append(i)
    print(*num_list, sep='')
n = 3
print_function(3)

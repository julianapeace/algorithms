"""
https://www.hackerrank.com/challenges/capitalize/problem
Submitted 19194 times
"""
string = "1 w 2 r 3g"
# string="hello world"
# string = "hello w0rld"
def capitalize(string):
    sstring = string.split()
    print(sstring)
    title = []
    for i in sstring:
        if i[0].isdigit():
            title.append(i)
        else:
            title.append(i.title())
    return " ".join(title)
print(capitalize(string))
"""
1 W 2 R 3g
"""

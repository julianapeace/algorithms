"""
url:https://www.hackerrank.com/challenges/whats-your-name/problem
Submitted 65245 times
"""
def print_full_name(a, b):
    #hackerrank compiler didn't accept f-strings
    # print(f'Hello {a} {b}! You just delved into python.')
    print("Hello {} {}! You just delved into python.".format(a,b))

# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)

print_full_name("Guido", "Rossum")
"""
Guido
Rossum
    >>> name = 'Fred'
    >>> age = 42
    >>> f'He said his name is {name} and he is {age} years old.'
    He said his name is Fred and he is 42 years old.
"""
